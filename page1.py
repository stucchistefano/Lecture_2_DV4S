import streamlit as st
import pandas as pd
import numpy as np

st.title("Lecture 2 - Streamlit Basics\n")

# Metrics
# Metrics allows to display a metric with specific font and maybe with also a variation
# with a graphical component like an arrow that is going down or up if the performances is going down or up
st.subheader("Metric")
st.metric(label="Number of Assists", value="25", delta="+6")
# "delta" is the parameter that gives info about past values, to track the changes of the value;
# the value could be passed by positional ways or by value, like did here
st.metric(label="Number of Goals", value="13", delta="-5")
# It is related to text, and there are aslo some different graphical elements related to metrics


# Dataframe
# Particularly used when we need and have to deal with tables, which could be displayed
# or changed in some elements. We could use and integrate the Pandas dataframe and library
st.subheader(":blue[Dataframe]")
# We need to define some data to put into the dataframe
data={
    "Player's Name": ["Pelè", "Maradona", "Baggio"],
    "Goals": [13,26,32],
    "Team": ["Santos", "Napoli", "Internazionale"]
}
# It is a dictionary, that could be converted into a dataframe of Pandas (import Pandas above)
df = pd.DataFrame(data)

# We can display the dataframe by using the streamlit method "dataframe()"
st.write("Dataframe")
st.dataframe(df) # Display the dataframe in an INTERACTIVE WAY
# We could display the dataframe NOT in an interactive way, with the "table()" method
st.write("Static Table")
st.table(df) # Display the dataframe as a static table (not interactable of copiable)

# The look of the application maybe is not the one that we will obtain on the browser on
# which we will open the web app

# Data
st.subheader("Data Generation")
# We need data, and thus we could generate some random data (then we will use some data from Google drive, files or online databases)
# To generate random data, we use numpy and this methods to generate random integer numbers from 4 to 21
n_goals = np.random.randint(4,21,size=(38,3)) # The size tells us to generate 38 values for 3 players
player_names=["Pelè", "Fonseca", "Baggio"]

# We can translate them into dataframe these data
df2 = pd.DataFrame(n_goals, columns=player_names)
# Check of the dataframe plotting it
st.dataframe(df2)


# Charts
# We will see some and more and more charts, which could be realised with libraries
# used in Python (for the specific libraries (like Altair) charts we need to import them correctly)

# Line Charts
st.subheader("Line Charts")
# We could use build-in methods to implement line charts, which are the ones of Altair mostly
# "x" is the column name and values related to the x axes, in opposition to "y"
# The color could be defined with strings as hex codes, or has integer numbers for the RGB representation (every tuple could be associated to a specific color)
# "width" and "height" are related to width and height of the chart
# "use_container_width" is the dimension of the container and component/window into which the graph is represented

# Plot of the dataframe as line chart
st.line_chart(data=df2)


# Area Charts
st.subheader("Area Charts")
st.area_chart(df2)
# We have already some interactions with the chart, because we could zoom-in and out, or to scroll and move, since they are buil-in on Altair


# Bar Charts
# It is another representation of data related to specific classes and categories
st.subheader("Bar Charts")
st.bar_chart(df2)
# In this build-in method we have that the bars are stacked, thus we have that they are not
# overlapped, but are placed on the same line/column (which is a better representation for this representation)
# The command and variables are the same of before


# Scatter Charts
# It is the one that allows to represent data with two variables/attributes, so related to 2D representation, with two variables on the axes

# Data
# We need to define 2D data, not like the ones above, which have only one numerical attribute
# We need to generate float numbers to represent the positions of the player on the field while scoring into each game of the season (so for 38 times)
n_matches = 38
x_coord = np.random.rand(n_matches)*100
y_coord = np.random.rand(n_matches)*100
goal_values = np.random.randint(1,15,size=n_matches)
# To have different colour
goal_colors = np.random.rand(n_matches, 3) # To get a numpy array related to RGB, which are three colours and must be generated in their numerical value
# We need to generate a list of tuples from a one dimensional array above obtained
# We could use a for loop, to convert a line of the goal_colors arrays values into a tuple of three numerical values (we obtain a list of tuples as final result)
goal_colors_lot = [tuple(c) for c in goal_colors]


# We could define the dataframe and we could start from the dictionary
goal_data = {
    "X": x_coord,
    "Y": y_coord,
    "Goals": goal_values,
    "Colors": goal_colors_lot
}

# Plot generated
st.write("Data Generated")
df3 = pd.DataFrame(goal_data)
# Plot and check of the dataframe created
st.dataframe(df3)

# Chart representation
st.subheader("Scatter Charts")
st.scatter_chart(goal_data, x="X", y="Y", size="Goals", color="Colors")


# Map (Charts)
# We need to generate the floating points that are correctly and effectively the coordinates of the player on the field
# Data Generation
n_pos = 100
# Latitude of Lecco
latitude = np.random.uniform(45.8, 45.9, n_pos) # To have a "uniform" and not "normal" distribution of random data
# Longitude of Lecco
longitude = np.random.uniform(9.35, 9.45, n_pos) # This is the definition of the position with float values, not the degrees
location = {
    "lat": latitude,
    "lon": longitude
}
# Conversion in dataframe
df4 = pd.DataFrame(location)
# Plot and Check of the dataframe
st.write("Data Generated")
st.dataframe(df4)

