import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.title('Moin zusammen')
streamlit.header('Header')

streamlit.text('sonstiges')
streamlit.text('sonstiges  🥝🍇')
streamlit.text('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
streamlit.dataframe(fruits_to_show)
