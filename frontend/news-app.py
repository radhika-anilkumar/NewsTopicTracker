import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 
import streamlit as st
from backend.news_scraper import fetch_google_news
from backend.summarizer import summarize_text
from backend.topic_grouper import group_headlines_by_topic
 
# Add category selector
category = st.selectbox(
    "Choose News Category",
    ["World", "Technology", "Sports", "Business", "Health", "Entertainment"]
)
 
st.title(f"🗞️ Trending in {category}")
 
news = fetch_google_news(category, max_articles=10)
headlines = [article["headline"] for article in news]
 
if not headlines:
    st.warning("No headlines found for this category.")
else:
    for article in news:
        st.subheader(article["headline"])
        st.write(summarize_text(article["headline"]))