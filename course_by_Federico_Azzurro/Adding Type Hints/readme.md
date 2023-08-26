**Adding Type Hints to your Python code**

Adding type hints to your Python code is a great way to improve code readability and maintainability.
Type hints help convey the expected data types of variables and function parameters, making it easier for others (and your future self) to understand the code.

Here's a quick guide on how to add type hints to your Python code:

1. **Import the `typing` module:** The `typing` module provides various classes that you can use to indicate types.


    from typing import List, Dict, Any

**Type hint variables:**

    name : str = "Laxmi"
    age : int = 26

**Type hint function Parameters and return types:**

    def greet(name:str)->str:
        return f"Hello, {name}!"

**Type hint for lists and dictionaries:**
    
    def process_numbers(numbers:List[int])->List[int]:
        result = [num *2 for num in numbers]
        return result

    def process_data(data : Dict[str,Any])->Dict[str,int]:
        processed_data = {key : len(value) for key,value in data.items()}
        return processed_data

**Type hint for optional types using `Optional`**
    

    from typing import Optional
    
    def optional_greeting(name:Optional[str])->str:
        if name:
            return f"Hello, {name}!"
        else:
            return "Hello, World!"



**Type hint for custom classes**

    class Person:
        def __init__(self,name:str,age:int):
            self.name = name
            self.age = age

Note that type hints are not enforced at runtime; they are meant to provide information to developer and tools (like linters and type checkers) to catch potential issues early.

By adding type hints to your code, you enhance it's readability and help others understand how to interact with your codebase effectively.
