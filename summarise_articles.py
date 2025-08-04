#summarize articles using LLM

import pandas as pd
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm
from transformers import pipeline

#alternate hugging face summarizer LLM
# Force pipeline to use PyTorch (and NOT TensorFlow/Keras)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt")


#load openai key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

#LOAD NEWS DATA

df = pd.read_csv("data/news_raw.csv")

df["summary"] = ""
df["summary_alt"]=""

# Loop through each article and summarize

for idx, row in tqdm(df.iterrows(), total=len(df)):
    content = row["content"]
    if pd.isna(content) or len(str(content)) < 30:
        content = row["description"]
    if pd.isna(content):
        summary = "No content to summarise"
        summary_alt = "No content to summarize."

    else:
        try:
            prompt=f"Summarise the following news articles in 2 sentances:\n\n{content}"
            response = client.chat.completions.create(
                       model="gpt-3.5-turbo",
                       messages=[{"role": "user", "content": prompt}],
                       temperature=0.7
                      )

            summary = response.choices[0].message.content.strip()
        except Exception as e:
            summary = f"Error: {e}"
            
        # === 2. HuggingFace Summary ===
        try:
            result = summarizer(content, max_length=100, min_length=30, do_sample=False)
            summary_alt = result[0]['summary_text']
        except Exception as e:
            summary_alt = f"Error: {e}"    

    df.at[idx, "summary"] = summary
    df.at[idx, "summary_alt"] = summary_alt

# Save the summarized data
df.to_csv("data/news_summarized.csv", index=False)
print("Summaries saved to data/news_summarized.csv")

