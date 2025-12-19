from team_class import Team
from scheduler import generate_schedule
from file_handler import save_schedule_csv, save_standings_csv

def main():
    teams = [
        Team("Team A"),
        Team("Team B"),
        Team("Team C"),
        Team("Team D")
    ]

    matches = generate_schedule(teams)

    print("\nFIXTURE LIST")
    for i, m in enumerate(matches, start=1):
        print(f"{i}. {m.team1.name} vs {m.team2.name}")

    for i, m in enumerate(matches, start=1):
        print(f"\nMatch {i}: {m.team1.name} vs {m.team2.name}")
        s1 = int(input(f"{m.team1.name} score: "))
        s2 = int(input(f"{m.team2.name} score: "))
        m.team1.update(s1, s2)
        m.team2.update(s2, s1)

    save_schedule_csv(matches)
    save_standings_csv(teams)

    print("\nFILES CREATED:")
    print("✔ tournament_schedule.csv")
    print("✔ standings.csv")

if __name__ == "__main__":
    main()