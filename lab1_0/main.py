"""Solution to the one billion rows problem."""
import sys

def mean_tenths(total: int, count: int) -> int:
    return (2 * total + count) // (2 * count)
    
def main() -> None:
    
    if len(sys.argv) != 2:
        print("usage: main.py <file>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            dict_of_stations: dict[str, list[int]] = {}
            for line in f:
                station, temperature_read = line[:-1].split(";")
                temperature = int(temperature_read.replace(".", ""))
                check = dict_of_stations.get(station)
                if check is None:
                    dict_of_stations[station] = [temperature, temperature, temperature, 1]
                else:
                    if temperature < check[0]: check[0] = temperature
                    if temperature > check[2]: check[2] = temperature
                    check[1] += temperature
                    check[3] += 1
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    for key in sorted(dict_of_stations):
        min, total, max, count = dict_of_stations[key]
        mean = mean_tenths(total, count)
        print(f"{key};{float(min/10)};{float(mean/10)};{float(max/10)}")
        
if __name__ == "__main__":
    main()