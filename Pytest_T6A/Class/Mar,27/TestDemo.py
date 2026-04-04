"""
Pytest : PyTest is a Python testing framework used to write simple and scalable test cases.
        -> File name should start or End with "test_" name
        -> Function and Method should also start with "test_"
        -> Class name should start with Test_
        -> Syntax --> def test_add():
        -> when we follow this rule
        ->pytest will automatically recognise the file function and class following the rules
            so without giving function call we can execute the test function
            and without crating an object wwe can make the test CLass

pytest -vs full form (meaning):
        -v → Verbose
            -> Shows detailed output (each test name + result)
        -s → Show output (no capture)
            -> Displays print() statements in console

-> Pytest cannot recognize the function that are not following the rules
-> In pytest We can not give or use or make a constructor

-> For Pytest this is not necessary to make object for calling a FUNCTION
"""
## function
# def test_login():
#     print("Logging in...")
# def test_logout():
#     print("Logging out...")
# def test_register():
#     print("Registering...")
#
# test_login()
# test_logout()
# test_register()

## CLass
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

    def test_register(self):
        print("Logging in...")
        ls = [1, 2, 3, 4, 5]
        assert (2 in ls) == True


# obj = Test_Demo()
# obj.test_login()
# obj.test_logout()