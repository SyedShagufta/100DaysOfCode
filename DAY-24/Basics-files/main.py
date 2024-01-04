# This is one method of opening the file, reading it and closing it
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Some of us might forget to close it so here's a better way of doing it
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew Line text.")


