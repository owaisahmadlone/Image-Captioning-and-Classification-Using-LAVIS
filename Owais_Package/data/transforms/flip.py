# Imports
import PIL
from PIL import Image

class FlipImage(object):
	"""
		Flips the image.
	"""

	def __init__(self, fliptype='horizontal'):
		"""
		Arguments:
		flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
		"""

		# Write your code here

		self.fliptype = fliptype

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

		if self.fliptype == "horizontal":
			return image.transpose(method=Image.FLIP_TOP_BOTTOM)
		else:
			return image.transpose(method=Image.FLIP_LEFT_RIGHT)


# Testing

"""
if __name__ == "__main__":
	img = Image.open("/Users/owaisahmadlone/Desktop/Dark_vignette_Al-Masjid_AL-Nabawi_Door800x600x300.jpeg")
	flip = FlipImage("vertical")
	img = flip(img)
	# img2 = asarray(img.convert("RGB"))
	# print(img2.shape)
	img.show()
"""