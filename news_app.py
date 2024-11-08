import streamlit as st 
import pandas as pd 
import requests 

#For using my API key, you can use your own API key 
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")


if 'data' not in st.session_state:
    #data fetching from api
    response = requests.get(f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}')
    data = pd.DataFrame(response.json()['articles'])
    st.session_state.data = data[['title', 'description', 'url', 'urlToImage', 'publishedAt', 'content']]

rows = st.session_state.data.shape[0]
dates = st.session_state.data['publishedAt']
#removing unnecessary details in dates
dates = dates.apply(lambda x:x.split(".", 1)[0])
dates = dates.apply(lambda x:x.replace("T", "  "))
titles = st.session_state.data['title']
imageLinks = st.session_state.data['urlToImage']
contents = st.session_state.data['content']
#removing the [+something characters] 
contents = contents.apply(lambda x:x.split("[", 1)[0])
links = st.session_state.data['url']
descriptions = st.session_state.data['description']





def news_page(num):
    n = int(num)

    st.header(titles[n])
    st.write(dates[n])
    st.write(descriptions[n])
    st.image(imageLinks[n])   
    st.write(contents[n])
    st.link_button("More", links[n])
    
# Show different pages based on the selection
def check(page):
    if page == "Home":
        home_page()
    elif page == titles[0]:
        news_page(num="0") 
    elif page == titles[1]:
        news_page(num="1") 
    elif page == titles[2]:
        news_page(num="2") 
    elif page == titles[3]:
        news_page(num="3") 
    elif page == titles[4]:
        news_page(num="4") 
    elif page == titles[5]:
        news_page(num="5") 
    elif page == titles[6]:
        news_page(num="6") 
    elif page == titles[7]:
        news_page(num="7") 
    elif page == titles[8]:
        news_page(num="8") 
    elif page == titles[9]:
        news_page(num="9") 
        
def home_page():
    st.header("Today's Top News")
    for title in titles:
        st.write("-", title)
    
page_list = ["Home"]
for title in titles:
    page_list.append(title)
page = st.sidebar.selectbox("Choose a page:", page_list)

check(page)