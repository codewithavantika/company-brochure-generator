# AI Company Brochure Generator

## Overview
This project is an AI-powered application that generates professional company brochures using a local Large Language Model (LLM) through Ollama.  
Users provide basic company details, and the system automatically creates structured brochure content.
Demonstrates hands-on experience in prompt engineering, REST API integration, local LLM inference, and structured JSON data handling.

## Features
- Accepts company name, industry, target audience, and tone as input
- Generates professional brochure content using Ollama
- Saves generated output in JSON format
- Displays brochure output in the terminal
- Clean and beginner-friendly Python code

## Technologies Used
- Python
- Ollama (TinyLLaMA / Phi)
- REST API
- JSON
- Git & GitHub

## How to Run
1. Start Ollama
2. Make sure a small model like `tinyllama` or `phi` is installed
3. Open terminal in the project folder
4. Run:
   python app.py
5. Enter company details when asked

## Problem Statement
Creating professional company brochures manually is time-consuming and repetitive. This project automates brochure generation using AI to produce structured and consistent content.

## Output
- Brochure shown in terminal
- JSON file saved in `sample_outputs/`
Example file:
sample_outputs/Demo_Company_brochure.json

## Learning Outcomes
- Prompt engineering
- Working with local LLMs
- API calls in Python
- JSON file handling
- Git and GitHub workflow

## Future Improvements
- Add Streamlit-based UI for easier input and brochure preview
- Enable PDF export of generated brochures
   
## Author
Avantika Gupta  
GitHub: https://github.com/codewithavantika
