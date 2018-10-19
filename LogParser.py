from pathlib import Path

# Prompt user to enter a filename
filename = input("Please enter file name (without .txt extension): ")
file_path = Path("logs/" + filename + ".txt")

# Read file contents into contents
file_stream = open(file_path, "r")

if file_stream.mode == "r":
    contents = file_stream.readlines()
    file_stream.close()

for i in contents:
    print(i.split(':'))