# Python Array Cheat Sheet

## Characteristics

### Pros
- Store data next to each other in memory
- Fast access to next data via index
- O(1) time complexity for deletion/insertion at the end

### Cons
- O(n) time complexity for deletion/insertion in the middle
- Requires shifting indices for each value when modifying middle elements

### Summary
- Array is a continuous area of memory
- Constant time access to any element
- Constant time to add/remove at the end
- Linear time to add/remove at the middle/beginning

---

## Example

```python
arr = [1, 2, 3, 4]
arr.append(5)        # [1, 2, 3, 4, 5]
arr.pop()            # [1, 2, 3, 4]
arr.insert(2, 99)    # [1, 2, 99, 3, 4]
arr.remove(99)       # [1, 2, 3, 4]