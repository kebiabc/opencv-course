import numpy as np
import cv2
import cvui

WINDOW_NAME = 'GUI1'

def main():
    path = input("Please enter the path of the image\n")
    image = cv2.imread("{}.png".format(path))
    frame = np.zeros(image.shape, np.uint8)

    # Init cvui and tell it to create a OpenCV window, i.e. cv2.namedWindow(WINDOW_NAME).
    cvui.init(WINDOW_NAME)

    while (True):
        frame[:] = image[:]
        if cvui.button(frame, 20, 20, 'Displaying'):
                cvui.printf(frame, 200, 95, 'Button clicked!')
                (h, w, c) = image.shape[:3]
                print("image heigth: {}".format(image.shape[0]))
                print("image width: {}".format(image.shape[1]))
                print("image channels: {}".format(image.shape[2]))
                # Render the settings window to house the checkbox
                # and the trackbars below.
                # cvui.window(frame, 10, 50, 180, 180, 'Settings')
        if cvui.button(frame, 20, 60, 'Translation'):
                cvui.printf(frame, 200, 95, 'Button clicked!')
                M = np.float32([[1, 0, 25], [0, 1, 50]])
                shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
                cv2.imshow("Shifted", shifted)

        if cvui.button(frame, 20, 100, 'Rotating'):
                cvui.printf(frame, 200, 95, 'Button clicked!')
                (h, w) = image.shape[:2]
                (cX, cY) = (w // 2, h // 2)
                M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0) 
                rotated = cv2.warpAffine(image, M, (w, h))
                cv2.imshow("Rotated", rotated)     
                
        if cvui.button(frame, 20, 150, 'Splitting'):
                cvui.printf(frame, 200, 95, 'Button clicked!')
                (B, G, R) = cv2.split(image)
                cv2.imshow("Blue channel", B)
                cv2.imshow("Green channel", G)
                cv2.imshow("Red channel", R)

        # This function must be called *AFTER* all UI components. It does
        # all the behind the scenes magic to handle mouse clicks, etc.
        cvui.update()

        # Show everything on the screen
        cv2.imshow(WINDOW_NAME, frame)

        # Check if ESC key was pressed
        if cv2.waitKey(20) == 27:
            break

if __name__ == '__main__':
    main()

