

# **T5 Model for Summarization and Question Answering**

---

## **📖 Overview**  

This repository features the implementation of the **T5 (Text-To-Text Transfer Transformer)** model, enabling two core functionalities: **Summarization** and **Question Answering**. The model excels in generating concise summaries of long texts and providing precise answers to questions based on a given context.  

---

## **🚀 Features**  

### **1. Summarization**  
- Efficiently processes lengthy textual inputs into short, coherent summaries.  
- Uses a specific input format for summarization:  
  ```  
  "summarize: <your text>"  
  ```  

### **2. Question Answering**  
- Generates contextually relevant answers to specific questions.  
- Input format:  
  ```  
  "question: <your question> context: <context>"  
  ```  

---

## **📂 Directory Guide**  

### **Implementation Files**  
- **`t5_qna_sum.ipynb`**:  
  - The primary notebook for training, fine-tuning, and testing the T5 model for both summarization and question-answering tasks.  

### **Output and Logs**  
- **`output_result`**:  
  - Contains training logs, output files, and metrics from model evaluation.  

### **Saved Models and Output**  
- **`models`**:  
  - Includes models saved after training, optimized for deployment or further experimentation.
 
- **`generated_texts_table.csv`**:  
  - Includes generated text by the trained model.

### **Weights and Biases**  
- **`wandb`**:  
  - Stores logs, visualizations, and analytics for tracking training progress using **Weights and Biases (W&B)**.  

---

## **🔗 Useful Links**  

- **Main Repository**: [E-47_QuestionAnswering-seq2seq](https://github.com/amitingits/E-47_QuestionAnswering-seq2seq)  

---

**🔖 Created with ❤️ by Team E-47.**  
