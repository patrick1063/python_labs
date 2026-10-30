uv run main_float_with_classes.py data/measurements_100k.txt \
 | python3 data/check.py data/measurements_100k.out
 
 uv run data/generate_measurements.py 10_000_000 -o measurements_10m.txt
 
 uv run main_float_with_classes.py data/measurements_10m.txt
 
 /usr/bin/time -p python3 main_float_with_classes_faster.py data/measurements_10m.txt
 
 
 First version
 
 Total time: 20.0318 s
File: main_float_with_classes.py
Function: process_file at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           @profile
     8                                           def process_file(path: str) -> dict[str, stats.StationStats]:
     9         1          0.0      0.0      0.0      final_dict: dict[str, stats.StationStats] = {}
    10         2         44.0     22.0      0.0      with open(path, "r", encoding="utf-8") as f:
    11  10000001    2085139.0      0.2     10.4          for line in f:
    12  10000000    2619681.0      0.3     13.1              station, temperature_read = line.rstrip("\n").split(";")
    13  10000000    2081770.0      0.2     10.4              temperature = float(temperature_read)
    14  10000000    1871066.0      0.2      9.3              check = final_dict.get(station)
    15  10000000    1801872.0      0.2      9.0              if check is None:
    16       411        429.0      1.0      0.0                  final_dict[station] = stats.StationStats(temperature)
    17                                                       else:
    18   9999589    9571766.0      1.0     47.8                  check.update(temperature)
    19         1          1.0      1.0      0.0      return final_dict
    
