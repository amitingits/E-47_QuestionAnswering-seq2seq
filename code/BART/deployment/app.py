from transformers import BartForConditionalGeneration
import torch
import gradio as gr
from predict import ensemble_predict, load_model
import functools

models = []
for i in range(2):
    model = load_model(f"model_{i}.pt")
    models.append(model)

ensemble_with_models = functools.partial(ensemble_predict, models=models)


with gr.Blocks() as app:
    gr.Markdown("Question Answering App using BART")
    
    # Input box (context)
    context_input = gr.Textbox(label="Context", placeholder="Enter your paragraph here...", lines=5)
    
    # Input box for question
    question_input = gr.Textbox(label="Question", placeholder="Ask any question within the paragraph.")
    
    # submit inputs
    submit_button = gr.Button("Get Answer")
    
    # Output
    output_text = gr.Textbox(label="Answer", interactive=False)
    submit_button.click(ensemble_with_models, inputs=[question_input, context_input], outputs=output_text)

# Launch the app
app.launch()