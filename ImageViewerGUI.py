# from my_package.model import ImageCaptioningModel
# from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog, Entry

image_label = None
file_way = ""


# captioner = ImageCaptioningModel()
# classifier = ImageClassificationModel()


def fileClick():
	# Define the function you want to call when the filebrowser button (Open) is clicked.
	# This function should pop-up a dialog for the user to select an input image file.
	# To have a better clarity, please check out the sample video.
	global image_label
	global file_way, image
	filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
	file_paths = filedialog.askopenfilenames(filetypes=filetypes)
	# Open the image file and resize it to fit within the specified max_size
	e.delete(0, END)
	e.insert(0, "Img" + file_paths[-6:])
	if file_paths:
		for file_path in file_paths:
			image = Image.open(file_path)
			image.resize((350, 350))
			file_way = file_path
	# Create an ImageTk object from the resized image and display it in a label
	image_tk = ImageTk.PhotoImage(image)
	if image_label:
		image_label.destroy()
	image_label = Label(image=image_tk)
	image_label.image = image_tk


def process():
	# This function will produce the required output when 'Process' button is clicked.
	# Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.
	if file_way == "":
		print("ERROR: Select a File First!")
		return
	if menu.get() == "Select Process":
		print("ERROR: Select a Process!")
		return
	if menu.get() == "Image Captioning":
		output = captioner(file_way)
		output_label.config(text="Output:\n1."+output[0]+"\n2."+output[1]+"\n3."+output[2]+"\n")
	if menu.get() == "Image Classification":
		output = classifier(file_way)
		output_label.config(text="Output:\n1."+str(output[0][0]*100)+"-"+output[0][1]+"\n2."+str(output[1][0]*100)+"-"+output[1][1]+"\n3."+str(output[2][0]*100)+"-"+output[2][1]+"\n")


if __name__ == '__main__':
	# Complete the main function preferably in this order:
	# Instantiate the root window.
	root = Tk()
	# Provide a title to the root window.
	root.title("Image Viewer | Python Assignment IV | 21CS10048")
	root.geometry("800x400")
	e = Entry(root, width=35, borderwidth=5)
	e.grid(row=0, column=0)
	# Instantiate the captioner, classifier models.
	# Declare the file browsing button.
	button_open = Button(root, text="Open", command=fileClick)
	# Declare the drop-down button.
	menu = StringVar()
	menu.set("Select Process")
	drop = OptionMenu(root, menu, "Image Captioning", "Image Classification")
	# Declare the process button.
	button_process = Button(root, text="Process", command=process)
	# Declare the output label
	image_label = Label(root, image="")
	image_label.grid(row=2, column=0)

	output_label = Label(root, text="")
	output_label.grid(row=2, column=1)

root.mainloop()
