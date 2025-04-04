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
