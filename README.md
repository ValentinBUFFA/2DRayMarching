# 2DRayMarching
Short 2D ray marching experiment from scratch.

## Usage
Execute rm_main.py to start program, you can move using z,q,s,d and mouse is used to give the ray a direction. <br/>
Right click to spawn a random-sized rectangle at cursor position. <br/>
Left click to spawn a random-sized circle at cursor position.

shapes.py contains the classes for different shapes, it is possible to add support for a new shape simply by adding a class with a 'dst(pos)' method, which gives the shortest distance between 'pos' and said shape.
