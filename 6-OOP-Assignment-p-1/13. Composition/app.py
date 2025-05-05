# app.py

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
