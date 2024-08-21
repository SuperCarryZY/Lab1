# CMPS 2200 Recitation 01
## Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `recitation-01.md` here for easier grading.

- **4)** Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 
- linear_search:The worst key will be the last one in the list, because all list elements will be searched.
- binary_search:The worst case occurs when every time after calculating mid, the key is always on the left or right of mid, until the range is reduced to only one element. In the worst case, a binary search requires log2 (total number of elements) comparisons until the range is reduced to one element. Each comparison in this process will recalculate mid until it is finally determined whether the key exists.

- **5)** Describe the best case input value of `key` for `linear_search`? for `binary_search`? 
- linear_search:The best key is list[0]==key.
- binary_search:The best key is mid==key.
- **8)** Call `print_results(compare_search())` and paste the results here:
- yanzhu@Yans-MBP yanzhu % python3 main.py

|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.001 |    0.003 |
|      100 |    0.002 |    0.002 |
|     1000 |    0.027 |    0.002 |
|    10000 |    0.261 |    0.003 |
|   100000 |    2.572 |    0.003 |
|  1000000 |   21.535 |    0.009 |
| 10000000 |  205.955 |    0.012 |
- **9)** Do the theoretical running times match your empirical results?

- **10a)** What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? 

- **10b)** For binary search? 

- **10c)** For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? You may assume that your sorting algorithm runs in $O(n \lg n)$ time.

   