# Imports
import numpy as np
import PIL
from PIL import Image


class CropImage(object):
    """
        Performs either random cropping or center cropping.
    """

    def __init__(self, shape, crop_type='center'):
        """
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        """

        # Write your code here

        self.cropType = crop_type
        self.finalHeight, self.finalWidth = shape

    def __call__(self, image):
        """
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        """

        # Write your code here
        if not isinstance(image, PIL.Image.Image):  # if given as numpy array, then convert into PIL Image
            image = Image.fromarray(image)

        wid, ht = image.size
        if self.cropType == "center":  # Center Crop
            centre_x = wid / 2
            centre_y = ht / 2
        else:  # Random Crop
            centre_x = np.random.randint(self.finalWidth / 2, wid - self.finalWidth / 2)
            centre_y = np.random.randint(self.finalHeight / 2, ht - self.finalHeight / 2)

        # Calculating coordinates
        lpos = centre_x - self.finalWidth / 2
        rpos = centre_x + self.finalWidth / 2
        tpos = centre_y - self.finalHeight / 2
        bpos = centre_y + self.finalHeight / 2

        return image.crop((lpos, tpos, rpos, bpos))


# Testing
"""
if __name__ == "__main__":
    img = Image.open("/Users/owaisahmadlone/Desktop/Dark_vignette_Al-Masjid_AL-Nabawi_Door800x600x300.jpeg")
    crop = CropImage((300, 300), "center")
    img = crop(img)
    # img2 = asarray(img.convert("RGB"))
    # print(img2.shape)
    img.show()
"""
