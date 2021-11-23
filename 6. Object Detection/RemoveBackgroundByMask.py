import cv2
import common.ImageProcessing as ip

def remove_background(image, mask):
    iproc = ip.ImageProcessing("Original", image)
    iproc.show(image=iproc.image)
    mask = cv2.imread(mask)
    iproc.show(title="Mask", image=mask)
    bg_removed, _ = iproc.remove_background_by_mask(mask)
    iproc.show(title="Background Removed", image=bg_removed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    remove_background(image = "../res/flower010.jpg",
                      mask = "../res/flower010_mask.jpg")
