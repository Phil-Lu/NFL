# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import re
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data_type = {
    # GameId - a unique game identifier
    'GameId': str,
    # PlayId - a unique play identifier
    'PlayId': str,
    # Team - home or away
    'Team': 'category',
    # X - player position along the long axis of the field. See figure below.
    'X': float,
    # Y - player position along the short axis of the field. See figure below.
    'Y': float,
    # S - speed in yards/second
    'S': float,
    # A - acceleration in yards/second^2
    'A': float,
    # Dis - distance traveled from prior time point, in yards
    'Dis': float,
    # Orientation - orientation of player (deg)
    'Orientation': float,
    # Dir - angle of player motion (deg)
    'Dir': float,
    # NflId - a unique identifier of the player
    'NflId': str,
    # DisplayName - player's name
    'DisplayName': str,
    # JerseyNumber - jersey number
    'JerseyNumber': str,
    # Season - year of the season
    'Season': int,
    # YardLine - the yard line of the line of scrimmage
    'YardLine': int,
    # Quarter - game quarter (1-5, 5 == overtime)
    'Quarter': int,
    # GameClock - time on the game clock - HH:MM:SS
    'GameClock': str,
    # PossessionTeam - team with possession
    'PossessionTeam': str,
    # Down - the down (1-4)
    'Down': int,
    # Distance - yards needed for a first down
    'Distance': int,
    # FieldPosition - which side of the field the play is happening on
    'FieldPosition': 'category',
    # HomeScoreBeforePlay - home team score before play started
    'HomeScoreBeforePlay': int,
    # VisitorScoreBeforePlay - visitor team score before play started
    'VisitorScoreBeforePlay': int,
    # NflIdRusher - the NflId of the rushing player
    'NflIdRusher': str,
    # OffenseFormation - offense formation
    'OffenseFormation': str,
    # OffensePersonnel - offensive team positional grouping
    'OffensePersonnel': str,
    # DefendersInTheBox - number of defenders lined up near the line of scrimmage, spanning the width of the offensive line
    # 'DefendersInTheBox': str,
    # DefensePersonnel - defensive team positional grouping
    'DefensePersonnel': str,
    # PlayDirection - direction the play is headed
    'PlayDirection': 'category',
    # TimeHandoff - UTC time of the handoff
    'TimeHandoff': str,
    # TimeSnap - UTC time of the snap
    'TimeSnap': str,
    # Yards - the yardage gained on the play (you are predicting this)
    'Yards': int,
    # PlayerHeight - player height (ft-in)
    # 'PlayerHeight': str,
    # PlayerWeight - player weight (lbs)
    'PlayerWeight': int,
    # PlayerBirthDate - birth date (mm/dd/yyyy)
    'PlayerBirthDate': str,
    # PlayerCollegeName - where the player attended college
    'PlayerCollegeName': str,
    'Position': 'category',
    # HomeTeamAbbr - home team abbreviation
    'HomeTeamAbbr': str,
    # VisitorTeamAbbr - visitor team abbreviation
    'VisitorTeamAbbr': str,
    # Week - week into the season
    'Week': int,
    # Stadium - stadium where the game is being played
    'Stadium': str,
    # Location - city where the game is being player
    'Location': str,
    # StadiumType - description of the stadium environment
    'StadiumType': 'category',
    # Turf - description of the field surface
    'Turf': 'category',
    # GameWeather - description of the game weather
    'GameWeather': 'category',
    # Humidity - humidity
    # 'Humidity': int,
    # WindSpeed - wind speed in miles/hour
    # 'WindSpeed': int,
    # WindDirection - wind direction
    'WindDirection': str
}


def try_parsing_date(text):
    for fmt in ('%Y-%m-%dT%H:%M:%S.%fZ', '%m/%d/%Y', "%H:%M:%S"):
        try:
            if fmt == "%H:%M:%S":
                return pd.datetime.strptime(text, fmt).time()
            else:
                return pd.datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')


def convert_windspeed(x):
    if x not in ('', 'SSW', 'E', 'SE', 'Calm'):
        return x[0:2]
    else:
        return x


data = pd.read_csv("../Data/Source/train.csv", header=0, delimiter=',',
                   dtype=data_type, date_parser=try_parsing_date,
                   parse_dates=['TimeHandoff', 'PlayerBirthDate', 'TimeSnap', 'GameClock'],
                   converters={'Temperature': lambda x: float(x) if x not in ('NA', '') else np.nan,
                               'DefendersInTheBox': lambda x: float(x) if x not in ('NA', '') else np.nan,
                               'Humidity': lambda x: float(x) if x not in ('NA', '') else np.nan,
                               'WindSpeed': convert_windspeed,
                               'PlayerHeight': lambda x: int(x[0:x.find('-')])*12 + int(x[x.find('-') + 1])
                               }
                   # ,skiprows=range(1, 1000)
                   # ,nrows=50000
                   )


# for some games, e.g., GameId = 2017100100, the WindSpeed/Direct order is reversed
for index, row in data.iterrows():
    if row['WindSpeed'] in ('SSW', 'E', 'SE', 'Calm'):
        data.loc[index, ['WindSpeed', 'WindDirection']] = data.loc[index, ['WindDirection', 'WindSpeed']].values

data.to_csv('../Data/Datamart/train_clean.csv', index=None, header=True)