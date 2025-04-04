import streamlit as st
import pandas as pd

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
st.write("Table")
st.table(df) # Display the dataframe as a static table (not interactable of copiable)