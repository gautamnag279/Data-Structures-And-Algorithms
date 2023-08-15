Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

```
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}

Output: 2 4

Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
```