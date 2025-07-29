import csv

import pytest


# fetching data from csv
def get_data():
    data=[]
    data_file = open("testdata.csv")
    reader = csv.reader(data_file)

    for row in reader:
        data.append(tuple(row))

    return data


@pytest.mark.parametrize("username,password",get_data())
def test_data_check(username,password):
    print(username+" "+password)
