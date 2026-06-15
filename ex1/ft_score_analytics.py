#! /usr/bin/python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...\n")
    else:
        data = []
        for i in range(1, len(sys.argv)):
            try:
                data.append(int(sys.argv[i]))
            except Exception:
                print(f"Invalid parameter: {sys.argv[i]}")
        print(f"Scores processed: {data}")
        if (len(data) > 0):
            print(f"Total players: {len(data)}")
            print(f"Total score: {sum(data)}")
            print(f"Average score: {sum(data) / len(data)}")
            print(f"High score: {max(data)}")
            print(f"Low score: {min(data)}")
            print(f"Score range: {max(data) - min(data)}\n")
