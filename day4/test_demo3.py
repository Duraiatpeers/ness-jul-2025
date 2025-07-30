import openpyxl

import pytest


def get_data():

   wb = openpyxl.Workbook()
   sheet = wb.create_sheet("Data")

   sheet['A1'].value = "Admin"
   sheet['B1'].value = "admin"

   wb.save("testdata1.xlsx")



def test1():
   get_data()
