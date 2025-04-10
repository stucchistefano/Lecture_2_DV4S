import streamlit as st
import numpy as np
import pandas as pd

st.title("This is an Info & Layout page")

# Get information from the sidebar (with the keywords presented)
st.subheader("Getting information from the sidebar")

# Creation of new variables in the page and recall of the keywrods to put in them the already selected values
player = st.session_state['Players']
team = st.session_state['Team']

# Write the values (selected into the sidebar)
st.write("Selected player is: ", player)
st.write("Selected team is: ", team)
# Changing the selections in the sidebar, the values of the plotted variables are changed
# Using session_state is really useful to do not have variables only visible into the main page (or one page)


# Columns
st.subheader("Columns")
st.write("We are using columns, with their proper method")

# Object-like approach/notation (of their definition)
col1, col2 = st.columns(2) # Split of the page into 2 different columns items
# In the "spec" parameter we could define the number of columns wanted, or a tuple with the % of the width of the page that are occupied by the different columns (or we could specify the width of the column, and then the number of column with this same width)
# We could also define the space between different columns (then the order of the items put into the method, is the same of the order of the columns that must be recalled)
col1.header("This is column 1 - Basket")
col1.image("data:image/jpeg;base64,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")
col2.header("This is column 2 - Soccer")
col2.image("data:image/jpeg;base64,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")
# We could save the images into a folder on the PC or spacecode, and then recall them with their paths
# We could work on the dimension of the columns to fit the user need in this way
# col1, col2 = st.columns([0.6,0.4])

# "with"-like approach/notation (of their definition)
st.subheader("More columns")
# Simulation of some data, with numpy
data = np.random.rand(20,1)

# Creation of two columns with the width of 3 and 1
colA, colB = st.columns([3,1])

# With the "with" method we are entering into a column at time, and thus we do not use the "." notation, but we need to recall directly the main library "st."
with colA:
    st.header("Data Viz")
    st.bar_chart(data)
with colB:
    st.header("Table")
    st.table(data)


# Tabs
st.subheader("Tabs")
# The user should push and click on the tabs and their containers to see and work on the information (contained into the tab)
tab1,tab2 = st.tabs(['Football', 'Skiing'])
# "tabs" parameter is a list of string, which are defining the information of the tabs
# This methods returns a list of containers, like the "st.columns" one
tab1.header("This is tab 1 - Football")
tab1.image("https://preply.com/wp-content/uploads/2022/01/americanfootball.jpg")
tab2.header("This is tab 2 - Skiing")
tab2.image("https://dev-snowit.ams3.digitaloceanspaces.com/uploads/2018/11/Aprica-copertina-canva.jpg")
# Only by clicking on the tab-button we could see (on the same part/place of the web app) a different element/image or information


# Expanders
st.subheader("Expanders")
# They are the last containers' elements, which could expand when clicked
st.write("We are working with expanders")

# "with"-like notation/approach (for their definition)
with st.expander("Data Viz", expanded=True):
    # The "expanded" is setting with a boolean if it is expanded or not at the start
    st.subheader('My Data')
    st.line_chart(data)

# Or not expanded expander at the start
with st.expander("Table", expanded=False):
    st.subheader("Table of My Data")
    st.table(data)
# By clicking on the "name" of the expander, we could close or open the expander (with its related info) when we want (like the users)


# Exercise in class
st.title("Exercise/Training in class")
# Simulated data
team_name = "Atlanta United"
seasons = ["2020-21", "2021-22", "2022-23", "2023-24"]
wins = [20, 22, 18, 25]
losses = [10, 8, 12, 5]
goals_scored = [60, 65, 55, 70]
top_scorer = {"Messi":10, "Pelè":15, "Retegui":20}

st.subheader("Data Visualisation for Sport - Exercise")

col1, col2 = st.columns(2)
with col1:
    st.header("Wins in different seasons")
    Win_data = {"S":seasons, "W": wins}
    st.bar_chart(Win_data, x="S", y="W")
