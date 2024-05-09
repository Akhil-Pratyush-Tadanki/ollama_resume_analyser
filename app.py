import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import PyPDF2 as pdf
from langchain_community.llms import Ollama

ollama_model=Ollama(base_url='http://localhost:11434',
                    model='ats_model')
# load_dotenv() #load all our environment variables

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_ollama_response(input,resume):
    response=ollama_model.invoke("Job Description-"+input+"resume-"+resume)
    return response

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

## steamlit app

st.title("Smart ATS Using Custom Ollama Model")
st.text("""I am an AI-powered text analysis agent, designed to help job seekers and recruiters by analyzing job descriptions and resumes. My primary function is to extract keywords and skills from job descriptions and compare them with the information present in a resume.

Here's how I can assist:

1. **Job Description Analysis**: Given a job description, I can extract relevant keywords and skills that are typically required for the role.
2. **Resume Analysis**: Provided with a text-based resume, I can identify the keywords and skills mentioned in the resume.
3. **Mismatch Identification**: By comparing the extracted keywords and skills from the job description with those present in the resume, I can highlight any missing or mismatched information that may make the candidate less competitive for the role.
4. **Matching Score**: Finally, I can provide a matching score, which represents how well the resume is tailored to the job description. This score helps recruiters and hiring managers quickly assess the relevance of a candidate's application.
        """)
jobdes=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload the Resume", type="pdf",help="please upload PDF")

submit=st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_ollama_response(jobdes,text)
        st.subheader(response)
