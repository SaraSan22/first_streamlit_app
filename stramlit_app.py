import streamlit
streamlit.title('🥣My Parents New Healthy Diner🥣')
streamlit.header('Breakfast Menu🍞🥗 ')  
streamlit.text('Omega 3 milk')
streamlit.text('Scrumbled eggs🐔')
streamlit.header('Build your own fruit smoothie🥑')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
