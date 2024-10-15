# Generates headings (eg: ---- heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here. 
- Type the file type that you want to assess.
- Types of files are: Image, Integer, and Text. 
- (For image)type the Width and Height to find out the number of bits in the image.
- If you want to exit the program type "xxx".   
    ''')


# asks users for file type (integer / image / text / xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image...
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text...
        elif response in ["text", 'txt', 't']:
            return "text"

        # if the response is invalid output an error
        else:
            print("Sorry, please choose integer, text or image")


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()


# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
while True:
    to_factor = num_check("To factors: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
