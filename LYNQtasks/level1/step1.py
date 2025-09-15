import os
api_key = os.getenv("GOOGLE_API_KEY")

import google.generativeai as genai   
genai.configure(api_key = api_key)                

def ask_llm(prompt) :
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__" :

    question = input("What is your question").strip()

    try:
        answer = ask_llm(question)
        print("gemini says: ", answer)
    except Exception as e:
        print(f"error occured: {e}")
        print("Make sure you have set your GOOGLE_API_KEY environment variable")