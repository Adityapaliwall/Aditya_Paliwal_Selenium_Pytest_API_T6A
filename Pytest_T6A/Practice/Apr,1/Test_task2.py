import pytest


class Test_Demo:
    @pytest.mark.smoke
    def test_login(self):
        print("Logging in...")
        assert 'hello' == 'hello'
        assert 'world' == 'world'

    @pytest.mark.smoke
    def test_logout(self):
        print("Logging out...")
        ls = [1,2,3,4,5]
        2 in ls
        print( 2 in ls)

    @pytest.mark.regression
    def test_register(self):
        print("Logging in...")
        ls = [1, 2, 3, 4, 5]
        assert (2 in ls) == True

    @pytest.mark.regression
    def test_addf(self):
        print("Logging in...")
        ls = [1, 2, 3, 4, 5]
        assert (2 in ls) == True
