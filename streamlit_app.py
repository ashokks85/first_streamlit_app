
import streamlit

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Menu')

streamlit.text(' π₯£ Omega 3 and Blueberry Oatmeal')
streamlit.text(' π₯ Kale and Spinach')
streamlit.text(' πHard Boiled Eggs')
streamlit.text(' π₯π Avocado toast')

streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])  

fruits_to_show=my_fruit_list.loc[fruits_selected]

streamlit.dataframe(my_fruit_list)

streamlit.dataframe(fruits_to_show)
