from generator import create_dataset
import insights as ci
def main():
    df = create_dataset(30)
    print("===== CRICKET DATASET =====\n")
    print(df)
    print("\n===== RUN STATISTICS =====")
    stats = ci.run_statistics(df)
    for k,v in stats.items():
        print(k,":",round(v,2))
    print("\n===== BEST BATSMAN =====")
    print(ci.best_batsman(df))
    print("\n===== BEST BOWLER =====")
    print(ci.best_bowler(df))
    print("\n===== ALL ROUNDER RANKING =====")
    ranked = ci.all_rounder_score(df)
    print(ranked[["Player","AllRounderScore"]].head(10))
    print("\n===== DREAM TEAM (TOP 11) =====")
    team = ci.select_dream_team(ranked)
    print(team[["Player","Runs","Wickets","AllRounderScore"]])
    print("\n===== HIGH STRIKE RATE PLAYERS =====")
    print(ci.high_strike_rate_players(df)[["Player","StrikeRate"]])
if __name__ == "__main__":
    main()