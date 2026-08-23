# CONTRIBUTING

You can contribute to the project in the following ways.

## Adding Questions

The easiest way to contribute is by adding new questions to the trivia question database.

A helper script, `script.py`, is provided to make this process easier. It automatically creates the required category/sub-category structure, loads existing questions, generates the next available question ID, and saves the new question in the correct JSON file.

### 1. Prerequisites

Make sure you have:

- Python 3 installed.

### 2. Run the Question Script

Run:

```bash
python script.py
```

On systems where Python 3 is invoked as `python3`:

```bash
python3 script.py
```

The script will guide you through the entire process interactively.

### 3. Select a Category

The script first displays all existing categories.

For example:

```text
===== SELECT CATEGORY =====
1. Anime
2. Movies
3. VideoGames
4. Create New Category

Enter choice:
```

Select an existing category by entering its number.

If the category you need does not exist, select **Create New Category** and enter the new category name.

For example:

```text
Enter new category name: Science
Created category: Science
```

Category names should be clear and consistent with the existing project structure.

### 4. Select or Create a Sub-Category

After selecting a category, the script displays its existing sub-categories.

For example:

```text
===== SELECT CATEGORY =====
1. Anime
2. Movies
3. VideoGames
4. Create New Category

Enter choice: 2

===== SELECT SUB-CATEGORY =====
1. Marvel
2. No Sub-Category
3. Create New Sub-Category
```

You can:

- Select an existing sub-category.
- Choose **No Sub-Category** if the question belongs directly to the category.
- Create a new sub-category.

If you create a new sub-category, the script automatically creates the required directory.

### 5. Enter the Answer

The script then asks for the answer:

```text
================================
       ENTER QUESTION DATA
================================

Answer:
```

Enter the correct answer to the question.

The answer cannot be empty.

Try to keep answers concise and unambiguous.

For example:

```text
Answer: Iron Man 1
```

### 6. Enter the Five Questions

Each trivia entry contains **five questions**, one for each difficulty level from 1 to 5.

The script will prompt you with:

```text
Level 1:
Level 2:
Level 3:
Level 4:
Level 5:
```

Enter one question for each level.

For example:

```text
Level 1: Initially Nicolas Cage and Tom Cruise both showed interest in playing the character in this movie.
Level 2: In this movie the main lead is kidnapped while traveling to Afghanistan.
Level 3: In this movie the main character suffers a heart injury from shrapnel.
Level 4: The director also played the protagonist's chauffeur/bodyguard.
Level 5: This movie gave birth to the Marvel Cinematic Universe.
```

Every level must contain a question. Empty questions will be rejected.

### 7. Question Difficulty

The five levels should represent increasing difficulty.

A good general guideline is:

| Level | Difficulty | Description                                       |
| ----- | ---------- | ------------------------------------------------- |
| 1     | Easy       | Common knowledge or basic facts                   |
| 2     | Moderate   | Requires some familiarity with the topic          |
| 3     | Medium     | Requires specific knowledge                       |
| 4     | Hard       | Less commonly known information                   |
| 5     | Very Hard  | Specialist, obscure, or highly specific knowledge |

Avoid making all five questions approximately the same difficulty.

The progression should feel meaningful to the player.

### 8. Review Your Contribution

After adding the question, the script displays a confirmation similar to:

```text
================================
     QUESTION ADDED SUCCESSFULLY
================================

ID           : 12
Category     : Science
Sub-Category : Physics
Answer       : Albert Einstein
File         : Science/Physics/Physics.json
```

Before committing your changes, open the modified JSON file and verify that:

- The answer is correct.
- All five questions are present.
- The difficulty increases from Level 1 to Level 5.
- The questions are grammatically correct.
- The questions are factually accurate.
- The generated structure matches the existing data.
- No unrelated files were modified.

## Question-Writing Guidelines

Good trivia questions should be:

- Clear
- Factually correct
- Specific
- Answerable
- Relevant to the selected category
- Appropriately difficult
- Free from unnecessary ambiguity

### Avoid Questions Like

```text
What is a famous country?
```

This has no single clear answer.

Instead, use:

```text
Which country has Tokyo as its capital?
```

Similarly, avoid questions where multiple answers could reasonably be considered correct.

### Avoid Giving Away the Answer

Do not include the answer directly in the question.

Bad:

```text
Which scientist developed the theory of relativity, Albert Einstein?
```

Good:

```text
Which scientist developed the theory of relativity?
```

### Verify Facts

Trivia questions should be based on reliable information.

For historical, scientific, geographical, or other factual questions, verify the answer before submitting the contribution.

If a fact is disputed or has multiple commonly accepted answers, rewrite the question to make the intended answer unambiguous.

---

Thank you for contributing questions and helping expand the trivia database!
