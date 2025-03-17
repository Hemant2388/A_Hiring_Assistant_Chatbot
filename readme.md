TalentScout - A hiring assistance chatbot.

# Project Overview
TalentScout is an interactive AI-powered Hiring Assistant chatbot built using **Streamlit**, **LangChain**, and **Hugging Face Transformers**. It streamlines the technical screening process by collecting candidate information and generating tailored interview questions based on their tech stack.


## Features
This project aims to assist HR professionals and hiring managers by automating parts of the recruitment process. The chatbot:

- Greets candidates in a friendly manner.
- Collects anonymized/simulated candidate data (in compliance with data privacy practices).
- Generates role-specific technical interview questions using LLMs.
- Handles fallback gracefully in case of errors or missing inputs.
- Stores anonymized candidate data in a CSV file for review.


#  Project Folder Structure
├── TalentScout/
    ├── app.py
    ├── candidate_data.csv
    ├── chatbot_logic.py 
    ├── data_handler.py
    ├── readme.md
    ├── requirements.txt
    ├── utils.py


## Setup and Installation
Clone the repository:

```sh
git clone 
cd 
```
Set up a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:
``` sh
pip install -r requirements.txt
```

Create a .env file in the root directory.
Add your Hugging Face API token:
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token

Run the application:
```sh
streamlit run app.py 
```
The API should now be running on http://localhost:8502.

