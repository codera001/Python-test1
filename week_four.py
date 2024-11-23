def read_and_modify_file():
    # Prompt the user for the input filename
    input_file = input("Enter the filename to read: ")

    try:
        # Attempt to open the input file
        with open(input_file, "r") as file:
            content = file.read()  # Read the entire content
            print("File read successfully!")

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Prompt the user for the output filename
        output_file = input("Enter the filename to save the modified content: ")

        # Write the modified content to the output file
        with open(output_file, "w") as file:
            file.write(modified_content)
            print("Modified content written to '{}'".format( output_file))

    except FileNotFoundError:
        print("Error: The file '{}' does not exist. Please check the filename." .format(input_file))
    except IOError:
        print("Error: Could not read from or write to file. Check your file permissions.")
    except Exception as e:
        print("An unexpected error occurred: {}". format(e))

# Run the program
read_and_modify_file()
