def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players_data = [
        {"name": "alice", "score": 2300, "status": "active",
         "achievements": ["first_kill", "level_10", "boss_slayer",
                          "speed_demon", "collector"], "region": "north"},
        {"name": "bob", "score": 1800, "status": "active",
         "achievements": ["first_kill", "treasure_hunter",
                          "survivor"], "region": "east"},
        {"name": "charlie", "score": 2150, "status": "active",
         "achievements": ["level_10", "boss_slayer",
                          "pacifist", "explorer"], "region": "central"},
        {"name": "diana", "score": 2050, "status": "inactive",
         "achievements": ["first_kill", "explorer"], "region": "north"}
    ]

    print("=== List Comprehension Examples ===")
    high_scorers = [p['name'] for p in players_data if p['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p['score'] * 2 for p in players_data]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p['name'] for p in players_data
                      if p['status'] == 'active']
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")
    player_scores = {p['name']: p['score'] for p in players_data}
    print(f"Player scores: {player_scores}")

    categories = ['high', 'medium', 'low']
    score_categories = {
        cat: len([p for p in players_data if
                  (cat == 'high' and p['score'] >= 2000) or
                  (cat == 'medium' and 1000 <= p['score'] < 2000) or
                  (cat == 'low' and p['score'] < 1000)])
        for cat in categories
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p['name']: len(
        p['achievements']) for p in players_data}
    print(f"Achievement counts: {achievement_counts}\n")

    print("=== Set Comprehension Examples ===")
    unique_players = {p['name'] for p in players_data}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach for p in players_data for ach in p['achievements']}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p['region']
                      for p in players_data if p['status'] == 'active'}
    print(f"Active regions: {active_regions}\n")

    print("=== Combined Analysis ===")
    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    avg_score = sum([p['score'] for p in players_data]) / total_players
    print(f"Average score: {avg_score}")

    top_score = max([p['score'] for p in players_data])
    top_performer = [p for p in players_data if p['score'] == top_score][0]

    top_name = top_performer['name']
    top_ach_count = len(top_performer['achievements'])
    print(
        f"Top performer: {top_name} ({top_score} points, "
        f"{top_ach_count} achievements)")


if __name__ == "__main__":
    main()
