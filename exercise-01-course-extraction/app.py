
import re
import torch
from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, AutoModelForTokenClassification

MODEL_DIR = "saved_model"

app = FastAPI(title="Course Name Extraction API")

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForTokenClassification.from_pretrained(MODEL_DIR)
model.eval()


class CourseRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)


@app.get("/")
def home():
    return {
        "message": "Course Name Extraction API is running",
        "docs": "/docs",
    }


@app.post("/extract-course-name/")
def extract_course_name(request: CourseRequest):
    inputs = tokenizer(
        request.text,
        return_tensors="pt",
        truncation=True,
        max_length=256,
        return_offsets_mapping=True,
    )

    offsets = inputs.pop("offset_mapping")[0].tolist()

    with torch.no_grad():
        outputs = model(**inputs)

    predictions = outputs.logits.argmax(dim=-1)[0].tolist()

    extracted = []
    current_start = None
    current_end = None

    for (start, end), label_id in zip(offsets, predictions):
        if start == end:
            continue

        label = model.config.id2label[label_id]

        if label == "B-COURSE":
            if current_start is not None:
                extracted.append(
                    request.text[current_start:current_end]
                )
            current_start, current_end = start, end

        elif label == "I-COURSE" and current_start is not None:
            current_end = end

        elif current_start is not None:
            extracted.append(request.text[current_start:current_end])
            current_start = None
            current_end = None

    if current_start is not None:
        extracted.append(request.text[current_start:current_end])

    # Remove duplicate predictions while preserving order.
    extracted = list(dict.fromkeys(
        name.strip(" .,!?;:") for name in extracted if name.strip(" .,!?;:")
    ))

    return {"extracted_course_names": extracted}
