# Binary Search Implementation
>Algorithms are sequences of instructions or codes to accomplish a task
## Performance and Big O
 Big O describes a performance of an algorithm meaning is this algorithm going to scale well as the input grows 
### Time-complexity and space-complexity 
* **has time-complexity of O(log n)** - it's very fast because every time it narrows down our search by half
* **has Space Complexity of O(1)** - Constant space since it uses only a few pointers. 
* **why i used** - if there are 1M search items it would only take 19 operations for binary search to search the target whereas for  Linear Search that's not the case and if we have 1M items, it would take 1M guesses which is not efficient.

## 🛠️ Implementation Details
To use this algorithm, the input list **must be sorted**.
## LeetCode Verification: #704 Binary Search
>LeetCode Success Result(./leetcode result.png)
