<div style='text-align: center;'>
<img title='logo' src='assets\icons\mazesolverlogo.png'>
</div>

<h2 align='center'>
A minimal application for solving mazes built with tkinter
</h2>

<p align='center'>
  <img src='https://img.shields.io/github/last-commit/EnricoBDev/maze-solvr?style=for-the-badge' />
  <img src='https://img.shields.io/github/stars/EnricoBDev/maze-solvr?style=for-the-badge' />
</p>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#create-new-mazes">Create New Mazes</a> •
  <a href="#known-issues">Known Issues</a> •
  <a href="#credits">Credits</a>
</p>

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

## Known Issues

- At the end of the generated gif a strange bugged image appears

## Credits

The app icon can be found [here](https://www.flaticon.com/free-icons/maze)

This app is powered by the following open source projects:

- [Pillow](https://github.com/python-pillow/Pillow)

- [Numpy](https://github.com/numpy/numpy)

- [Tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)
