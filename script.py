import json
from pathlib import Path


# Root directory where this script is located
BASE_DIR = Path(__file__).parent


def choose_from_list(options, title):
    """Display options and let the user choose one."""

    print(f"\n===== {title} =====")

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("\nEnter choice: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a number.")


# --------------------------------------------------
# 1. Find categories
# --------------------------------------------------

categories = [
    folder.name
    for folder in BASE_DIR.iterdir()
    if folder.is_dir() and not folder.name.startswith(".")
]

if not categories:
    print("No categories found.")
    exit()


# --------------------------------------------------
# 2. Choose category
# --------------------------------------------------

category = choose_from_list(
    categories,
    "SELECT CATEGORY"
)

category_path = BASE_DIR / category


# --------------------------------------------------
# 3. Find sub-categories / JSON files
# --------------------------------------------------

subfolders = [
    folder
    for folder in category_path.iterdir()
    if folder.is_dir()
]

json_files = [
    file
    for file in category_path.iterdir()
    if file.suffix.lower() == ".json"
]


# --------------------------------------------------
# 4. Choose sub-category
# --------------------------------------------------

if subfolders:

    subcategory_names = [
        folder.name
        for folder in subfolders
    ]

    subcategory = choose_from_list(
        subcategory_names,
        "SELECT SUB-CATEGORY"
    )

    subcategory_path = category_path / subcategory

    # Look for JSON file inside sub-category
    json_files = [
        file
        for file in subcategory_path.iterdir()
        if file.suffix.lower() == ".json"
    ]

    if json_files:
        json_path = json_files[0]
    else:
        # Create JSON file using sub-category name
        json_path = subcategory_path / f"{subcategory}.json"

else:

    # Category has no sub-category
    subcategory = None

    if json_files:
        json_path = json_files[0]
    else:
        # Create JSON using category name
        json_path = category_path / f"{category}.json"


# --------------------------------------------------
# 5. Load existing JSON
# --------------------------------------------------

if json_path.exists():

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError:
        print("JSON file is empty or invalid. Starting a new database.")
        data = []

else:
    data = []


# Make sure data is a list
if isinstance(data, dict):
    data = [data]


# --------------------------------------------------
# 6. Generate ID automatically
# --------------------------------------------------

if data:
    next_id = max(
        item.get("id", 0)
        for item in data
    ) + 1
else:
    next_id = 1


# --------------------------------------------------
# 7. Get question information
# --------------------------------------------------

print("\n===== ENTER QUESTION DATA =====")

answer = input("Answer: ")

questions = []

for level in range(1, 6):

    while True:
        text = input(f"Level {level}: ").strip()

        if text:
            break

        print("Question cannot be empty.")

    questions.append({
        "level": level,
        "text": text
    })


# --------------------------------------------------
# 8. Create new entry
# --------------------------------------------------

new_entry = {
    "id": next_id,
    "category": category,
    "sub-category": subcategory,
    "answer": answer,
    "questions": questions
}


# --------------------------------------------------
# 9. Append to database
# --------------------------------------------------

data.append(new_entry)


# --------------------------------------------------
# 10. Save JSON
# --------------------------------------------------

with open(json_path, "w", encoding="utf-8") as file:
    json.dump(
        data,
        file,
        indent=4,
        ensure_ascii=False
    )


# --------------------------------------------------
# 11. Confirmation
# --------------------------------------------------

print("\n================================")
print("Question added successfully!")
print("================================")
print(f"Category     : {category}")
print(f"Sub-Category : {subcategory}")
print(f"Answer       : {answer}")
print(f"ID           : {next_id}")
print(f"File         : {json_path}")