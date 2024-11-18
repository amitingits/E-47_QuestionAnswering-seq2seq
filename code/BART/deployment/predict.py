import torch
from transformers import BartTokenizer, BartForConditionalGeneration

tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model(model_path):
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-base")
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    return model


def generate_predictions(model, question, context):
    inputs = tokenizer(question + " " + context, return_tensors='pt', max_length=512, truncation=True).to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.strip()

def ensemble_predict(question, context, models):
    predictions = []

    for model in models:
        pred = generate_predictions(model, question, context)
        predictions.append(pred)

    final_predictions = max(set(predictions), key=predictions.count)
    return final_predictions