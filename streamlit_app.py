import streamlit as st

# Definition of the names of the pages and of what is present into them
page1 = st.Page('page1.py', title="Page 1")
page2 = st.Page('page2.py', title="Page 2")
# We have only defined the pages as objects, and then now we need to define the sidebar that allows to navigate into them (with a "navigation" object)

pg = st.navigation([page1,page2]) # In the navigation object we need to put a list (in []) of the pages in which we need to navigate
st.set_page_config(page_title="DV4S - Lecture 3")

# Selectbox (into the sidebar)
# Object-like approach
st.sidebar.selectbox(
    "Select your player",
    ('Lookman','Bellingham','Mbappe'),
    key ='Players' # Introduction of a keyword to recall the players in the pages
    )

# "with"-like approach
with st.sidebar:
    rb = st.radio(
        "Team",
        ('Atalanta', 'Real Madrid', 'Internazionale'),
        key = 'Team' # Keyword to recall after (in the pages) the information of the team
    )

# The key parameters are able to save the information in the sessions state that we are running

# We need to run the pages that we are recalling with the navigation, with this command
pg.run()