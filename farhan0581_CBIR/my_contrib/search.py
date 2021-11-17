from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2


class Search:
    def __init__(self, image_name, path):
        self.name = image_name
        self.file_path = path
        # path of your folder containing images
        self.data_path = "/home/farhan/project/CBIR/my_contrib/test_dataset"

    def main_search(self):
        cd = ColorDescriptor((8, 12, 3))

        # load the query image and describe it
        query = cv2.imread("test_dataset/" + self.name)
        features = cd.describe(query)

        # perform the search
        searcher = Searcher(self.file_path)
        results = searcher.search(features)

        # display the query
        cv2.imshow("Query", query)

        # loop over the results
        for (score, resultID) in results:
            # load the result image and display it
            result = cv2.imread(self.data_path + "/" + resultID)
            r = 300.0 / result.shape[1]
            dim = (300, int(result.shape[0] * r))
            resized = cv2.resize(result, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow("RESULT", resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
