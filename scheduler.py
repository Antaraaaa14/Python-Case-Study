from match_class import Match

def generate_schedule(teams):
    matches = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            matches.append(Match(teams[i], teams[j]))
    return matches