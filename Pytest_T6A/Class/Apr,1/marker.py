"""
Markers:Markers in pytest are tags/labels used to:
                - Group tests
                - Run specific tests
                - Skip tests
                - Mark slow or important tests

        --> Markers help you control which tests to run

"""
import pytest


class Test_Demo:
    def test_login(self):
        print("Logging in...")
        assert 'hello' == 'hello'
        assert 'world' == 'world'

    def test_logout(self):
        print("Logging out...")
        ls = [1,2,3,4,5]
        2 in ls
        print( 2 in ls)
    @pytest.mark.regre
    def test_register(self):
        print("Logging in...")
        ls = [1, 2, 3, 4, 5]
        assert (2 in ls) == True