"""Solution to the one billion rows problem."""
import sys
import stats


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: main_float_with_classes.py <file>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, "r", encoding="utf-8") as f:
            final_dict: dict[str, stats.StationStats] = {}
            for line in f:
                station, temperature_read = line.rstrip("\n").split(";")
                temperature = float(temperature_read)
                check = final_dict.get(station)
                if check is None:
                    final_dict[station] = stats.StationStats(temperature)
                else:
                    check.update(temperature)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    for key in sorted(final_dict):
        print(f"{key};{final_dict[key]}")


if __name__ == "__main__":
    main()