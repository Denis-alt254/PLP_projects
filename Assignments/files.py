def modify_file_content(content):
    # Example modification: Convert content to uppercase
    return content.upper()

def main():
    try:
        # Ask the user for the filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Open the file in read mode
        with open("./Week4/example.txt, 'r'") as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Write the modified content to a new file
        output_filename = "modified_" + "./Week4/example.txt"
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")

if __name__ == "__main__":
    main()