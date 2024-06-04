"""于2024-6-2测试通过"""
M = int(input())
submissions = []
for _ in range(M):
    team_name, problem, verdict = input().split(',')
    submissions.append((team_name, problem, verdict))

team_stats = {}
for team, problem, verdict in submissions:
    if team not in team_stats:
        team_stats[team] = [0, 0, {}]

    if problem not in team_stats[team][2] and verdict == 'yes':
        team_stats[team][0] += 1
        team_stats[team][2][problem] = True
    team_stats[team][1] += 1

sorted_teams = sorted(team_stats.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))

for i, (team, stats) in enumerate(sorted_teams[:12], start=1):
    print(i, team, stats[0], stats[1])