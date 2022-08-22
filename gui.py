from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from pathlib import Path
import numpy as np
import subprocess, os, platform

from color_matrix import create_maze
from create_adj_list import create_adj_list
from solve import solve
from img_manipulation import create_gif, draw_path

def preview_accepted():
    top_popup.destroy()
    solve_btn["state"] = "normal"

def preview_declined():
    top_popup.destroy()

def open_img():
    global preview, top_popup, filename_open_path

    # disables the user from opening multiple windows simultaneously
    open_img_btn["state"] = "disabled"

    # opens the file explorer
    filetypes = (("Image files", "*.png"), ("All files", "*.*"))
    filename_open_path = filedialog.askopenfilename(
        initialdir = Path.cwd(), 
        title = "Choose an image file", 
        filetypes = filetypes)
    
    # if the user does not open the image it will just return back to the root window
    if filename_open_path:

        # creates the window
        top_popup = Toplevel()
        top_popup.geometry =("+100+100")
        top_popup.iconbitmap("assets/icons/maze.ico")
        top_popup.lift()
        top_popup.focus_force()
        top_popup.title("Maze solver")

        # opens the image and resises it if it is too small
        preview_Image = Image.open(filename_open_path)
        width, height = preview_Image.size
        if height < 300 and width < 300:
            preview_Image = preview_Image.resize((width * 3, height * 3), resample = Image.Resampling.NEAREST)
        
        # displays the image
        preview = ImageTk.PhotoImage(preview_Image)
        preview_lbl = ttk.Label(top_popup, image = preview)
        preview_lbl.grid(column = 0, row = 0, pady = (10, 0))
        
        # label and buttons layout
        ttk.Label(top_popup, text = "Is this the image you wanted?").grid(column = 0, row = 1, pady = 10) 

        btn_frame = Frame(top_popup, height = 200, width = 200)
        btn_frame.grid(column = 0, row = 2, pady = (5, 10))

        y_btn = ttk.Button(btn_frame, text = "Yes", command = preview_accepted)
        y_btn.grid(column = 0, row = 0, padx = 10)

        n_btn = ttk.Button(btn_frame, text = "No", command = preview_declined)
        n_btn.grid(column = 1, row = 0, padx = 10)

    # now the user can open another window
    open_img_btn["state"] = "normal"

def solve_maze():
    open_img_btn["state"] = "normal"
    solve_btn["state"] = "disabled"
    img = Image.open(filename_open_path)
    array = np.asarray(img)

    maze = create_maze(array)

    if maze:
        adj_list = create_adj_list(maze.matrix)
        path = solve(maze, adj_list)
        
        if not path:
            messagebox.showerror( title = "Error", message = "The maze you chose is not solvable")
        else:
            filetypes = (("Image files", "*.png"), ("All files", "*.*"))
            filename_save_path = filedialog.asksaveasfilename(
                filetypes = filetypes,
                initialdir = Path.cwd(),
                title = "Save solved maze"
            )

            gif_save_path = Path(filename_save_path).stem + ".gif"

            finalImage, frames = draw_path(img, filename_save_path, path, list())
            if isGifCreated.get():
                create_gif(gif_save_path, frames)
            finalImage.save(filename_save_path)
            img.close()

            if platform.system() == "Darwin":       # macOS 
                subprocess.call(('open', filename_save_path), check=True)
            elif platform.system() == "Windows":    # windows
                os.startfile(filename_save_path)
            else:                                   # linux 
                subprocess.call(("xdg-open", filename_save_path), check=True)
                
            filename_save_path = ""
    else:
        messagebox.showerror( title = "Error", message = "There are too many/too little entry/finish points")


root = Tk()
root.geometry("350x400")
root.title("Maze solver")
root.resizable(False, False)
root.iconbitmap("assets/icons/maze.ico")

isGifCreated = BooleanVar(root)

open_img_btn = ttk.Button(root, text = "Open Image", command = open_img)
open_img_btn.grid(column = 0, row = 0, padx = (10, 0), pady = (10, 0))

solve_btn = ttk.Button(root, text = "Solve Image", command = solve_maze)
solve_btn.grid(column = 1, row = 0, padx = (5, 0), pady = (10, 0))
solve_btn["state"] = "disabled"

checkbox = Checkbutton(root, text = "Generate gif", variable = isGifCreated, onvalue = True, offvalue = False)
checkbox.grid(column = 2, row = 0, padx = (5, 0), pady = (10, 0))

if __name__ == "__main__":
    root.mainloop()