import PIL.Image
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog

# Screen Setup
WIN = Tk()
WIN.title("Image Compressor")


class Compression:
	def __init__(self, window):
		self.file_name = None
		self.export_path = None
		self.label_filename = None
		self.label_export = None
		self.quality = None
		self.win = window

	def build_gui(self):
		# Select File
		open_btn = Button(self.win, text="Select Image", command=self.select_file)
		open_btn.grid(row=0, column=0, padx=20, pady=10)
		self.label_filename = Label(self.win, text="File Name: ")
		self.label_filename.grid(row=0, column=1, columnspan=2, padx=20, pady=20)
		# Select Export Path
		path_btn = Button(self.win, text="Export Path", command=self.select_export_path)
		path_btn.grid(row=1, column=0, padx=20, pady=10)
		self.label_export = Label(self.win, text="Export Path: ")
		self.label_export.grid(row=1, column=1, columnspan=2, padx=20, pady=20)
		# Compress Image
		label_quality = Label(self.win, text="Image Quality: ")
		label_quality.grid(row=2, column=0, padx=20, pady=10)
		self.quality = Scale(self.win, from_=0, to=100, orient=HORIZONTAL, length=200)
		self.quality.set(30)
		self.quality.grid(row=2, column=1, columnspan=2, padx=20, pady=10)
		compress_btn = Button(self.win, text="Compress Image", command=self.compress_image)
		compress_btn.grid(row=4, column=0, padx=20, pady=10)

	def select_file(self):
		self.file_name = filedialog.askopenfilename(initialdir="/", title="Select a Image", filetypes=(("png", "*.png"), ("jpg", "*.jpg")))
		self.label_filename.config(text=f"File Name: {self.file_name}")

	def select_export_path(self):
		self.export_path = filedialog.askdirectory(initialdir="/", title="Select Export Path")
		self.label_export.config(text=f"Export Path: {self.export_path}")

	def compress_image(self):
		if self.file_name != None: 
			img = PIL.Image.open(self.file_name)
			name = self.file_name.split("/")[-1].split(".")[0]

			if img.format == "JPEG":
				img_format = "jpg"

			if img.format == "PNG":
				img_format = "png"

			img.save(f"{self.export_path}/{name}_compressed.{img_format}", optimize=True, quality=self.quality.get())

			self.label_filename.config(text="File Name: ")
			self.label_export.config(text="Export Path: ")

			label_feedback = Label(self.win, text="Success")
			label_feedback.grid(row=4, column=1, padx=20, pady=10)



c = Compression(WIN)

c.build_gui()	

WIN.mainloop()
