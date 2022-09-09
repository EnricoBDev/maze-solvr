from PIL import Image
import numpy as np

def draw_edge(img, start, end, color):
    c_vect = start.coords[1] - end.coords[1]
    r_vect = start.coords[0] - end.coords[0]

    if c_vect > 0:
        i = start.coords[1]
        while i >= end.coords[1]:
            img.putpixel((i, start.coords[0]), color)
            i -= 1
    if r_vect > 0:
        i = start.coords[0]
        while i >= end.coords[0]:
            img.putpixel((start.coords[1], i), color)
            i -= 1
    if c_vect < 0:
        i = start.coords[1]
        while i <= end.coords[1]:
            img.putpixel((i, start.coords[0]), color)
            i += 1
    if r_vect < 0:
        i = start.coords[0]
        while i <= end.coords[0]:
            img.putpixel((start.coords[1], i), color)
            i += 1

def resize_Image(image): # to use in gif creation
    """ Input parameter is PIL Image object """
    width, height = image.size
    if height < 300 and width < 300:
        resized = image.resize((width * 3, height * 3), resample = Image.Resampling.NEAREST)
    return resized

def create_gif(save_path, frames, speed, looping):
    frames[0].save(save_path, format = "GIF", append_images = frames,
        save_all = True, duration = 100 / speed, loop = looping)

def draw_path(image, color, solved_path, frames):
    """ Input parameter is PIL Image object """
    if len(solved_path) > 1:
        start = solved_path.pop()
        end = solved_path[-1]
        draw_edge(image, start, end, color)
        frames.append(image.convert("RGBA"))
        return draw_path(image, color, solved_path, frames)
    
    return resize_Image(image), frames

def draw_alg_frame(frame, start, end):

    GREEN = (0, 255, 0, 255)

    draw_edge(frame, start, end, GREEN)

    return frame

def create_full_gif(maze_image, solved_maze_image, solved_frames, execution_frames):
    full_frames = []
    full_frames.append(maze_image.convert("RGBA"))
    transparent_frames = []

    for i in execution_frames:
        maze_image.paste(i, (0, 0), i)
        full_frames.append(maze_image.convert("RGBA")) 
        # So apparently without the maze_image.convert() method 
        # all images in the list are equal to what the last one should be
        # If anyone has a fix for this please create a pr with the fix and hopefully an explanation
        # btw this fix is necessary whenever an image is appended to a list

    for solved_frame in solved_frames:
        array = np.asarray(solved_frame)
        for i in range(len(array)):
            for j in range(len(array[0])):
                if not np.array_equal(array[i][j], (255, 0, 0, 255)):
                    solved_frame.putpixel((j, i), (0, 0, 0, 0))
                    solved_frame.convert("RGBA")

        transparent_frames.append(solved_frame)

    maze_traversed = full_frames[-1].convert("RGBA")

    for transparent_frame in transparent_frames:
        maze_traversed.paste(transparent_frame, (0, 0), transparent_frame)
        full_frames.append(maze_traversed.convert("RGBA"))

    full_frames.append(solved_maze_image.convert("RGBA"))             

    return full_frames


# driver code for testing purposes
# im = Image.open(r"C:\Users\bassi\Documents\PythonScripts\maze_solver\maze.png")
# array = np.asarray(im)
# maze = create_maze(array)
# adj_list = create_adj_list(maze.matrix)
# print(adj_list)
# path = solve(maze, adj_list)
# finalImage = draw_path(im, r"animation", path, 0)
# finalImage = resize_Image(finalImage)
# finalImage.save("C:/Users/bassi/Documents/PythonScripts/maze_solver/animation/funzionaporcodio.png")
# im.close()
