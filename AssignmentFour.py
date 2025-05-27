# Method Overriding Example
class Vehicle:
    def start(self):
        print("Starting the vehicle")

class Car(Vehicle):
    def start(self):
        print("Starting the car with key...")

#Method Overloading Example, We use default arguments since python doesn't support it
class Calculator:
    def add(self, a,b=0, c=0):
        return a + b + c

# MRO Example
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

# Real world example of Method Overriding
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Real world example for method overloading
class Messenger:
    def send_message(self, to, message="Hi", attachment=None):
        if attachment:
            print(f"Sending '{message}' to {to} with attachment: {attachment}")
        else:
            print(f"Sending '{message}' to {to}")

# Demonstration
if __name__ == "__main__":
    print("---Method Overriding---")
    v = Vehicle()
    c = Car()
    v.start()
    c.start()

    print("\n----Method Overloading---")
    calc = Calculator()
    print("Sum:", calc.add(5))
    print("Sum:", calc.add(5,10))
    print("Sum:", calc.add(5,10,15))

    print("\n---MRO Example---")
    d = D()
    d.show()
    print(D.__mro__)

    print("\n---Real World Overriding---")
    animal = Animal()
    dog = Dog()
    animal.sound()
    dog.sound()

    print("\n---Real World Overloading---")
    msg = Messenger()
    msg.send_message("Sandra")
    msg.send_message("Mellisa", "Tracy")
    msg.send_message("Hello", "How are you")