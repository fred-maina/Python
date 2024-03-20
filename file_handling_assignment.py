def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Another line with some numbers: 3.14, 42\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Permission denied. Unable to create the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation process completed.")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading process completed.")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("\nThis is an appended line.\n")
            file.write("Another appended line.\n")
            file.write("1234567890\n")
        print("Content appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Permission denied. Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending process completed.")


create_file()
read_file()
append_to_file()
