import streamlit as st
import pandas as pd

st.title("📰 News Insights Dashboard📰 ")

df = pd.read_csv("data/news_summarized.csv")

# No filtering — show everything
for i, row in df.iterrows():
    st.subheader(row['title'])
    # Display published date in smaller text
    st.markdown(f"<small><i>Published at: {row['publishedAt']}</i></small>", unsafe_allow_html=True)
    st.write(row['summary_alt'])
    st.markdown("---")