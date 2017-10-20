# pxsort

This is a simple little Python program to do some pixel sorting.

Usage example:

    import cv2, pxsort
    img = cv2.imread('river.jpg')
    pxsort.vertical_sort(img,100,500) #image array, brightness-min, brightness-max
    cv2.imwrite('river_vsort.jpg',img)
