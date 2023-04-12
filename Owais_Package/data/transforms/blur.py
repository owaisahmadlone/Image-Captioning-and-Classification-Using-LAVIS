# Imports
import PIL
from PIL import Image, ImageFilter


class BlurImage(object):
    """
        Applies Gaussian Blur on the image.
    """

    def __init__(self, radius):
        """
            Arguments:
            radius (int): radius to blur
        """
        self.radius = radius

    def __call__(self, image):
        """
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        """

        # Write your code here
        if not isinstance(image, PIL.Image.Image):  # if the image is given as the numpy array, convert to PIL Image
            image = Image.fromarray(image)

        return image.filter(ImageFilter.GaussianBlur(self.radius))


# Test
"""
if __name__ == "__main__":
    img = Image.open("")
    blur = BlurImage(1)
    img = blur(img)
    img.show()
"""