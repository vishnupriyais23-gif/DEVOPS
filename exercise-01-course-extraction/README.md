# Exercise 1: Course Name Extraction Using Fine-Tuned BERT and Docker

## Objective
Fine-tune a pretrained DistilBERT token-classification model to extract course names from text, expose predictions through FastAPI, and run the application using Docker.

## Technologies
- Python
- PyTorch
- Hugging Face Transformers
- FastAPI and Uvicorn
- Docker
- Git and GitHub

## Project Structure
- `train.py` - creates training examples and fine-tunes the model.
- `app.py` - provides the course-name extraction API.
- `requirements.txt` - lists Python dependencies.
- `Dockerfile` - defines the Docker image.
- `saved_model/` - contains the trained model and tokenizer.
- `screenshots/` - stores project execution screenshots.

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/vishnupriyais23-gif/DEVOPS.git
cd DEVOPS/exercise-01-course-extraction
```

Install Python dependencies:

```bash
py -m pip install -r requirements.txt
```

## Train the Model

Run:

```bash
py train.py
```

The training script fine-tunes DistilBERT and saves the model and tokenizer to `saved_model/`.

Training is required before running the API or building the Docker image if the trained model has not been obtained separately.

## Run the API Locally

```bash
py -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

Use `POST /extract-course-name/` with this example request:

```json
{
  "text": "I want to study Machine Learning and Computer Networks."
}
```

The response contains an `extracted_course_names` array.

## Build and Run with Docker

Train the model first, so that `saved_model/` exists. Then build the image:

```bash
docker build -t course-extraction-api .
```

Run the container:

```bash
docker run -d --name course-api -p 8000:8000 course-extraction-api
```

Open the API documentation:

http://127.0.0.1:8000/docs

Check the container:

```bash
docker ps
docker logs course-api
```

Stop and remove the container when finished:

```bash
docker stop course-api
docker rm course-api
```

## Model Storage

The `saved_model/` directory is excluded from Git because the model weights are large. A fresh clone must train the model or obtain the saved model separately before running the API or building the Docker image.

## Workflow
1. Generate course-name training examples.
2. Fine-tune the pretrained model.
3. Save the model and tokenizer.
4. Expose predictions through FastAPI.
5. Test the API locally.
6. Build and run the Docker container.
7. Test the API inside Docker.

## Limitations
This is an educational demonstration using synthetic training examples. A low training loss does not establish generalization or real-world accuracy. Evaluation on separate, representative test data is needed before making performance claims.
