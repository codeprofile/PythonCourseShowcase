**Underscores in Numeric Literals**

Python allows the use of underscores in numbers as a way to enhance the readability of numeric literals,particularly when dealing with large numbers.

This feature was introduced in Python 3.6 as part of `PEP 515("Underscores in Numeric Literals")`.

Using underscores in numeric literals helps separate digits into more readable groups, making it easier to understand the magnitude of the number at a glance.

This is particularly useful for large numbers like thousands, millions or billions, where the digits can quickly become overwhelming.


For example:

    population =  7_800_000_000 #7.8 billion
    credit_card_number = 1234_5678_9012_3456


Underscores are ignored by the Python Interpreter when parsing numeric literals, so they don't affect the actual value of the number.
This means that you can use underscores to format numbers for better human readability without any impact on the computations performed by your code.


The use of underscores in numeric literals is purely for code readability and does not affect the way 
the numbers are processed or used within the code.It's a feature designed to make your code more human-friendly while preserving its accuracy and functionality.



