"""
Pytest : PyTest is a Python testing framework used to write simple and scalable test cases.
        -> File name should start or End with "test_" name
        -> class and Function should also start or end with "test_"
        -> Syntax --> def test_add():

pytest -vs full form (meaning):
        -v → Verbose
            -> Shows detailed output (each test name + result)
        -s → Show output (no capture)
            -> Displays print() statements in console
"""
########################################################################################################################
##basic
## function
def login():
    print("Logging in...")

## CLass
class Demo:
    def login(self):
        print("Logging in...")
        assert 2+4 == 6
    def logout(self):
        print("Logging out...")
        assert 2+4 == 7

obj = Demo()
obj.login()
obj.logout()