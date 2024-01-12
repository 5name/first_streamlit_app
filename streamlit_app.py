import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title('Moin zusammen')
streamlit.header('Header')

streamlit.text('sonstiges')
streamlit.text('sonstiges  🥝🍇')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_list)
