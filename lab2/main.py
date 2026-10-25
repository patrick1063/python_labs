"""Solution to the one billion rows problem."""
import sys
import time

def mean_tenths(total: int, count: int) -> int:
    return (2 * total + count) // (2 * count)
    
def main() -> None:
    
    if len(sys.argv) != 2:
        print("usage: main.py <file>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, "r", encoding="utf-8") as f:
            final_dict: dict[str, list[int]] = {}
            making_dict_start_time = time.perf_counter()
            for line in f:
                station, temperature_read = line[:-1].split(";")
                temperature = int(float(temperature_read) * 10)
                check = final_dict.get(station)
                if check is None:
                    final_dict[station] = [temperature, temperature, temperature, 1]
                else:
                    if temperature < check[0]: check[0] = temperature
                    if temperature > check[2]: check[2] = temperature
                    check[1] += temperature
                    check[3] += 1
            making_dict_time = time.perf_counter() - making_dict_start_time
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
	
    sorting_dict_start_time = time.perf_counter()
    sorted_dict_keys = sorted(final_dict)
    sorting_dict_time = time.perf_counter() - sorting_dict_start_time
    output_start_time = time.perf_counter()
    for key in sorted_dict_keys:
        mn, total, mx, cnt = final_dict[key]
        mean = mean_tenths(total, cnt)
        print(f"{key};{float(mn/10)};{float(mean/10)};{float(mx/10)}")
    output_time = time.perf_counter() - output_start_time
    print(f"output_time = {output_time}, sorting_dict_time = {sorting_dict_time}, making_dict_time = {making_dict_time}")

if __name__ == "__main__":
    main()