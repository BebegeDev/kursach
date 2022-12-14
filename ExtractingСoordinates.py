import cv2
import test1


class ExtractingCoord:

    def __init__(self, agregat_n):
        self.agregat_n = agregat_n

    def get_images(self):
        images = {"Graf/Ag7.png": "Агрегат 7"}
        image = cv2.imread("Ag7.png", 1)
        cv2.imshow('image', image)


agregat_n = test1.obj_interface.get_s()
s = ExtractingCoord(agregat_n)
s.get_images()