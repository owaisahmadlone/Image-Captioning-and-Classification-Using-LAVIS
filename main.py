# Imports
from Owais_Package.model import ImageCaptioningModel
from Owais_Package.data import dataset, download
from Owais_Package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    """
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    """

    # Create the instances of the dataset, download
    data_set = dataset.Dataset(annotation_file, transforms)
    downld = download.Download()


    # Print image names and their captions from annotation file using dataset object
    obj = data_set.__getann__(8)
    print("Image name: " , obj['file_name'] , ", Image Caption: " , obj['captions'])


    # Download images to ./data/imgs/ folder using download object

    downld.path = 'Python_DS_Assignment_Question_02_21CS10048 copy/data/imgs'+'/' + obj['file_name']
    downld.url = obj['url']
    downld.__call__(downld.path, downld.url)


    # Transform the required image (roll number mod 10) and save it seperately
    img = data_set.__transformitem__(downld.path)
    img.save(outputs)

    # Get the predictions from the captioner for the above saved transformed image
    print(captioner(outputs, 3))

def main():
    captioner = ImageCaptioningModel()
    # Sample arguments to call experiment()
    # Printing the same Image
    experiment('Python_DS_Assignment_Question_02_21CS10048 copy/data/annotations.jsonl', captioner, [], 'Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_A.jpg')
    print("First experiment is Completed")

    # Flipping the Image
    experiment('Python_DS_Assignment_Question_02_21CS10048 copy/data/annotations.jsonl', captioner, [FlipImage('horizontal')], "Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_B.jpg")
    print("Second experiment is Completed")

    # Blurring the Image
    experiment('Python_DS_Assignment_Question_02_21CS10048 copy/data/annotations.jsonl', captioner, [BlurImage(20)], "Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_C.jpg")
    print("Third experiment is Completed")

    # Rescaling to 2 times the size
    img_ = Image.open('Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_A.jpg')
    new_size = (int (2*img_.size[0]), int (2*img_.size[1]))
    experiment('Python_DS_Assignment_Question_02_21CS10048 copy/data/annotations.jsonl', captioner, [RescaleImage(new_size)], "Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_D.jpg")
    print("Fourth experiment is Completed")

    # Rescaling to 0.5 times the size
    neww_size = (int (0.5*img_.size[0]),int (0.5*img_.size[1]))
    experiment('Python_DS_Assignment_Question_02_21CS10048 copy/data/annotations.jsonl', captioner, [RescaleImage(neww_size)], "Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_E.jpg")
    print("Fifth experiment is Completed")

    # Rotating by 90 degree clockwise
    experiment('Python_DS_Assignment_Question_02_21CS10048 copy/data/annotations.jsonl', captioner, [RotateImage(-90)], "Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_F.jpg")
    print("Sixth experiment is Completed")

    # Rotating by 45 degree anti clockwise
    experiment('Python_DS_Assignment_Question_02_21CS10048 copy/data/annotations.jsonl', captioner, [RotateImage(45)], "Python_DS_Assignment_Question_02_21CS10048 copy/outputs/8_G.jpg")
    print("Seventh experiment is Completed")

if __name__ == '__main__':
    main()