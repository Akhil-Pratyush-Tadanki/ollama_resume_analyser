# Ollama_resume_analyser
AI-powered text analysis agent, designed to help job seekers by analysing job descriptions and resumes. The primary function is to extract keywords and skills from job descriptions and compare them with the information present in a resume.

## Pre Requisits/ Setup steps
Install Ollama3 from https://ollama.com
List of models available in ollama- https://ollama.com/library

Running ollama in terminal
- ollama pull <Model_Name> #Downloads the model
- ollama run <Model_Name> # Runs the model
- ollama list #list of installed models
- /exit to exit a model

Creating a model file
- nano <model_file_name>
- Inside the file give parameters and commands Guide- https://github.com/ollama/ollama/blob/main/docs/modelfile.md
Sample model file- ats_ollama3

After writing the model file create your custom model using command
- ollama create <custom_model_name> -f ./<model_file_name>
- ollama run <custom_model_name> to use the model in terminal.
- check list ($ ollama list) to see your model there which can be used in your notebook/code

using custom model in vs code/ notebook using langchain
```
from langchain.llms import 0llama
ollama = 0llama (base url='http: //localhost:11434', model= "<custom_model_name>")
print (ollama ("who are you?")) #test your custom model
```
You can also use ollama models with api calls which is not demonstrated in this project.

VS code environment setup using conda
- conda create -p <your_env_name> python==3.10 -y
- create 2 files .env and requirements.txt
- .env file is to store your api key which is not a part of this project as we are using local model.
- requirements.txt to list all the required libraries.

Installing requirements
- conda activate <your_env_name> #activate your env
- pip install -r requirements.txt # installl all required libraries
- conda deactivate #deactivate env after use

Running streamlit app
- streamlit run app.py 
  

## Project overview
1. Install and run llm (ollama) locally into your system
2. Use LLM to analyse resume and job description to give missing keywords and matching score and suggestions.
3. Build a custom modelfile to tailor the model to our needs and create your custom LLM model.
4. Use langchain to use your custom model and make the analyser application using streamlit.


## Output streamlit app

