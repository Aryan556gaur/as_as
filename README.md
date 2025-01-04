TalentScout Intelligent Hiring Assistant Chatbot

Overview

The TalentScout Intelligent Hiring Assistant Chatbot is an AI-powered application designed for recruitment agencies specializing in technology placements. It streamlines the initial screening of candidates by collecting essential details and generating tailored technical questions based on their declared tech stack.

Key Features

Candidate Information Collection:

Gathers essential details like name, contact info, years of experience, desired positions, and tech stack.

Tech Stack-Based Question Generation:

Uses advanced generative AI to produce 3-5 technical interview questions for the specified tech stack.

Interactive UI:

Built using Streamlit for a clean and user-friendly interface.

Context Handling:

Maintains conversation context for seamless interactions.

Fallback Mechanisms:

Provides meaningful responses for unexpected inputs.

Conversation Conclusion:

Gracefully ends conversations with next-step guidance.

Installation

Prerequisites

Python 3.8+

Required Python packages: streamlit, google-generativeai, dotenv

Setup

Clone the repository:

git clone <repository_url>
cd TalentScout

Install dependencies:

pip install -r requirements.txt

Set up your environment variables:

Create a .env file in the project root:

API_KEY=<Your_Generative_AI_API_Key>

Run the application:

streamlit run app.py
