import sys

def main() -> None:
    print("=== Player Score Analytics ===")

    score = []
    nbr = len(sys.argv)
    i = 1
    while (i < nbr):
        try:
            score.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    if not score:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_player = nbr - 1
    Total_score = sum(score)
    low_score = min(score)
    high_score = max(score)

    print(f"Total players: {total_player}")
    print(f"Total score: {Total_score}")
    print(f"Average score: {Total_score / total_player}")
    print(f"High score: {high_score}")
    print(f"low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
