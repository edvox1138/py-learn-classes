# myLogging.py
Add basic logging and log message into file.
Log a list 4 different ways.

```
04-23 18:12 __main__     DEBUG    This is a debug message
04-23 18:12 __main__:functionInfo INFO     This is a info message
04-23 18:12 __main__:functionWarning WARNING  This is a warn message
04-23 18:12 __main__:printFruits INFO     print fruits 1 way:
04-23 18:12 __main__:printFruits INFO     Apple
04-23 18:12 __main__:printFruits INFO     Orange
04-23 18:12 __main__:printFruits INFO     Banana
04-23 18:12 __main__:printFruits INFO     Strawberry
04-23 18:12 __main__:printFruits INFO     Mango
04-23 18:12 __main__:printFruits INFO     

print fruits 2 way:
04-23 18:12 __main__:printFruits INFO     Fruits: ['Apple', 'Orange', 'Banana', 'Strawberry', 'Mango']
04-23 18:12 __main__:printFruits INFO     

print fruits 3 way:
04-23 18:12 __main__:printFruits INFO     Fruits: Apple Orange Banana Strawberry Mango
04-23 18:12 __main__:printFruits INFO     

print fruits 4 way:
04-23 18:12 __main__:printFruits INFO     Fruits:Apple
Orange
Banana
Strawberry
Mango
```

# links:
# https://realpython.com/lessons/import-statement/
# https://realpython.com/python-logging/
#
#  https://pyyaml.org/wiki/PyYAMLDocumentation
#
# from <module_name> import <name(s)>
# An alternate form of the import statement allows individual 
# objects from the module to be imported directly into the caller’s symbol table:
#
#>>> try:
#...     # Non-existent module
#...     import foo
#... except ImportError:
#...     print('Module not found')
# 