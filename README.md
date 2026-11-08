# Django Generative AI Summarizer & Horoscope Generator

A Generative AI application developed using Python, Django REST Framework, and OpenAI API. The application provides REST APIs for text summarization and personalized horoscope generation using custom prompts.

## Features

### 1. AI Text Summarization
- Accepts user-provided text through a POST request.
- Uses the OpenAI API to generate a concise summary.
- Generates summaries of up to 100 words.
- Preserves the main ideas of the original text.
- Returns the generated summary in JSON format.

### 2. AI Horoscope Generation
- Accepts user details such as name, star, birthdate, birth time, and gender.
- Uses the OpenAI API to generate a personalized horoscope.
- Covers marriage, career, health, finance, and love life.
- Generates responses of up to 200 words.
- Returns the horoscope in JSON format.

## Technologies Used

- Python
- Django
- Django REST Framework
- OpenAI API
- Generative AI
- SQLite
- python-dotenv
- Postman

## Project Structure

```text
django-generative-ai-summarizer-horoscope/
│
├── genai_project/
├── llm_api/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

1. Clone the repository.

2. Create and activate a Python virtual environment.

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### 1. Text Summarization

**Endpoint:**

`POST /api/summarize/`

**Request Body:**

```json
{
    "userquery": "Enter the text you want to summarize here."
}
```

**Sample Response:**

```json
{
    "summary": "Generated summary of the provided text."
}
```

### 2. Horoscope Generation

**Endpoint:**

`POST /api/horoscope/`

**Request Body:**

```json
{
    "Name": "John",
    "Star": "Ashwini",
    "birthdate": "2000-01-15",
    "time": "10:30 AM",
    "gender": "Male"
}
```

**Sample Response:**

```json
{
    "horoscope": "AI-generated horoscope based on the provided details."
}
```

## API Testing

The REST API endpoints can be tested using Postman by sending POST requests with JSON request bodies.

## How It Works

1. The user sends input through a REST API request.
2. Django REST Framework receives and validates the request.
3. A custom prompt is created based on the requested functionality.
4. The OpenAI API processes the prompt.
5. The generated response is returned to the user in JSON format.

## Future Enhancements

- Develop a React.js frontend.
- Add user authentication.
- Implement conversation history.
- Improve input validation and error handling.
- Add support for multiple summarization formats.