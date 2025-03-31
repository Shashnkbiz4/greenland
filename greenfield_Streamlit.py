import streamlit as st
import os
import openai
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Set up Groq API Key
client = Groq( api_key=os.environ.get("GROQ_API_KEY"))

# Function to interact with Groq API
def generate_llm_response(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Adjust as per Groq API model availability
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2000
    )
    return response.choices[0].message.content.strip()


# Streamlit UI
st.set_page_config(page_title="AI Codegen Workflow", layout="wide")
st.title("🚀 Greenfield AI Codegen Workflow")
st.write("Use AI to plan and execute your project efficiently.")

# Tabs for different workflow steps
tab1, tab2, tab3 = st.tabs(["🧠 Idea Honing", "📋 Planning", "⚙️ Execution"])

# Tab 1: Idea Honing
with tab1:
    st.header("🧠 Idea Honing: Refine Your Concept")
    idea = st.text_area("Enter your initial project idea:")
    if st.button("Generate Spec", key="spec"):
        if idea:
            prompt = f"""
            Help me refine this idea into a structured software project specification.
            - Ask relevant questions one by one to improve the idea.
            - Generate a final specification including:
              - **Project Overview**
              - **Key Features**
              - **Technology Stack**
              - **Implementation Plan**
            
            Idea: {idea}
            """
            response = generate_llm_response(prompt)
            st.subheader("📜 AI-Generated Specification:")
            st.write(response)
        else:
            st.warning("Please enter an idea first.")

# Tab 2: Planning
with tab2:
    st.header("📋 Planning: Break It Down")
    refined_spec = st.text_area("Enter the refined project specification:")
    if st.button("Generate Plan", key="plan"):
        if refined_spec:
            prompt = f"""
            Take the following software project specification and break it down into a step-by-step development plan:
            - Each step should be small, iterative, and build on previous steps.
            - Prioritize best practices and ensure test-driven development.
            - Avoid big complexity jumps.
            - Output the steps in a numbered list format.
            
            Specification: {refined_spec}
            """
            response = generate_llm_response(prompt)
            st.subheader("📌 AI-Generated Development Plan:")
            st.write(response)
        else:
            st.warning("Please enter a project specification first.")

# Tab 3: Execution
with tab3:
    st.header("⚙️ Execution: Generate Structured Codegen Prompt")
    task = st.text_area("Describe what you want to build:")
    if st.button("Generate Codegen Prompt", key="execute"):
        if task:
            prompt = f"""
            Generate a structured code generation prompt for a large language model (LLM) to execute.
            - Ensure the prompt guides the LLM to generate what user wants.
            - The prompt should not to be long and it should be in paragrapgh or bullet points NO HEADER ,TITLE 
            - In the output dont ever give any code, just create a structure prompt also include what user's code snippet that user provided
            - while writing prompt consider yourself as the user, so use first person language and consider LLM as YOU. for example,"I want you yo analyse this "

            
            Task: {task}
            """
            response = generate_llm_response(prompt)
            st.subheader("📝 AI-Generated Codegen Prompt:")
            st.write(response)
        else:
            st.warning("Please enter a task description first.")

st.write("💡 Use these AI-generated insights to build your project efficiently!")
