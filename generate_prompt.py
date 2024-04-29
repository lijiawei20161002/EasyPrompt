import pandas as pd
import os
import openai
from pandas import read_parquet

df = pd.read_parquet('test_set.parquet', engine='fastparquet')
openai.api_key = os.getenv('API')

# Function to ask GPT-4 a question and determine if the answer is correct
def ask_gpt(question, correct_answer):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[{"role": "system", "content": "You are a knowledgeable assistant."}, 
                        {"role": "user", "content": question}]
        )
        # Assume the model's response is processed to extract a numeric answer
        predicted_answer = int(response['choices'][0]['message']['content'].strip())
        print(question, predicted_answer, correct_answer)
        return predicted_answer == correct_answer
    except ValueError:
        return False

# Loop through the DataFrame and collect questions with correct answers
correct_questions = []
for index, row in df.iterrows():
    if len(correct_questions) >= 10:
        break
    if ask_gpt(row['question']+" Your answer must be a choice in "+str(row['choices'])+" Only output the choice index, no other information.", row['answer']):
        correct_questions.append(row['question'])

with open('correct_questions.txt', 'w') as file:
    for question in correct_questions:
        file.write(question + '\n')

print("Questions where the model got the correct answer:", correct_questions)

