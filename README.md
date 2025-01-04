1. Project Overview

The TalentScout Hiring Assistant chatbot is an intelligent recruitment tool designed to assist "TalentScout," a fictional recruitment agency specializing in technology placements. The chatbot simplifies the initial screening process by:

Gathering essential candidate details like name, contact information, experience, and tech stack.

Generating tailored technical interview questions based on the declared tech stack.

Ensuring coherent and context-aware interactions to provide a seamless user experience.

2. Installation Instructions

Follow these steps to set up and run the application locally:

Clone the Repository:

git clone <repository_url>
cd TalentScout

Set Up the Environment:

Install Python (>=3.8).

Install necessary libraries:

pip install -r requirements.txt

API Key Configuration:

Create a .env file in the project directory.

Add your API key for Google Generative AI:

API_KEY=your_api_key_here

Run the Application:

streamlit run app.py

3. Usage Guide

Launch the Application:
Open the provided URL in your web browser after running the application.

Interact with the Chatbot:

Enter personal details like name, email, phone number, experience, and desired position.

Provide your tech stack (e.g., Python, Django, PostgreSQL).

Click on "Generate Questions" to receive tailored technical questions.

End the Conversation:
Type a conversation-ending keyword (e.g., "exit") to gracefully conclude the interaction.

4. Technical Details

Libraries Used:

streamlit: For the frontend interface.

google.generativeai: For leveraging generative models to craft questions.

dotenv: To manage API keys securely.

Model Details:

The chatbot uses Google’s Gemini-Pro generative model for crafting technical questions based on user input.

Architectural Decisions:

Frontend: Developed using Streamlit for simplicity and interactivity.

Backend: Powered by Google Generative AI for dynamic content generation.

Data Handling: Minimal storage and privacy-focused, leveraging .env for secure API keys.

5. Prompt Design

Purpose:

To accurately gather candidate information.

To generate 3-5 tailored technical questions for the specified tech stack.

Example Prompt:

"You are an assistant generating 5 technical interview questions for the following tech stack: {tech_stack}."

Optimization:

Prompts are designed to be concise and guide the model for coherent outputs.

Ensures context-aware responses for diverse tech stacks.

6. Challenges & Solutions

Challenge: Handling diverse tech stacks with varying complexities.

Solution: Optimized prompts to ensure relevance and tailored questions for each input.

Challenge: Managing sensitive candidate data securely.

Solution: Used .env files for API keys and avoided persistent storage of sensitive information.

Challenge: Maintaining context in conversations.

Solution: Integrated context-aware prompt design and dynamic response mechanisms.
