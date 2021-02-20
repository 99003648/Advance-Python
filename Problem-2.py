"""
Implement a Python program as follows.

* Create a class Temperature representing temperature in celsius format
* Add constructor for temperature class
* Add a method to retrive temperature value
* Convert from celsius to Fahrenheit format 
* Implement magical methods for following
    * Adding two temperature objects, e.g. is t1 is 36.1 and t2 is 1.2, result will be 36.3
    * Comparing if two temperature objects are equal or not, i.e. t1==t2
    * Check if one temperature object is smaller than other


Implement test cases using pytest for the following
-  constructor of Temperature class
-  Conversion to Fahrenheit formar
-  Magical methods supporting t1+t2, t1==t2, t1<t2


Guidelines:-
* Your code should be in compliance with PEP8, zero or minimal errors from pylint
* Use modular approach, different files for class implementation and test cases

Optional:-
-  Raise an exception if given temperature is out of (0,100) ranges
-  test case to check exception raise


"""
class Temperature:
    def __init__(self, temp):

        self.temp_celsius = temp
        self.temp_far = 0
    
    def temp(self):
        return self.temp_celsius
  
    def convert(self):

        self.temp_far = (1.8 * self.temp_celsius)+ 32
        return round(self.temp_far, 3)
    
    def display(self):
        print(self.temp_celsius)

    def __add__(self, other):
        value = self.temp_celsius + other.temp_celsius
        return Temperature(value)
        
    def __eq__(self, other):
          if self.temp_celsius == other.temp_celsius:
              return True
          return False
    
    def __lt__(self, other):
        if self.temp_celsius < other.temp_celsius:
            return True
        return False
    
    
C1=Temperature(45)
print(C1.convert())