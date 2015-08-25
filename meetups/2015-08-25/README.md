# Alamo Python Learners Meetup - 08/25/2015

[Github repo](https://github.com/alamo-python-learners/alamo-python-learners)
[Meetup](http://www.meetup.com/Alamo-Python-Learners)

## Getting Started with Python

### How to see if python is installed on your system

    $\> python --version
    Python 2.7.6

### Python Versions

This also tells you which version of Python you are using, there are some significant differences between Python v2.x and v3.x

### How to execute Python code

If you have Python installed on your system there are 3 main ways to run it.

1. Interactive

    jamal@mjolnir ~ $ python
    Python 2.7.6 (default, Jun 22 2015, 17:58:13)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

You can exit this mode by typing quit()

2. Running a script directly

    jamal@mjolnir ~ $ cat hello.py
    print "Hello Python!"

    jamal@mjolnir ~ $ python hello.py
    Hello Python!

3. Importing another Python module

    from <module> import <python code>

### Variables

Variables are a way of organizing and storing information in our programs, you can think of them as:

1. Containers that have names
2. They can hold and represent anything

    >>> secret_of_life = 42
    >>> secret_of_life / 6
    7

### Basic Data Types

1. Strings
..* Hold characters
..* Enclosed in quotes
2. Integers
..* Whole numbers
3. Float
..* Floating point (decimal like) numbers
4 Boolean
..* True or False

### Equivalence vs. assignment

Python uses = and == to mean two different things
This can be confusing for beginners, the reason for the two different notations is that equals can be used to mean two different things.

1. Assignment - Sets a variable to some value

    x = 8
    pie = "Apple"

2. Equivalence - Are these two things the same?

    x == 8              >> True
    pie == "Apple"      >> True

    x == 12             >> False
    pie == "Rhubarb"    >> False

### Fizz Buzz

*Coding exercise*

Given a string of numbers separated by spaces

    "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"

When this string is run through Fizz Buzz

Then it will replace numbers

* Divisible by 3 with "Fizz"
* Divisible by 5 with "Buzz"
* Divisible by 3 and 5 with "Fizz Buzz"

