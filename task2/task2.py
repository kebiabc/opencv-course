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
        if cvui.button(frame, 20, 20, 'GaussianBluring'):
                cvui.printf(frame, 200, 95, 'Button clicked!')
                kernelSizes = [(3, 3), (7, 7), (17, 17)]
                # loop over the kernel sizes
                for (kX, kY) in kernelSizes:
                # apply an "average" blur to the image using the current kernel size
                    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
                    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)

        if cvui.button(frame, 20, 60, 'Adaptive Thresholding'):
                cvui.printf(frame, 200, 95, 'Button clicked!')
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (7,7), 0)
                cv2.imshow("Original", image)
                thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
                cv2.imshow("Mean Adaptive Thresholding", thresh)  
                
        if cvui.button(frame, 20, 100, 'Gradients'):
                cvui.printf(frame, 200, 95, 'Button clicked!')
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imshow("Original", image)
                ksize = 3
                gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
                gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

                # the gradient magnitude images are now of the floating point data type, so we need to take
                # care to convert them back a to unsigned 8-bit integer representation so other OpenCV functions can operate
                # on them and visualize them
                gX = cv2.convertScaleAbs(gX)
                gY = cv2.convertScaleAbs(gY)

                # combine the gradient representations into a single image
                combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

                # show our output images
                cv2.imshow("Sobel X", gX)
                cv2.imshow("Sobel Y", gY)
                cv2.imshow("Sobel Combined", combined)

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