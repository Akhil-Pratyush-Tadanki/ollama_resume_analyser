# ollama_resume_analyser
AI-powered text analysis agent, designed to help job seekers by analysing job descriptions and resumes. The primary function is to extract keywords and skills from job descriptions and compare them with the information present in a resume.

## Pre Requisits
Install Ollama3 from https://ollama.com
List of models available in ollama- https://ollama.com/library

running ollama in terminal-
- ollama pull <Model_Name> #Downloads the model
- ollama run <Model_Name> # Runs the model
- ollama list #list of installed models
- /exit to exit a model

creating a model file
- nano <model_file_name>
- Inside the file give parameters and commands Guide- https://github.com/ollama/ollama/blob/main/docs/modelfile.md
Sample model file- ats_ollama3

After writing the model file create your custom model using command
- ollama create <custom_model_name> -f ./<model_file_name>
-check list ($ ollama list) to see your model there which can be used in your notebook/code



Steps-
1. Install and run llm (ollama) locally into your system
2. Use LLM to analyse resume and job description to give missing keywords and matching score and suggestions.
3. Build a custom modelfile to tailor the model to our needs and create your custom LLM model.
4. Use langchain to use your custom model and make the analyser application using streamlit.
