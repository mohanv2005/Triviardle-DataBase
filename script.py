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


def create_category():
    """Create a new category folder."""

    while True:
        category = input("\nEnter new category name: ").strip()

        if not category:
            print("Category cannot be empty.")
            continue

        category_path = BASE_DIR / category

        if category_path.exists():
            print("That category already exists.")
            return category, category_path

        category_path.mkdir(parents=True)

        print(f"Created category: {category}")

        return category, category_path


def create_subcategory(category_path):
    """Create a new sub-category folder."""

    while True:
        subcategory = input("\nEnter new sub-category name: ").strip()

        if not subcategory:
            print("Sub-category cannot be empty.")
            continue

        subcategory_path = category_path / subcategory

        if subcategory_path.exists():
            print("That sub-category already exists.")
            return subcategory, subcategory_path

        subcategory_path.mkdir(parents=True)

        print(f"Created sub-category: {subcategory}")

        return subcategory, subcategory_path


# ==================================================
# 1. FIND EXISTING CATEGORIES
# ==================================================

categories = sorted([
    folder.name
    for folder in BASE_DIR.iterdir()
    if folder.is_dir()
    and not folder.name.startswith(".")
])


# ==================================================
# 2. SELECT OR CREATE CATEGORY
# ==================================================

category_options = categories + ["Create New Category"]

category_choice = choose_from_list(
    category_options,
    "SELECT CATEGORY"
)


# --------------------------------------------------
# Create new category
# --------------------------------------------------

if category_choice == "Create New Category":

    category, category_path = create_category()

else:

    category = category_choice
    category_path = BASE_DIR / category


# ==================================================
# 3. FIND SUB-CATEGORIES
# ==================================================

subfolders = sorted([
    folder
    for folder in category_path.iterdir()
    if folder.is_dir()
    and not folder.name.startswith(".")
])


# ==================================================
# 4. SELECT / CREATE / SKIP SUB-CATEGORY
# ==================================================

if subfolders:

    subcategory_options = [
        folder.name
        for folder in subfolders
    ]

    # Allow questions without a sub-category
    subcategory_options.append("No Sub-Category")

    # Allow creating a new sub-category
    subcategory_options.append("Create New Sub-Category")

    subcategory_choice = choose_from_list(
        subcategory_options,
        "SELECT SUB-CATEGORY"
    )

    # --------------------------------------------------
    # No sub-category
    # --------------------------------------------------

    if subcategory_choice == "No Sub-Category":

        subcategory = None

        json_path = category_path / f"{category}.json"


    # --------------------------------------------------
    # Create new sub-category
    # --------------------------------------------------

    elif subcategory_choice == "Create New Sub-Category":

        subcategory, subcategory_path = create_subcategory(
            category_path
        )

        json_path = subcategory_path / f"{subcategory}.json"


    # --------------------------------------------------
    # Existing sub-category
    # --------------------------------------------------

    else:

        subcategory = subcategory_choice

        subcategory_path = category_path / subcategory

        json_files = sorted([
            file
            for file in subcategory_path.iterdir()
            if file.is_file()
            and file.suffix.lower() == ".json"
        ])

        if json_files:
            json_path = json_files[0]

        else:
            json_path = (
                subcategory_path /
                f"{subcategory}.json"
            )


# ==================================================
# CATEGORY HAS NO SUB-CATEGORIES
# ==================================================

else:

    print("\nNo existing sub-categories found.")

    subcategory_options = [
        "No Sub-Category",
        "Create New Sub-Category"
    ]

    subcategory_choice = choose_from_list(
        subcategory_options,
        "SUB-CATEGORY"
    )

    # --------------------------------------------------
    # No sub-category
    # --------------------------------------------------

    if subcategory_choice == "No Sub-Category":

        subcategory = None

        json_path = category_path / f"{category}.json"


    # --------------------------------------------------
    # Create sub-category
    # --------------------------------------------------

    else:

        subcategory, subcategory_path = create_subcategory(
            category_path
        )

        json_path = subcategory_path / f"{subcategory}.json"


# ==================================================
# 5. LOAD EXISTING JSON
# ==================================================

if json_path.exists():

    try:

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    except json.JSONDecodeError:

        print(
            "\nWarning: JSON file is empty or invalid."
        )

        data = []

else:

    data = []


# Make sure data is a list
if isinstance(data, dict):
    data = [data]


# ==================================================
# 6. GENERATE NEXT ID
# ==================================================

if data:

    next_id = max(
        item.get("id", 0)
        for item in data
        if isinstance(item, dict)
    ) + 1

else:

    next_id = 1


# ==================================================
# 7. GET QUESTION INFORMATION
# ==================================================

print("\n================================")
print("       ENTER QUESTION DATA")
print("================================")

answer = input("\nAnswer: ").strip()

while not answer:
    print("Answer cannot be empty.")
    answer = input("Answer: ").strip()


questions = []

for level in range(1, 6):

    while True:

        text = input(
            f"Level {level}: "
        ).strip()

        if text:
            break

        print("Question cannot be empty.")

    questions.append({
        "level": level,
        "text": text
    })


# ==================================================
# 8. CREATE NEW ENTRY
# ==================================================

new_entry = {
    "id": next_id,
    "category": category,
    "sub-category": subcategory,
    "answer": answer,
    "questions": questions
}


# ==================================================
# 9. APPEND NEW ENTRY
# ==================================================

data.append(new_entry)


# ==================================================
# 10. SAVE JSON
# ==================================================

with open(
    json_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        indent=4,
        ensure_ascii=False
    )


# ==================================================
# 11. CONFIRMATION
# ==================================================

print("\n================================")
print("     QUESTION ADDED SUCCESSFULLY")
print("================================")

print(f"ID           : {next_id}")
print(f"Category     : {category}")
print(f"Sub-Category : {subcategory}")
print(f"Answer       : {answer}")
print(f"File         : {json_path}")