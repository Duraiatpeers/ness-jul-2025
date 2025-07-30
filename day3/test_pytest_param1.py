import pytest



@pytest.mark.parametrize('username',[('Sam'),('Tom')])
def test_param(username):
    print(username)
    assert username == 'Sam'

