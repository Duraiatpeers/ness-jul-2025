import pytest

from openpyxl import load_workbook


def get_test_data():
    test_data = []
    data_file = '.\TestData\LoginData.xlsx'

    testdata_workbook = load_workbook(data_file)
    ws = testdata_workbook.active

    print(ws['A1'])
    print(ws['A1'].value)
    return test_data

get_test_data()
# @pytest.mark.parametrize('username,password',get_test_data())
# def test_param(username,password):
#     print(username)
#     print(password)
