import csv

def save_schedule_csv(matches, filename="tournament_schedule.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Match No", "Team 1", "Team 2", "Date", "Venue"])
        for i, m in enumerate(matches, start=1):
            writer.writerow([i, m.team1.name, m.team2.name, m.date, m.venue])


def save_standings_csv(teams, filename="standings.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Team", "Points", "Wins", "Losses", "Draws"])
        for t in teams:
            writer.writerow([t.name, t.points, t.wins, t.losses, t.draws])