# Map Chart
st.subheader("Map Chart") # Without the need of have a token, because already into the PyDeck
st.map(df4)


# Assignment 3
st.title("Training/Assignment - At Home\n")

# Generate Dataset of 5 Football Players
p = ["Mateo Retegui", "Lautaro Martinez", "Romelu Lukaku", "Ademola Lookman", "Marcus Thuram"]
g = np.random.randint(10, 30, size=5) # Random integer for 5 players
a = np.random.randint(10, 40, size=5)
m = np.random.randint(10, 38, size=5)
avg_d = np.random.rand(5)*20 # 5 values as players of runned distance
p_acc = np.random.rand(5)*100 # 5 percentual values of pass accuracy

d = {
    "Player Name": p,
    "Goals Scored": g,
    "Assists Made": a,
    "Matches Played": m,
    "Average Distance Covered [km]": avg_d,
    "Pass Accuracy [%]": p_acc
}

df_train = pd.DataFrame(d)

# Show created dataframe
st.subheader("Generated DataFrame")
st.dataframe(df_train)


# Charts and Interactive Elements
st.subheader("Charts and Interactive Elements")

# Goals
st.write("Goals")
st.bar_chart(df_train.set_index("Player Name")["Goals Scored"])

# Matches and Assists
st.write("Matches and Assists")
# Extraction of only interesting data in new dataframe
match_assist_data = df_train[["Player Name", "Matches Played", "Assists Made"]]
st.line_chart(match_assist_data.set_index("Player Name"))

# Accuracy and Distance Covered
st.write("Pass Accuracy and Distance Covered")
# Extraction of only interesting data in new dataframe
acc_dist_data = df_train[["Player Name", "Pass Accuracy [%]", "Average Distance Covered [km]"]]
st.area_chart(acc_dist_data.set_index("Player Name"))

# Interactive Element (Select Box)
st.write("Select a Player to View his Individual Stats")
selected_player = st.selectbox("Choose a Player (between the proposed ones)", df_train["Player Name"])
# Display Selected Player's Stats
index_selected_player = df_train["Player Name"] == selected_player # So extraction of the index (for all the columns) of the only player selected
# Creation of a new dataframe with only selected player's stats
player_stats = df_train[index_selected_player]
# Plot/Writing of the Stats of the selected player
st.write(player_stats.set_index("Player Name").T) # This command allows to report the stats on rows, no more on columns, as done in the after plotted dataframe

# Plot of its stats as a dataframe
st.write("Selected Player's Stats DataFrame")
st.dataframe(player_stats)

# Plot in a bar chart of all the stats
st.write("Selected Player Stats")
st.bar_chart(player_stats.T)




# Lecture 3
st.title("Lecture 3 - Streamlit Basics")
st.subheader("Data Visualization & Additional Components/Themes")

# Session State
st.subheader("Session State")
# Shared variables between different pages
# We can use the Session State, to share some info, here defined
# Session State (allows to share variables associating them a "key" that could be recalled)
st.session_state['Player'] = "Diego"
st.session_state['Goals'] = 35
# These variables could be available during the whole project, and could be recalled in this way
st.write("The name of the player is: ", st.session_state['Player'])
# Later we will explain how to recall different variables in different pages of the project


# Alphanumerical Information (errors, warnings, info or success messages)
# Error message
st.subheader("Error Message")
st.error("**This is an error messagge!**")
# Warning message
st.subheader("Warning Message")
st.warning("_This is a warning message!_")
# Success message
st.subheader("Success Message")
st.success("This is a success message")
# Info Message/Function
st.subheader("Info Message")
st.info("This is an info message")
# We could put also some icons and emoji into the text of our message, like the fire, or the caution alarm and light


# Waiting and Computation Time reporting visual encoding
import time as t
# Progress Bar
st.subheader("Progress Bar")
progress_bar = st.progress(0) # We can start from 0 and then we will implement a for loop to scroll 100 values
# Its value is an integer or float, and it is plotted in its changing
for i in range(101):
    t.sleep(0.005)
    progress_bar.progress(i) # We are using the object (progress_bar) of before, updating its value
    # (Before there is the) Introduction of a temporal delay between one value and the other (otherwise too fast) (with time library)
st.success("**Computation is complete!**")

# Spinner (Which is a rotating loading "wheel" that mimic the loading function)
st.subheader("Spinner")
# We can have a string, which is updated during the loading, with which we could inform the user that he has to wait (but that does not know in which part of the computation is now)
# Definition of a proper part of code with "with"
with st.spinner("You have to wait!", show_time=True): # We do not know in which part of the computation time we are now, but we will only know that we are "computing"
    t.sleep(2) # Wait for 2 seconds (with "show_time" we will present the computational time for which we are computing)
st.success("**Task was completed!**")


# Layout tools
# We could rearrange the layout with sidebars, columns 
# (which allows to define the containers (fo the same dimensions) in which we should put graphs), 
# or tabs (which allows to push on them and to switch from one element to others) 
# or expanders (which allows the interaction of the user by pushing on the expanders to have more data when clicking on it)
# Sidebar
st.subheader("Sidebar")
# We will define the Sidebar as an object, and them as an HTML