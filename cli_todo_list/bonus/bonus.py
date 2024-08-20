# contents = ["text string 1", "text string 2", "text string 3"]
# file_names = ["doc.txt", "report.txt", "presentation.txt"]
#
# for content, file_name in zip(contents, file_names):
#     with open(f"files/{file_name}", "w") as text_file:
#         text_file.write(content)

# file_names = ["1. doc", "1. report", "1. presentation"]
# print(file_names)
#
# file_names = [filename.replace(". ", " - ") + ".txt" for filename in file_names]
# print(file_names)
#
# new = [i for i in ['a', 'b', 'c']]
# print(new)

# numbers = [10.1, 12.3, 14.7]
# numbers = [int(item) for item in numbers]
# print(numbers)

# # Getting user input
# date = input("Enter today's date: ")
# mood = input("Enter mood today on a scale of 1 - 10: ")
# thoughts = input("Let your thoughts flow:\n")
#
# # Manually construct the path to the Journal directory
# journal_dir = '../journal'
# file_name = f"{date}.txt"
# file_path = f"{journal_dir}/{file_name}"
#
# # Write to the file inside the Journal directory
# with open(file_path, "w") as file:
#     file.write(mood + '\n')
#     file.write(thoughts)

# password = input("Enter your password: ")
# result = {}
#
# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
# result["digits"] = digit
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
# result["upper_case"] = uppercase
#
# # print(result)
# # print(result.values())
#
# if all(result.values()):
#     print("Password is strong")
# else:
#     print("Password is weak")

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")





