"""
CMPS 6610  Lab 1
Group: Yan Zhu and Yongbo Chen
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
    """ done. """
    for i,v in enumerate(mylist):
        if v == key:
            return i
    return -1

def test_linear_search():
    """ done. """
    assert linear_search([1,2,3,4,5], 5) == 4
    assert linear_search([1,2,3,4,5], 1) == 0
    assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
    return _binary_search(mylist, key, 0, len(mylist)-1)


def binary_search(mylist, key):
    return _binary_search(mylist, key, 0, len(mylist) - 1)

def _binary_search(mylist, key, left, right):
 
    if left > right:
        return -1  
    
    mid = (left + right) // 2
    
    if mylist[mid] == key:
        return mid 
    elif mylist[mid] < key:
        return _binary_search(mylist, key, mid + 1, right)  
    else:
        return _binary_search(mylist, key, left, mid - 1)  


def test_binary_search():
    assert binary_search([1,2,3,4,5], 5) == 4
    assert binary_search([1,2,3,4,5], 1) == 0
    assert binary_search([1,2,3,4,5], 6) == -1
    assert binary_search([1,2,3,4,5], 7) == -1
    assert binary_search([1,2,3,4,5], 2) == 1



def time_search(search_fn, mylist, key):
    start=time.time()
    search_fn(mylist,key)
    end=time.time()
    fn_time=(end-start)*1000
    return fn_time
    

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
    key = -1
    results = []
    for n in sizes:  
        n = int(n)  
        mylist = list(range(n))  
        linear_time = time_search(linear_search, mylist, key)  
        binary_time = time_search(binary_search, mylist, key)
        results.append((n, linear_time, binary_time)) 
    return results
     


def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
        headers=['n', 'linear', 'binary'],
        floatfmt=".3f",
        tablefmt="github"))


def test_compare_search():
    res = compare_search(sizes=[10, 100])
    print(res)
    assert res[0][0] == 10
    assert res[1][0] == 100
    assert res[0][1] < 1
    assert res[1][1] < 1

print_results(compare_search())