with col2:
    st.header("Losses in different seasons")
    Los_data= {"S":seasons, "L": losses}
    st.bar_chart(Los_data, x="S", y="L")

tab1, tab2 = st.tabs(["Goals Scored", "Top Scorers"])
tab1.header("Goals Scored")
goal_data ={"S":seasons, "G":goals_scored}
tab1.area_chart(goal_data, x="S", y="G", color="#FFFFFF")
tab2.header("Top Scorers")
tab2.bar_chart(top_scorer)
tab2.image("https://assets.goal.com/images/v3/blt10b807851956e767/retegui%20lecce%20atalanta%20goal.jpg")

data ={
    "Season": seasons,
    "Goals": goals_scored,
    "Wins": wins,
    "Losses": losses,
    #"Top Scorers": top_scorer
}
df= pd.DataFrame(data)

with st.expander("Wins & Goals", expanded=False):
    st.subheader("Wins & Goals Relation")
    wins_goals_data = df[["Season", "Wins", "Goals"]]
    st.line_chart(wins_goals_data.set_index("Season"), color=("#008000", "#FFFFFF"))
with st.expander("Losses & Goals", expanded=False):
    st.subheader("Losses & Goals Relation")
    losses_goals_data = df[["Season", "Losses", "Goals"]]
    st.line_chart(losses_goals_data.set_index("Season"), color=("#FF0000", "#FFFFFF"))
    

"""
# Secrets of Streamlit
st.subheader("Secrets")
# We can recall the secret info with the method "st.secrets()", which works as a dictionary
username = st.secrets["username"]
# We can write it at screen
st.write("The username is: ", username)

import os
# To get information not from the secret file, but from the "operating system (os)"
password = os.environ["password"]
st.write("The password is: ", password)

# Accessing more and tree-organized secret information
secret_psw = st.secret.further_secrets.secret_username # With the "." notation we could move on in the tree of the secret info
st.write("The secret password is: ", secret_psw)
"""

# Connection to Google Sheet
from streamlit_gsheets import GSheetsConnection
# Object related to the connection
gconn = st.connection("gsheets", type=GSheetsConnection) # st.connection is defined and usable also for all other connection, not only to Google Sheet

# Read the connection
df = gconn.read(
    #worksheet=0, # To decide which sheet to read
    #usecols=[1,2], # To choose the columns and the rows to read
    #nrows=2
) # If we do not put anything in the read() brackets, we have that the program runs correctly starting from the link into the secrets
# Before we save the data into some dataframe and then we could plot it
st.dataframe(df)

# We need to use a proper function to read an excel function
# We have limited space in the repository of github (it is better to link to some data online)
# We can create a file and connect it to some online spaces
import os

# To extract the current working directory (CWD)
cwd = os.getcwd()
filename2save = os.path.join(cwd, "data2save.csv") # Saving of the file into a .csv file, with this name
df.to_csv(filename2save, index=False) # Effective saving in .csv file, with "index=False" to do not save also the indexes of the dataframe into the .csv format
st.success("File Saved!")


# Additional components
# iframe web page
st.subheader("iframe")
st.write("Use of iframe")
import streamlit.components.v1 as components

# Embed fantacalcio web page
components.iframe("https://www.fantacalcio.it/", height=500, scrolling=True)
# The "scrolling" component should be used to allow the scrolling

# VEDI SUE SOLUZIONI DA QUI IN POI
# HTML components
# With the method "components.html(...)", with an html code that define the web components that it represented by a Figma like button
# These buttons, if implemented with html, could not be used to "function" so to remind and report to some actions or pages as st.button() ones
# The "st.markdown(...)" is the components that allows us to match the deisgned html buttons with the st.button() abilities and the streamlit functioning
# We could link a callback function correlated with the st.button() components (that are recalled when the button is pressed) --> We could made it by defining the function and then recalling it in/when the button is clicked
# Then, after having placed the st.button(), we could place the "st.markdown()" method that is able to change the style of the component of streamlit before made (not spend too much time to change streamlit components)
