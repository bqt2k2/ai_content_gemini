# AI Content Generator

A lightweight, FastAPI-based application that generates content using OpenAI's API. Designed for scalability and easy deployment on Railway, the app allows users to send prompts and receive AI-generated text content in return. Ideal for automating blog writing, marketing content, or social media posts.

## Features

- 🔧 Built with FastAPI and Uvicorn for high performance
- 🚀 Deployed on Railway with automatic builds and HTTPS
- 🤖 Integrates with OpenAI API for content generation
- 🔐 API key secured via environment variables
- 🔁 Ready for integration with frontends or chatbots

## Tech Stack

- **Backend:** FastAPI, Uvicorn
- **Deployment:** Railway
- **AI Engine:** OpenAI API (GPT)
- **Others:** Python, dotenv, requests

## How to Run Locally

```bash
git clone <repo-url>
cd project-directory
pip install -r requirements.txt
# Add your OpenAI key to .env file
echo "API_KEY=sk-xxxxx" > .env
uvicorn main:app --reload
