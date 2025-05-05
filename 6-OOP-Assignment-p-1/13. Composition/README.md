# 🚗 Assignment: Composition – Car and Engine

## 🎯 Objective
Create a class `Engine` and a class `Car`. Use **composition** by passing an `Engine` object to the `Car` class during initialization. Access a method of the `Engine` class via the `Car` class.

---

## ✅ Python Code (`app.py`)

```python
class Engine:
    def start(self):
        return "Engine has started."


class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine is part of Car

    def start_car(self):
        return self.engine.start()  # Access Engine's method


# Example usage
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())  # Output: Engine has started.

🧠 Explanation
Composition: The Car class includes an Engine object as part of its definition.

This is different from inheritance. Instead of Car being an Engine, it has an Engine.

The Car class uses the Engine class’s start() method through self.engine.start().

🖥️ Output
Engine has started.
