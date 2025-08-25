# ============================================
# File Handling and Exception Handling Assignment
# ============================================

# Task 1: File Read & Write Challenge
def file_read_write():
    # Read from an existing file and write modified version
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Example modification: change text to uppercase
        modified_content = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File read and modified version written to 'output.txt'")

    except Exception as e:
        print(f"❌ An error occurred: {e}")


# Task 2: Error Handling Lab
def error_handling_lab():
    filename = input("Enter the filename you want to open: ")

    try:
        with open(filename, "r") as file:
            print("✅ File opened successfully. Content:")
            print(file.read())
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


# Run both tasks
if __name__ == "__main__":
    print("📂 Running File Handling and Exception Handling Assignment...\n")

    # Task 1
    file_read_write()

    # Task 2
    error_handling_lab()
