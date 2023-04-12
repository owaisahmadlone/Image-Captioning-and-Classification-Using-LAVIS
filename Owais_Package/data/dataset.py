# Imports
import jsonlines
from PIL import Image

class Dataset(object):
    """
        A class for the dataset that will return data items as per the given index
    """

    def __init__(self, annotation_file, transforms=None):
        """
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        """
        self.transforms = transforms

        # access annotation file

        with jsonlines.open(annotation_file, 'r') as json_file:
            self.json_list = [obj for obj in json_file]


    def __len__(self):
        """
            return the number of data points in the dataset
        """
        return len(self.json_list)
    
    def __getann__(self, idx):
        """
            return the data items for the index idx as an object
        """
        self.idx = idx
        dataidx = self.json_list[idx]
        return dataidx

    def __transformitem__(self, path):
        """
            return transformed PIL Image object for the image in the given path
        """
        # PIL image to be accepted
        image = Image.open(path)
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)

        # Transforming image as required
        if self.transforms is not None:
            for instanceTransform in self.transforms:
                image = instanceTransform(image)
        return image
