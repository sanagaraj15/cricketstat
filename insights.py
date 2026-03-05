import numpy as np
def run_statistics(df):

    stats = {
        "Total Runs": np.sum(df["Runs"]),
        "Average Runs": np.mean(df["Runs"]),
        "Max Runs": np.max(df["Runs"]),
        "Min Runs": np.min(df["Runs"]),
        "Run Std Dev": np.std(df["Runs"])
    }
    return stats
def best_batsman(df):
    return df.loc[df["Runs"].idxmax()]
def best_bowler(df):
    return df.loc[df["Wickets"].idxmax()]
def all_rounder_score(df):
    score = (df["Runs"] * 0.6) + (df["Wickets"] * 25) + (df["Catches"] * 10)
    df["AllRounderScore"] = score
    return df.sort_values(by="AllRounderScore", ascending=False)
def select_dream_team(df):
    return df.head(11)
def high_strike_rate_players(df):
    return df[df["StrikeRate"] > 120]