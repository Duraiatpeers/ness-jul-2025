import openpyxl

import pytest
from openpyxl import load_workbook


def test_demo():

    wb = load_workbook("testdata1.xlsx")
    sheet = wb["Data"]

    print(sheet.title)
    sheet['C1'] = "Pass"
    sheet['C2'] = "Fail"

    wb.save("testdata1.xlsx")
