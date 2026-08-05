
## JSON Structure


| Field | Type | Description |
|-------|------|-------------|
| `id` | Number | Unique identifier for the quiz. |
| `category` | String | Main category of the quiz. |
| `sub-category` | String | Optional sub-category. |
| `answer` | String | The correct answer. |
| `questions` | Array | List of clues ordered by difficulty. |

### Question Object


| Field | Type | Description |
|-------|------|-------------|
| `level` | Number | Difficulty level (1 = hardest, 5 = easiest). |
| `points` | Number | Points awarded for answering at this level. |
| `text` | String | The clue shown to the player. |

## Sample Data

```json
{
  "id": 1,
  "category": "Movies",
  "sub-category": "Marvel",
  "answer": "Iron Man 1",
  "questions": [
    {
      "level": 1,
      "points": 50,
      "text": "Initially Nicolas Cage and Tom Cruise both showed interest in playing the character in this movie."
    },
    {
      "level": 2,
      "points": 40,
      "text": "In this movie the main lead is kidnapped while traveling to Afghanistan."
    },
    {
      "level": 3,
      "points": 30,
      "text": "In this movie the main character suffers a heart injury from shrapnel."
    },
    {
      "level": 4,
      "points": 20,
      "text": "The director also played the protagonist's chauffeur/bodyguard."
    },
    {
      "level": 5,
      "points": 10,
      "text": "This movie gave birth to the Marvel Cinematic Universe."
    }
  ]
}
```

