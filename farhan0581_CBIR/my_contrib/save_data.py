import MySQLdb as mdb
import cv2
import csv
import numpy as np
from matplotlib import pyplot as plt
import os, glob
from collections import OrderedDict
from operator import itemgetter
import itertools


class Data_index:

    """indexing the features to mysql"""

    def __init__(self, path):
        self.path = path
        self.host = "localhost"
        self.user = "root"
        self.db = "cbir"
        self.password = ""

    def insert_data(self):

        con = mdb.connect(self.host, self.user, self.password, self.db)
        cur = con.cursor()
        types = ["*.png", "*.jpg"]
        os.chdir(self.path)
        for filetype in types:
            for fil in glob.glob(filetype):
                img = cv2.imread(self.path + fil)
                orb = cv2.ORB_create()
                kp, desc = orb.detectAndCompute(img, None)
                byte = desc.dumps()
                cur.execute(
                    """insert ignore into prop1(name,des) values(%s,%s)""", (fil, byte)
                )
                con.commit()


if __name__ == "__main__":
    print "This is meant for import only!!"
