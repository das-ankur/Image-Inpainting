import numpy as np
import cv2
if __name__ == '__main__':
    img_file = input("Enter the image file: ")
    mask_file = input("Enter the mask file: ")
    try:
        img = cv2.imread(img_file)
        mask = cv2.imread(mask_file, 0)
    except:
        print("Exception occurs during  reading")
    res = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
    # res = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
    cv2.imshow("Actual Image", img)
    cv2.imshow("Processed Image", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()