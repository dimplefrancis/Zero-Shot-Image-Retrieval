import cv2
from PIL import Image
from numpy import *
from pylab import *
import os

def process_image(imagename,resultname,params="--edge-thresh 10 --peak-thresh 5"):

	image = cv2.imread(imagename)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	sift = cv2.xfeatures2d.SIFT_create()
	(kps, descs) = sift.detectAndCompute(gray, None)
	handle=open(resultname,'w+')
	handle.write(descs)


	# if imagename[:-3]!='pgm':
	# 	im=Image.open(imagename).convert('L')
	# 	im.save('tmp.pgm')
	# 	imagename='tmp.pgm'
	# # cmmd= str("sift "+imagename+" --output="+resultname+
	# # 		" "+params)
	# # os.system(cmmd)
	# gray = cv2.cvtColor(imagename, cv2.COLOR_BGR2GRAY)
	# sift = cv2.xfeatures2d.SIFT_create()
	# (kps, descs) = sift.detectAndCompute(gray, None)
	# print 'processed',imagename, 'to', resultname



# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# sift = cv2.xfeatures2d.SIFT_create()
# (kps, descs) = sift.detectAndCompute(gray, None)