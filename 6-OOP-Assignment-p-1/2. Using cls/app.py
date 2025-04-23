class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        # Increment count each time an object is created
        Counter.count += 1

    # Class method to display the current count
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Displaying object count
Counter.display_count()
