## Algorithms tested
- Insertion Sort
- Merge Sort
- Quick Sort
- Python sorted()

## Data types
- sorted data
- reversed data
- random data

## Sizes
100, 1000, 10000, 100000

## Tools
Python, time.perf_counter, matplotlib

## How to run
pip install matplotlib
python sorting_benchmark.py

## Results
- Insertion is fast on sorted but very slow on reversed/random.
- Merge and Quick are O(n log n) and stable.
- Python sorted() is the fastest (Timsort).
