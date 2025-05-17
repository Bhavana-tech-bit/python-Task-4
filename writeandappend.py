def write_and_append_file():
    
    try:
        initial_content = input("Enter text to write to the file: ")
        with open("output.txt", "w") as file:
            file.write(initial_content + '\n')
        print("Data successfully written to output.txt.")
        additional_content = input("Enter additional text to append: ")

        with open("output.txt", "a") as file:
            file.write(additional_content + '\n')
        print("Data successfully appended.")

        with open("output.txt", "r") as file:
            final_content = file.read()
        print("Final content of output.txt:")
        print(final_content)

    except Exception as e:
         print(f"An error occurred: {e}")
write_and_append_file()
