def append_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)

if __name__ == "__main__":
    # read user input and store it in a file
    # ask the user for more input until they're done

    while True:
        user_input = input("Enter your text: ")
        append_file('input.txt', user_input)
        
        if user_input == "":
            break

    print("File written successfully")
