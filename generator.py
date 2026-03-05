import numpy as np
import pandas as pd

def create_dataset(n=30):

    np.random.seed(10)

    players = [f"Player_{i+1}" for i in range(n)]

    matches = np.random.randint(20,100,n)
    runs = np.random.randint(500,5000,n)
    balls = np.random.randint(400,4500,n)
    wickets = np.random.randint(0,150,n)
    catches = np.random.randint(0,60,n)

    strike_rate = (runs/balls)*100
    batting_avg = runs/matches

    df = pd.DataFrame({
        "Player":players,
        "Matches":matches,
        "Runs":runs,
        "Balls":balls,
        "StrikeRate":strike_rate,
        "BattingAverage":batting_avg,
        "Wickets":wickets,
        "Catches":catches
    })

    return df