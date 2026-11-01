uv run main_float_with_classes.py data/measurements_100k.txt \
 | python3 data/check.py data/measurements_100k.out
 
 uv run data/generate_measurements.py 10_000_000 -o measurements_10m.txt
 
 uv run main_float_with_classes.py data/measurements_10m.txt
 
 /usr/bin/time -p python3 main_float_with_classes_faster.py data/measurements_10m.txt
 
 uv run kernprof -l -v main_float_with_classes.py data/measurements_10m.txt

 
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
    

Second version(binary read):
Total time: 19.6039 s
File: main_float_with_classes.py
Function: process_file at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           @profile
     8                                           def process_file(path: str) -> dict[str, stats.StationStats]:
     9         1          1.0      1.0      0.0      final_dict: dict[bytes, stats.StationStats] = {}
    10         2         52.0     26.0      0.0      with open(path, "rb") as f:
    11  10000001    1953510.0      0.2     10.0          for line in f:
    12  10000000    2249560.0      0.2     11.5              station_bytes, _, temperature_read = line.partition(b";")
    13  10000000    2071280.0      0.2     10.6              temperature = float(temperature_read)
    14  10000000    1926988.0      0.2      9.8              check = final_dict.get(station_bytes)
    15  10000000    1565294.0      0.2      8.0              if check is None:
    16       411        429.0      1.0      0.0                  final_dict[station_bytes] = stats.StationStats(temperature)
    17                                                       else:
    18   9999589    9836751.0      1.0     50.2                  check.update(temperature)
    19         1          1.0      1.0      0.0      return final_dict
    

Third version(getting rid of update in main)

Total time: 16.8123 s
File: main_float_with_classes.py
Function: process_file at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           @profile
     8                                           def process_file(path: str) -> dict[str, stats.StationStats]:
     9         1          0.0      0.0      0.0      final_dict: dict[bytes, stats.StationStats] = {}
    10         2         64.0     32.0      0.0      with open(path, "rb") as f:
    11  10000001    1898362.0      0.2     11.3          for line in f:
    12  10000000    2333810.0      0.2     13.9              station_bytes, _, temperature_read = line.partition(b";")
    13  10000000    2201587.0      0.2     13.1              temperature = float(temperature_read)
    14  10000000    2049228.0      0.2     12.2              check = final_dict.get(station_bytes)
    15  10000000    1569470.0      0.2      9.3              if check is None:
    16       411        429.0      1.0      0.0                  final_dict[station_bytes] = stats.StationStats(temperature)
    17                                                       else:
    18   9999589    1622420.0      0.2      9.7                  if temperature < check._min:
    19      3903        583.0      0.1      0.0                      check._min = temperature
    20   9999589    1567507.0      0.2      9.3                  if temperature > check._max:
    21      3941        633.0      0.2      0.0                      check._max = temperature
    22   9999589    1786731.0      0.2     10.6                  check._sum += temperature
    23   9999589    1781462.0      0.2     10.6                  check._count += 1
    24         1          4.0      4.0      0.0      return final_dict
