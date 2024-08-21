# CMPS 2200 Recitation 01
## Answers

**Name:**_______Yan Zhu_______  
**Name:**_______Yongbo Chen_______

Place all written answers from `recitation-01.md` here for easier grading.

- **4)** Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 
  - **linear_search**:The worst case input will be when the key is the last one in the list, and all elements will be searched. If there are n inputs, the worst time required is O(n). 
  - **binary_search**:The worst case occurs when every time after calculating mid, the key is always on the left or right of mid, until the range is reduced to only one element. In the worst case, a binary search requires log2 (total number of elements) comparisons until the range is reduced to one element. Each comparison in this process will recalculate mid until it is finally determined whether the key exists.If there are n inputs, the worst time required is O(log2(n)) or O(logn).  

  
- **5)** Describe the best case input value of `key` for `linear_search`? for `binary_search`? 
  - **linear_search**:The best case is when the key at the first place, which means **list[0] == key**. Therefore, the best case of time cost should be O(1).  
  - **binary_search**:The best case is when **mid == key**, which means when the key is at the middle place. Since binary search starts by checking the middle element, so the best case of time cose for binary_search is O(1).  


- **8)** Call `print_results(compare_search())` and paste the results here:
  - The input is shown as below:  
  yanzhu@Yans-MBP yanzhu % python3 main.py

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
  - **Linear Search**:  
  Theoretically, the time complexity of linear search is 
  O(𝑛). Our test results show that as n increases, the time taken by linear search also increases linearly, which is consistent with the theoretical expectation.

  - **Binary Search**:  
  Theoretically, the time complexity of binary search is O(logn). Our results show that the time taken by binary search increase logarithmically with the size of the input list, which is also consistent with the theoretical expectation.

  - Overall the theoretical running times match our empirical results. Besides, it should be mentioned that on small data sets, algorithm and system performance may have a greater impact on running time, make our result vary under different runs.


- **10a)** What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search?
  - According to **4)**, the worst-case complexity of searching a list of $n$ elements using linear-search under one-time running costs O(n). Therefore, the worst-case complexity of searching a list of $n$ elements $k$ times using linear search takes **O(k*n)**.
  

- **10b)** For binary search? 
  - According to **4)**, the worst-case complexity of searching a list of $n$ elements using binary search under one-time running costs O(n). Therefore, the worst-case complexity of searching a list of $n$ elements $k$ times using binary search takes **O(k*log n)**.


- **10c)** For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? You may assume that your sorting algorithm runs in $O(n\log n)$ time.  
  - The worst case of time cost to search n elements using linear search without sorting takes O(n*k).
  - The worst case of time cost to search n elements by sorting first and use binary search takes ($O(n\log n)$ + $$O(k\log n)$$), which is $O((n+k)\log n)$.
  - To determine what values of $k$ is more efficient to first sort and then use binary search versus just using linear search without sorting, we need to compare in the worst case when $O((n+k)\log n)$ takes less time than $$O(nk)$$. Therefore, the calculation should be $$O((n+k)\log n) < O(nk)$$, which means $$(n+k)logn<nk$$. The calculation result is follow:  <div align="center"><img src="https://latex.codecogs.com/svg.image?&space;k>\frac{nlogn}{n-logn}"/></div>
  - **Overall, when $k$ is larger than (nlogn)/(n-logn), it will be more efficient to first sort and then use binary search versus just using linear search without sorting**.



