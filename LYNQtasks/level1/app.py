import os
import gradio as gr
from step1 import ask_llm
from step2 import analyse_pdf

def gradio_inputs(pdf_path, prompt):

    if pdf_path is not None:
        return analyse_pdf(pdf_path, prompt)
    else:
        return ask_llm(prompt)
    
css = """
footer { display: none !important; }
textarea {resize: vertical !important;}
"""

interface = gr.Interface(
    fn = gradio_inputs,
    inputs = [
        gr.File(label="Upload PDF"),
        gr.Textbox(lines=3, placeholder="Enter your question here")
    ],
    outputs = gr.Textbox(lines=12,label="Answer"),
    title = "Basic chatbot",
    description=("Ask questions with or without a pdf"),
    allow_flagging="never",
    css = css
)    

if __name__ == "__main__" :
    interface.launch(inbrowser=True)