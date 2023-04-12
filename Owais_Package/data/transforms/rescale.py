# Imports
from PIL import Image
import PIL


class RescaleImage(object):
	"""
		Rescales the image to a given size.
	"""

	def __init__(self, output_size):
		"""
			Arguments:
			output_size (tuple or int): Desired output size. If tuple, output is
			matched to output_size. If int, smaller of image edges is matched
			to output_size keeping aspect ratio the same.
		"""

		self.size = output_size

	def __call__(self, image):
		"""
			Arguments:
			image (numpy array or PIL image)

			Returns:
			image (numpy array or PIL image)

			Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
		"""

		img = image

		if not isinstance(image, PIL.Image.Image):
			img = Image.fromarray(image)

		res = img

		if isinstance(self.size, tuple):
			res = img.resize(self.size)

		if isinstance(self.size, int):
			x, y = img.size
			if x < y:
				wid = self.size
				hgt = y * wid//x
			else:
				hgt = self.size
				wid = x * hgt//y
			mod_size = (wid, hgt)
			res = img.resize(mod_size)
		return res

"""
if __name__ == "__main__":
	img_ = Image.open("")
	new_size = [2*img_.size[0], 2*img_.size[1]]
	print(new_size)
	rescale = RescaleImage([])
	img_out = rescale(img_)
	print(img_out.size)
	img_out.show()
"""
