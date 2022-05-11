 TASK1
 
 Create an application that performs all the tasks provided
▪ The program will ask the user to provide an image.
▪ Within the program will have the buttons to provide all the actions that the user will ask 
such as displaying its dimensions, draw on it, rotate, translate etc.
▪ An application with a GUI is recommended.

To start, enter the relative path of the image on the command line.Then through the button it can display dimensions, rotate, translate etc.Press ESC to exit.

Since opencv does not provide an option for buttons, I found a library called cvui.It is close to the native GUI function of opencv, but provides a more friendly interface design.

But the call interface of the mouse still uses its own, so it is placed in draw.py separately.