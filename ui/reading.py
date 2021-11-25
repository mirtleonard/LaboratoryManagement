import time

def invalid(message = "Invalid input!"):
    print(message)
    time.sleep(1)

def read_input(message, integer = False, string = False):
    while True:
        processed = input(message)
        try:
            if integer:
                processed = int(processed)
            elif string and processed == "":
                raise Exception()
            return processed
        except:
            invalid()
