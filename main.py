# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import keyword
test = ["else", "integer", "except", "elif"]
keyword_test = []
for item in test:
    if keyword.iskeyword(item):
        keyword_test.append(True)
    else:
        keyword_test.append(False)

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)