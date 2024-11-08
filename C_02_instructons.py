# function go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions",  "-")

    print('''
Instructions go here
- instructions 1
- instructions 2
- etc
    ''')


# Main Routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

    print("Program continues")
