# team_class.py

class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0
        self.total_score = 0  # total points scored by this team
        self.matches_played = 0

    # This method updates scores after each match
    def update(self, scored, conceded):
        self.matches_played += 1
        self.total_score += scored

        if scored > conceded:
            self.wins += 1
            self.points += 2  # 2 points for win
        elif scored < conceded:
            self.losses += 1
            self.points += 0  # 0 points for loss
        else:
            self.draws += 1
            self.points += 1  # 1 point for draw