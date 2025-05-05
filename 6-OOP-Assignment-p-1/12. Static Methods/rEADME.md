# 🌡️ Assignment: Static Methods – Temperature Conversion

## 🎯 Objective
Create a class `TemperatureConverter` with a static method `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit.

---

## ✅ Python Code (`app.py`)

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

🧠 Explanation
Static Method: The method celsius_to_fahrenheit does not depend on any class or instance variables. That’s why we use @staticmethod.

Formula Used:

Fahrenheit
=
(
Celsius
×
9
5
)
+
32
Fahrenheit=(Celsius× 
5
9
​
 )+32
You can call the method directly using the class name:
TemperatureConverter.celsius_to_fahrenheit(25)

🖥️ Output

25°C is equal to 77.0°F