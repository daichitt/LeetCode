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
---

## Array Operations Cheat Sheet

| Operation       | Time Complexity | Description                    |
| --------------- | --------------- | ------------------------------ |
| Access          | O(1)            | Get element at index           |
| Search          | O(n)            | Find element in unsorted array |
| Insert (end)    | O(1)            | Add element at end             |
| Insert (middle) | O(n)            | Add element in middle          |
| Delete (end)    | O(1)            | Remove last element            |
| Delete (middle) | O(n)            | Remove element from middle     |
| Push/Pop        | O(1)            | Add/remove at end              |
| Shift/Unshift   | O(n)            | Add/remove at beginning        |

---

## Common Python Array Methods

| Method      | Description              | Time Complexity |
| ----------- | ------------------------ | --------------- |
| `append()`  | Add element to end       | O(1)            |
| `pop()`     | Remove last element      | O(1)            |
| `insert()`  | Insert at specific index | O(n)            |
| `remove()`  | Remove first occurrence  | O(n)            |
| `index()`   | Find index of element    | O(n)            |
| `len()`     | Get array length         | O(1)            |
| `sort()`    | Sort array               | O(n log n)      |
| `reverse()` | Reverse array            | O(n)            |


```
