import random

players = [
    {'name': 'Mike', 'average': 10},
    {'name': 'Pete', 'average': 10},
    {'name': 'Britt', 'average': 10},
    {'name': 'Alex', 'average': 10},
    {'name': 'Dom', 'average': 9},
    {'name': 'Mikey', 'average': 9},
    {'name': 'Grace', 'average': 9},
    {'name': 'Gabby', 'average': 8},
    {'name': 'Tommy', 'average': 8},
    {'name': 'Matt', 'average': 7},
    {'name': 'Jay', 'average': 6},
    {'name': 'Brian', 'average': 4},
    {'name': 'Joe', 'average': 4},
    {'name': 'Gooch', 'average': 4},
    {'name': 'Kelly', 'average': 2},
    {'name': 'Jess', 'average': 2},
#    {'name': 'Christine', 'average': 1},
#    {'name': 'Dana', 'average': 1},
#    {'name': 'James', 'average': 1},
#    {'name': 'Jan', 'average': 1}
#    {'name': 'Reno', 'average': 1}
]

def create_even_teams(players, num_teams, max_players_per_team):
    # Shuffle players randomly
    random.shuffle(players)

    # Sort players by average in descending order
    sorted_players = sorted(players, key=lambda x: x['average'], reverse=True)

    # Initialize empty teams
    teams = [[] for _ in range(num_teams)]

    # Assign players with average 10 to each team
    average_10_players = [player for player in sorted_players if player['average'] == 10]
    for i, player in enumerate(average_10_players):
        team_index = i % num_teams
        teams[team_index].append(player)

    # Distribute remaining players to teams
    for player in sorted_players:
        if player in average_10_players:
            continue
        # Find the team with the lowest total average and add the player to it
        min_avg = float('inf')
        min_team = None
        for team in teams:
            if len(team) >= max_players_per_team:
                continue
            total_avg = sum(player['average'] for player in team)
            if total_avg < min_avg:
                min_avg = total_avg
                min_team = team

        min_team.append(player)

    return teams

def display_teams(teams):
    print("Evenly Matched Teams:")
    for i, team in enumerate(teams):
        print(f"Team {i + 1}:")
        for player in team:
            print(f"- {player['name']} (Average: {player['average']})")
        print()

# Example usage
num_teams = 4
max_players_per_team = 5
teams = create_even_teams(players, num_teams, max_players_per_team)
display_teams(teams)