#!/usr/bin/python
import os
import sift


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg")]


path = "/home/farhan/Desktop/"
imlist = get_imlist(path)

nbr_images = len(imlist)
featlist = [imlist[i][:-3] + "sift" for i in range(nbr_images)]
# print featlist
sift.process_image(imlist[0], featlist[0])
