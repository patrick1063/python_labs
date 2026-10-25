uv run main_float_with_classes.py data/measurements_100k.txt \
 | python3 data/check.py data/measurements_100k.out
 
 uv run data/generate_measurements.py 10_000_000 -o measurements_10m.txt