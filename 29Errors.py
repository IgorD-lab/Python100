# ------------------------------------------ Catching errors ------------------------------------------------
# try - something might cause exception
# except - do if exception was caused (as) keyword can be used to print the thrown error message
# else - do this if there were no exceptions
# finally - do no matter what happens usually to clean stuff up at the end of code execution
# raise - throw your own error
try:
    file = open("no_file.txt")
    no_dictionary = {"key": "value"}
    print(no_dictionary["no_key"])
except FileNotFoundError:
    file = open("no_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"Key {error_message} doesnt exist in dictionary")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

    # good to know use - here it will skip invalid values without breaking the loop
    values = [1, 2, 3, 4, "44"]
    total_value = 0
    try:
        for v in values:
            total_value += v
    except KeyError:
        pass

raise TypeError("This TypeError is caused by me!")

# I've got to figure out what to make with this stuff errors tend to be a utility only thing ¯\_(ツ)_/¯
