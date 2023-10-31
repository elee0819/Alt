# file_operations.py

import os

class FileOperations:
    def __init__(self):
        # Initialize file operations settings and configurations
        # Add any additional initialization logic here if needed
        pass

    def create_file(self, file_name):
        try:
            # Create a new file with the given name
            with open(file_name, "w") as new_file:
                print(f"AI Assistant: Created a new file '{file_name}'.")
        except Exception as e:
            print(f"AI Assistant: Error - {str(e)}")

    def read_file(self, file_name):
        try:
            # Read the contents of a file
            with open(file_name, "r") as file:
                contents = file.read()
                print(f"AI Assistant: Contents of '{file_name}':\n{contents}")
        except FileNotFoundError:
            print(f"AI Assistant: Error - File '{file_name}' not found.")
        except Exception as e:
            print(f"AI Assistant: Error - {str(e)}")

    def delete_file(self, file_name):
        try:
            # Delete a file
            os.remove(file_name)
            print(f"AI Assistant: Deleted file '{file_name}'.")
        except FileNotFoundError:
            print(f"AI Assistant: Error - File '{file_name}' not found.")
        except Exception as e:
            print(f"AI Assistant: Error - {str(e)}")

if __name__ == "__main__":
    file_operations = FileOperations()

    print("AI Assistant: Welcome to the file operations module!")
    while True:
        print("Options:")
        print("1. Create a new file")
        print("2. Read a file")
        print("3. Delete a file")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            file_name = input("Enter the name of the new file: ")
            file_operations.create_file(file_name)
        elif choice == "2":
            file_name = input("Enter the name of the file to read: ")
            file_operations.read_file(file_name)
        elif choice == "3":
            file_name = input("Enter the name of the file to delete: ")
            file_operations.delete_file(file_name)
        elif choice == "4":
            print("AI Assistant: Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
