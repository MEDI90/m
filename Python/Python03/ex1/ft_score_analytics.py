import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            args = []
            for arg in sys.argv[1:]:
                args += [int(arg)]
            print(f"Scores processed: {args}")
            print(f"Total players: {len(args)}")
            print(f"Total score: {sum(args)}")
            print(f"Average score: {sum(args) / len(args)}")
            print(f"High score: {max(args)}")
            print(f"Low score: {min(args)}")
            print(f"Score range: {max(args) - min(args)}")
        except (ValueError, TypeError):
            print("please enter an valid inputs (only numeric values)")
