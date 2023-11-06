import json

# Open the JSON file and load its contents
with open("data.json", "r") as file:
    data = json.load(file)

# print(data)
# Flatten the nested list structure

# Create a list of items in the flattened data that are equal to "ebay"
data_list = [website_name for website_name in data if website_name == "ebay"]
print(str(data_list)[1:-1])

print(data[data_list[0]]["email"])
print(data[data_list[0]]["password"])
print(data["ebay"])
