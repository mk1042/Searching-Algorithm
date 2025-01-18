
# Combined Search Algorithms: Binary Search and Linear Search

## Purpose of the Code
This project combines two essential search algorithms, Binary Search and Linear Search, into a single script. The purpose is to compare their efficiencies and understand their practical applications in different scenarios.

## How to Run the Program
1. Clone this repository:
   ```
   git clone https://github.com/your-username/Search-Algorithms.git
   ```
2. Navigate to the project directory and run the script:
   ```
   python combined_search.py
   ```

## Features
- **Binary Search:** Efficient for sorted arrays with a time complexity of O(log n).
- **Linear Search:** Simple algorithm with a time complexity of O(n), suitable for unsorted data.

## Time Complexity
### Binary Search
- **Best Case:** O(1) (Target is at the middle of the array)
- **Worst Case:** O(log n) (Target is not present in the array)

### Linear Search
- **Best Case:** O(1) (Target is the first element)
- **Worst Case:** O(n) (Target is not present in the array)

## Example Output
For the input array `[1, 3, 5, 7, 9, 11, 13, 15]` and target `7`:
```
Using Binary Search:
Target 7 found at index 3 using Binary Search.

Using Linear Search:
Target 7 found at index 3 using Linear Search.
```

## Learning Outcome
This project demonstrates how to implement and compare search algorithms in Python, providing valuable insights into their use cases and efficiencies.
