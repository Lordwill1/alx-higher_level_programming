# 0x0A. Python - Inheritance

As I am diving deeper in Object Oriented Programming (OOP) with python, this project introduce me to the concept of `inheritance`


Inheritance is a mechanism in which one class acquires the property of another class. For example, a child inherits the traits of his/her parents. With inheritance, we can reuse the fields and methods of the existing class. Hence, inheritance facilitates Reusability and is an important concept of OOPs.


Python has two built-in functions that work with inheritance:

- Use `isinstance()` to check an instance’s type: `isinstance(obj, int)` will be `True` only if `obj.__class__` is `int` or some class derived from `int`.

- Use  `issubclass()` to check class inheritance: `issubclass(bool, int)` is `True` since bool is a subclass of int. However, issubclass(float, int) is `False` since `float` is not a subclass of `int`.


In this project, I learnt:
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions


# Resources
- [python documentation](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2020/10/inheritance-object-oriented-programming/#:~:text=super()%20function-,What%20is%20Inheritance%20in%20Object%20Oriented%20Programming%3F,known%20as%20the%20Parent%20class.)
- [youtube](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
