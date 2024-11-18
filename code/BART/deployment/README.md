---
title: Seq2Seq Question Answering
emoji: 🦀
colorFrom: indigo
colorTo: green
sdk: gradio
sdk_version: 5.5.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Question Answering seq2seq model using BART
---

Link to the app : [Click Here](https://huggingface.co/spaces/amithugs/Seq2Seq-Question-Answering/)

**This directory contains the files used to deploy the fine tuned model into the hugging face Spaces platform.**
 
* **requirements.txt** to specify the required modules and libraries needed for successful deployment.
* **app.py** is the main app file and contains the script to launch the app defined within it.
* **predict.py** is the script file which contains the functions such load_model(), generate_predictions(), ensemble_predict()

The models(model_0.pt, model_1.pt) used for the app provided is located in the root directory in the Spaces which is saved under the folder "/code/BART/saved_models" of this tree.

