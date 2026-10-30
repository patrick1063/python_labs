"""Solution to the one billion rows problem."""
import sys
import stats
from line_profiler import profile
LINE_PROFILE = 1

@profile
def process_file(path: str) -> dict[str, stats.StationStats]:
    final_dict: dict[bytes, stats.StationStats] = {}
    with open(path, "rb") as f:
        for line in f:
            station_bytes, _, temperature_read = line.partition(b";")
            temperature = float(temperature_read)
            check = final_dict.get(station_bytes)
            if check is None:
                final_dict[station_bytes] = stats.StationStats(temperature)
            else:
                check.update(temperature)
    return final_dict


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: main_float_with_classes.py <file>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    try:
        final_dict = process_file(path)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    for key in sorted(final_dict, key = lambda a: a.decode("utf-8")):
            print(f"{key.decode('utf-8')};{final_dict[key]}")


if __name__ == "__main__":
    main()