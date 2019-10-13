# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data_type = {
# GameId - a unique game identifier
    'GameId': 'object',
# PlayId - a unique play identifier
    'PlayId': 'object',
# Team - home or away
    'Team': 'category',
# X - player position along the long axis of the field. See figure below.
    'X': 'float64',
# Y - player position along the short axis of the field. See figure below.
    'Y': 'float64',
# S - speed in yards/second
    'S': 'float64',
# A - acceleration in yards/second^2
    'A': 'float64',
# Dis - distance traveled from prior time point, in yards
    'Dis': 'float64',
# Orientation - orientation of player (deg)
    'Orientation': 'float64',
# Dir - angle of player motion (deg)
    'Dir': 'float64',
# NflId - a unique identifier of the player
# DisplayName - player's name
# JerseyNumber - jersey number
# Season - year of the season
# YardLine - the yard line of the line of scrimmage
# Quarter - game quarter (1-5, 5 == overtime)
# GameClock - time on the game clock
# PossessionTeam - team with possession
# Down - the down (1-4)
# Distance - yards needed for a first down
# FieldPosition - which side of the field the play is happening on
# HomeScoreBeforePlay - home team score before play started
# VisitorScoreBeforePlay - visitor team score before play started
# NflIdRusher - the NflId of the rushing player
# OffenseFormation - offense formation
# OffensePersonnel - offensive team positional grouping
# DefendersInTheBox - number of defenders lined up near the line of scrimmage, spanning the width of the offensive line
# DefensePersonnel - defensive team positional grouping
# PlayDirection - direction the play is headed
# TimeHandoff - UTC time of the handoff
# TimeSnap - UTC time of the snap
# Yards - the yardage gained on the play (you are predicting this)
# PlayerHeight - player height (ft-in)
# PlayerWeight - player weight (lbs)
# PlayerBirthDate - birth date (mm/dd/yyyy)
# PlayerCollegeName - where the player attended college
# HomeTeamAbbr - home team abbreviation
# VisitorTeamAbbr - visitor team abbreviation
# Week - week into the season
# Stadium - stadium where the game is being played
# Location - city where the game is being player
# StadiumType - description of the stadium environment
# Turf - description of the field surface
# GameWeather - description of the game weather
# Temperature - temperature (deg F)
# Humidity - humidity
# WindSpeed - wind speed in miles/hour
# WindDirection - wind direction
}


data = pd.read_csv("../Data/Source/train.csv", dtype=data_type)
# Preview the first 5 lines of the loaded data
data.head()