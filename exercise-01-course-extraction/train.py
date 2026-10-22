
import os
import re
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForTokenClassification

MODEL_NAME = "distilbert/distilbert-base-uncased"
OUTPUT_DIR = "saved_model"

COURSES = [
    "Computer Science",
    "Artificial Intelligence",
    "Machine Learning",
    "Data Structures and Algorithms",
    "Operating Systems",
    "Database Management Systems",
    "Computer Networks",
    "Software Engineering",
    "Cloud Computing",
    "Cyber Security",
    "Advanced Mathematics",
    "Digital Electronics",
    "Information Science",
    "Web Development",
    "Data Analytics",
]

# Each example contains text and the exact course name to extract.
TEMPLATES = [
    "The college offers {}.",
    "I want to study {}.",
    "My favourite course is {}.",
    "Please provide details about {}.",
    "The department teaches {} this semester.",
    "Is {} available at this college?",
    "I am interested in learning {}.",
    "The syllabus includes {} and other subjects.",
]

LABEL2ID = {"O": 0, "B-COURSE": 1, "I-COURSE": 2}
ID2LABEL = {v: k for k, v in LABEL2ID.items()}


def create_examples():
    examples = []
    for course in COURSES:
        for template in TEMPLATES:
            text = template.format(course)
            start = text.index(course)
            end = start + len(course)
            examples.append((text, start, end))
    return examples


class CourseDataset(Dataset):
    def __init__(self, examples, tokenizer):
        self.items = []

        for text, start, end in examples:
            encoded = tokenizer(
                text,
                truncation=True,
                max_length=96,
                padding="max_length",
                return_offsets_mapping=True,
            )

            labels = []
            started = False

            for token_start, token_end in encoded["offset_mapping"]:
                if token_start == token_end:
                    labels.append(-100)
                elif token_start >= start and token_end <= end:
                    labels.append(
                        LABEL2ID["B-COURSE"]
                        if not started
                        else LABEL2ID["I-COURSE"]
                    )
                    started = True
                else:
                    labels.append(LABEL2ID["O"])

            self.items.append({
                "input_ids": torch.tensor(encoded["input_ids"]),
                "attention_mask": torch.tensor(encoded["attention_mask"]),
                "labels": torch.tensor(labels),
            })

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


def main():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForTokenClassification.from_pretrained(
        MODEL_NAME,
        num_labels=3,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
    )

    dataset = CourseDataset(create_examples(), tokenizer)
    loader = DataLoader(dataset, batch_size=4, shuffle=True)

    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
    model.train()

    epochs = 3

    for epoch in range(epochs):
        total_loss = 0.0

        for batch in loader:
            optimizer.zero_grad()

            outputs = model(**batch)
            loss = outputs.loss
            loss.backward()

            optimizer.step()
            total_loss += loss.item()

        average_loss = total_loss / len(loader)
        print(
            f"Epoch {epoch + 1}/{epochs} "
            f"- Average loss: {average_loss:.4f}"
        )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    print(f"\nModel and tokenizer saved in ./{OUTPUT_DIR}")


if __name__ == "__main__":
    main()

