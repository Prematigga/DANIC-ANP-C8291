# 10. Write a function convert_to_float that takes a list of strings and attempts
# to convert each string to a float. Use exception handling to manage:
#
# Value errors (e.g., strings that cannot be converted to float).
#
# Any other unexpected errors.
#
# The function should return a list of successfully converted floats and a list of
# errors (with the original string and the error message).
list = ['12','322','444','4545','avd','fsdf4','dfds']
def convert_to_float(list):
    i = None

    for i,string in enumerate(list):
        try:
            list[i] = float(string)

        except ValueError:
            list[i] = f'{list[i]}:ValueError'
        except Exception as e:
            list[i] = f'{list[i]}:{e}'
    print(list)
convert_to_float(list)