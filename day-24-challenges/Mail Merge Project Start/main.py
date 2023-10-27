
name_list = []
with open("Input\/Names\invited_names.txt", 'r') as file:
    for f in file.readlines():
        print(f.strip())
        name_list.append(f.strip())

content = ""
with open("Input\/Letters\starting_letter.txt", 'r') as rfile:
    content=rfile.read()

for name in name_list:
    with open(f"Output\ReadyToSend\{name}.txt",'a') as file_name:
        file_name.write(content.replace("[name]", name.strip()))

