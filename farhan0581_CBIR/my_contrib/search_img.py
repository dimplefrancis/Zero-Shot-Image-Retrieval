# class to search images from database on the basis of keypoints...
import MySQLdb as mdb
import cv2
import csv
import numpy as np
from matplotlib import pyplot as plt
import os, glob
from collections import OrderedDict
from operator import itemgetter
import itertools


class Searcher:
    def __init__(self, image_name):

        self.image = image_name
        self.host = "localhost"
        self.user = "root"
        self.db = "cbir"
        self.password = ""

    def search_image(self):

        in_img = self.image
        # test_dataset is the name of the image folder
        query_img = cv2.imread("test_dataset/" + in_img)
        orb = cv2.ORB_create()
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        kp, des = orb.detectAndCompute(query_img, None)
        con = mdb.connect(self.host, self.user, self.password, self.db)
        cur = con.cursor()
        query = "select name,des from prop1 where name like '%jpg' OR name like '%png'"
        cur.execute(query)
        rows = cur.fetchall()
        res_dict = {}
        for row in rows:
            val = 0
            dess = np.ma.loads(row[1])
            matches = bf.match(des, dess)
            matches = sorted(matches, key=lambda x: x.distance)
            for dis in matches[:15]:
                val += dis.distance
            res_dict[row[0]] = val
        # sorting the dictionary and display the top results
        d = OrderedDict(sorted(res_dict.items(), key=itemgetter(1)))
        x = itertools.islice(d.items(), 0, 5)
        for value in x:
            to_show = cv2.imread("test_dataset/" + value[0])
            r = 300.0 / to_show.shape[1]
            dim = (300, int(to_show.shape[0] * r))
            resized = cv2.resize(to_show, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow("RESULT", resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    print "this is meant for import only!!"
