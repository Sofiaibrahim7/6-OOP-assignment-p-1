# ⏳ Assignment: Make a Custom Class Iterable – Countdown

## 🎯 Objective
Create a class `Countdown` that takes a start number.  
Implement `__iter__()` and `__next__()` to make the object iterable in a for-loop, counting down to 0.

---

## ✅ Python Code (`app.py`)

```python
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Example usage
countdown = Countdown(5)

for number in countdown:
    print(number)

# ⏳ Assignment: Make a Custom Class Iterable – Countdown

## 🎯 Objective
Create a class `Countdown` that takes a start number.  
Implement `__iter__()` and `__next__()` to make the object iterable in a for-loop, counting down to 0.

---

## ✅ Python Code (`app.py`)

```python
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Example usage
countdown = Countdown(5)

for number in countdown:
    print(number)
🧠 Explanation
__iter__(): This method is required to make the class iterable. It returns the iterator object, which is the object itself in this case.

__next__(): This method defines the logic for iteration. It returns the next value and raises a StopIteration exception when the countdown reaches 0.

🖥️ Output

5
4
3
2
1