file_data = []
file2_data = []
with open("file1.txt") as file:
    for i in file:
        file_data.append(int(i.strip()))

with open("file2.txt") as file:
    for i in file:
        file2_data.append(int(i.strip()))

result = [number for number in file_data if number in file2_data]

print(result)
