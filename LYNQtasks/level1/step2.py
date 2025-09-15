import os
api_key = os.getenv("GOOGLE_API_KEY")

import google.generativeai as genai   
genai.configure(api_key = api_key)

from pypdf import PdfReader

def analyse_pdf(pdf_path, user_prompt):

    # extracting all text from the pdf
    reader = PdfReader(pdf_path)
    full_text = " "
    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    # truncating because of token limits
    if len(full_text) > 8000:
        full_text = full_text[:8000] + "... content truncated"

    full_prompt = f" Based on this PDF content: {full_text}, User Question: {user_prompt}, Please answer the question based on the PDF content above."

    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(full_prompt)
    return response.text    


if __name__ == "__main__" :

    pdf_path  = input("Enter the complete path of your pdf file : ").strip()
    user_prompt =  input("What do you want to know about the pdf? ").strip()

    if not os.path.exists(pdf_path):
        print(f"file '{pdf_path}' not found!")
    else:
        print(f"\nAnalysing '{pdf_path}'...")
        answer = analyse_pdf( pdf_path, user_prompt ) 
        print("AI Response:")
        print(answer)   
