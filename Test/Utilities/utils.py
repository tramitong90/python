import unittest
import xlrd
import csv
from openpyxl import load_workbook

class Utils(unittest.TestCase):

    def read_data_from_csv(file_name):
        datalist = []
        csvdata = open(file_name, "r")
        reader = csv.reader(csvdata)
        next(reader)
        for rows in reader:
           datalist.append(rows)
        return datalist
