from PIL import Image

def draw_edge(img, start, end):


    RED = (255, 0, 0, 255)
    c_vect = start.coords[1] - end.coords[1]
    r_vect = start.coords[0] - end.coords[0]

    if c_vect > 0:
        i = start.coords[1]
        while i >= end.coords[1]:
            img.putpixel((i, start.coords[0],) ,RED)
            i -= 1
    if r_vect > 0:
        i = start.coords[0]
        while i >= end.coords[0]:
            img.putpixel((start.coords[1], i), RED)
            i -= 1
    if c_vect < 0:
        i = start.coords[1]
        while i <= end.coords[1]:
            img.putpixel((i, start.coords[0]), RED)
            i += 1
    if r_vect < 0:
        i = start.coords[0]
        while i <= end.coords[0]:
            img.putpixel((start.coords[1], i), RED)
            i += 1

def resize_Image(image): # to use in gif creation
    """ Input parameter is PIL Image object """
    width, height = image.size
    if height < 300 and width < 300:
        resized = image.resize((width * 3, height * 3), resample = Image.Resampling.NEAREST)
    return resized

def create_gif(save_path, frames):
    first_frame = frames[0]
    first_frame.save(save_path, format = "GIF", append_images = frames,
        save_all = True, duration = 100, loop = 0
    )

def draw_path(image, animation_path, solved_path, frames):
    """ Input parameter is PIL Image object """
    if len(solved_path) > 1:
        start = solved_path.pop()
        end = solved_path[-1]
        draw_edge(image, start, end)
        # cv2.imwrite(f"/{animation_path}/maze{index}.png", img)
        resized_image = resize_Image(image)
        frames.append(resized_image)
        return draw_path(image, animation_path, solved_path, frames)
    
    return image, frames


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
