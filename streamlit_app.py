import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞 Avacado Toast')
streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#setting fruit col as the index
my_fruit_list = my_fruit_list.setindex('Fruit')
#put a pick list here so the user can pick they want to include
streamlit.multiselect ("Pick some fruits: ", list(my_fruit_list.index))
#display the table
streamlit.dataframe (my_fruit_list)
