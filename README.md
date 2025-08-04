News Insights Dashboard 
📰<img width="1025" height="696" alt="Screenshot 2025-08-04 at 1 16 03 PM" src="https://github.com/user-attachments/assets/732a79ab-dd17-4be7-abd7-180863e4034b" />

Over the past day, I built a fully functional data pipeline + dashboard to fetch, summarize, and visualize real-time news content — integrating multiple tools in a complete end-to-end workflow!

🔧 What I did:

✅ Fetched breaking news using a public API
✅ Parsed and stored the data into CSV format
✅ Applied dual summarization using:
	•	🔁 OpenAI GPT (for premium quality, where quota allowed)
	•	🤗 HuggingFace transformers (distilbart-cnn) for fallback, open-source summarization
✅ Cleaned + structured the data with fallback logic (title > content > description)
✅ Built a Streamlit dashboard to filter articles by category, and display summaries along with their publish dates

📊 Tools & Tech Stack:
Python | OpenAI API | Hugging Face | Streamlit | Pandas | Transformers

🔍 Takeaways:
➡️ Learned to handle API rate limits smartly
➡️ Worked with fallback logic for missing data
➡️ Used HuggingFace models offline for free summarization
➡️ Improved deployment-ready dashboard skills using Streamlit

🧠 Next Steps:
Thinking of adding keyword tagging, sentiment analysis, and topic clustering to make this dashboard even more insightful!


Here’s a quick visual flow of what was built 👇
<img width="449" height="692" alt="Screenshot 2025-08-04 at 1 21 07 PM" src="https://github.com/user-attachments/assets/ba4a60aa-06af-429b-9027-0a9bc8178415" />

Let me know what you think — and if you’re working on something similar, I’d love to connect and exchange ideas! 👋

#DataEngineering #LLM #Streamlit #OpenSource #NLP #NewsSummarization #Python #DataScienceProject
