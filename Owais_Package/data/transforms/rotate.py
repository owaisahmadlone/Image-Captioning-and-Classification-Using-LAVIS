# Imports
import PIL
from PIL import Image
from numpy import asarray


class RotateImage(object):
	"""
		Rotates the image about the centre of the image.
	"""

	def __init__(self, degrees):
		"""
			Arguments:
			degrees: rotation degree.
		"""

		# Write your code here

		self.degree = degrees

	def __call__(self, sample):
		"""
			Arguments:
			image (numpy array or PIL image)

			Returns:
			image (numpy array or PIL image)
		"""

		# Write your code here
		if not isinstance(sample, PIL.Image.Image):  # if given as numpy array, then convert into PIL Image
			sample = Image.fromarray(sample)

		return sample.rotate(self.degree)


# Test
"""
if __name__ == "__main__":
	img = Image.open("")
	rotate = RotateImage(90)
	img = rotate(img)
	img_ = asarray(img.convert("RGB"))
	print(img_.shape)
	img.show()
"""