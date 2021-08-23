from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import os

class Index:
	def __init__(self,path):
		self.path=path

	def main_fun(self):
		# initialize the color descriptor
		cd = ColorDescriptor((8, 12, 3))

		# open the output index file for writing
		output = open(self.path, "w")
		#data contains the path to your images folder
		data='/home/farhan/project/CBIR/my_contrib/test_dataset'
		# use glob to grab the image paths and loop over them
		types=['/*.png','/*.jpg']
		# os.chdir(data)
		for filetype in types:
			for imagePath in glob.glob(data+filetype):
				# extract the image ID (i.e. the unique filename) from the image
				# path and load the image itself
				imageID = imagePath[imagePath.rfind("/") + 1:]
				image = cv2.imread(imagePath)

				# describe the image
				features = cd.describe(image)

				# write the features to file
				features = [str(f) for f in features]
				output.write("%s,%s\n" % (imageID, ",".join(features)))

			# close the index file
		output.close()
