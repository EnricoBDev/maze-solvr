<h1 align="center">
  <br>
  <img title='logo' src='assets\icons\mazesolverlogo.png'>
  <br>
  A minimal application for solving mazes built with tkinter
  <br>
</h1>

<p align='center'>
  <img src='https://img.shields.io/github/last-commit/EnricoBDev/maze-solvr?style=for-the-badge' />
  <img src='https://img.shields.io/github/stars/EnricoBDev/maze-solvr?style=for-the-badge' />
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#create-new-mazes">Create New Mazes</a> •
  <a href="#credits">Credits</a> •
  <a href="#how-does-the-app-work">How does the app work</a>
</p>

<h1 align="center">
  <img title='example' src='assets\example.gif'>
</h1>

## Key Features

- BFS algorithm for maze solving
- Option to generate animated gif
- Option to loop generated gif
- Slider to control gif speed

## How To Use

``` bash
# Clone the repository
git clone https://github.com/EnricoBDev/maze-solvr.git

# Install the required dependencies
cd maze-solver
pip install -r requirements.txt

# Run the app
python main.py
```

Testing mazes can be found in

``` text
assets/test_images
```

## Create New Mazes

To create new mazes you can use any image manipulation program, you just need to follow these rules:

- The image must be in png format
- The start and end points must be indicated with 2 blue ```#0000ff``` pixels
- The walls/obstacles must be indicated with black ```#000000``` pixels
- The navigable paths must be indicated with white ```#ffffff``` pixels

## How does the app work?

As I said previously, this application uses the BFS (Breadth First Search) algorithm, this is an important algorithm used extensively when working with graphs.

But since the input file is an image, how do we generate the adjacency list used to describe the maze in a graph format?

The application follows the following steps:

1. First of all we tranform the image file in a pixel matrix,
2. Then we recreate the pixel matrix but we substitute each pixel value with a predefined constant for every pixel color,
3. After this we find the two blue pixels (indicating the start and the end of the maze), and we save those
4. Finally, by using a recursive algorithm to follow the white path, we take each pixel and we find its neighbours.

Now all that's left to do is to run the algorithm on the adjacency list:

```python
# solve.py

def solve(maze, adj_list):
    start = maze.start
    end = maze.end

    queue = deque([start])
    visited = [False] * (maze.width * maze.height)
    prev = [None] * (maze.width * maze.height)

    visited[start.coords[0] * maze.width + start.coords[1]] = True

    while queue:
        current = queue.pop()

        if current.__repr__() == end.__repr__():
            break
        
        for i in adj_list.get(current.__repr__()):
            visited_pos = i.coords[0] * maze.width + i.coords[1]
            if visited[visited_pos] == False:    
                queue.appendleft(i)
                visited[visited_pos] = True
                prev[visited_pos] = current
        

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.coords[0] * maze.width + current.coords[1]]
    
    if len(path) > 1:
        return path
    else: 
        return False
```

## Credits

The app icon can be found [here](https://www.flaticon.com/free-icons/maze)

This app is powered by the following open source projects:

- [Pillow](https://github.com/python-pillow/Pillow), image manipulation library

- [Numpy](https://github.com/numpy/numpy), array and matrix manipulation library

- [Tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter), gui library included in the std library
