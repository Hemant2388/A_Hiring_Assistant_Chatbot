import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=api_token
)

model = ChatHuggingFace(llm=llm)

def greet_user():
    return "👋 Hello! I'm your Hiring Assistant. I’ll help you assess technical skills by generating tailored questions based on your tech stack."

def end_conversation():
    return "🎯 Thank you for providing the information! Our team will review your responses and get in touch with you shortly."

def handle_fallback(error_msg):
    return f"⚠️ Something went wrong or input was unclear. Please check your details and try again. Error: {error_msg}"

def generate_questions_llm(tech_stack):
    try:
        prompt = f"Generate 5 technical interview questions for a candidate experienced in: {tech_stack}."
        response = model.invoke(prompt)  # <-- directly call llm
        print("📤 LLM Output:", response)
        return response.content
    except Exception as e:
        return handle_fallback(str(e))