import pytest


def get_test_data():
    user_data_list = [('Admin','admin123'),('Tom','welcome123')]
    return user_data_list

@pytest.mark.parametrize('username,password',get_test_data())
def test_param(username,password):
    print(username)
    print(password)
