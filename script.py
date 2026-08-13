import json

FILE_NAME = "Movies/Marvel/Marvel.json"

# Read existing JSON
with open(FILE_NAME, "r", encoding="utf-8") as file:
    data = json.load(file)

# Make sure data is a list
if not isinstance(data, list):
    data = [data]

# Generate next ID automatically
next_id = max(item["id"] for item in data) + 1 if data else 1

# Get user input
category = input("Enter Category: ")
subcategory = input("Enter Sub-Category: ")
answer = input("Enter Answer: ")

questions = []

for level in range(1, 6):
    text = input(f"Enter clue for Level {level}: ")

    questions.append({
        "level": level,
        "text": text
    })

# Create new entry
new_entry = {
    "id": next_id,
    "category": category,
    "sub-category": subcategory,
    "answer": answer,
    "questions": questions
}

# Append
data.append(new_entry)

# Save
with open(FILE_NAME, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"\nSuccessfully added entry with ID {next_id}!")