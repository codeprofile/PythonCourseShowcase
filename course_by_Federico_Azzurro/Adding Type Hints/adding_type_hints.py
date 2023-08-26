from typing import List, Dict, Any


# Type hint function Parameters and return types:
def greet(name: str) -> str:
    return f"Hello, {name}!"


# Type hint for lists and dictionaries:
def process_numbers(numbers: List[int]) -> List[int]:
    result = [num * 2 for num in numbers]
    return result


def process_data(data: Dict[str, Any]) -> Dict[str, int]:
    processed_data = {key: len(value) for key, value in data.items()}
    return processed_data


# Type hint for optional types using Optional
from typing import Optional


def optional_greeting(name: Optional[str]) -> str:
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"


# Type hint for custom classes

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


if __name__ == "__main__":
    # Type hint variables:
    name: str = "Laxmi"
    age: int = 26
    print(greet(name))
    print(process_numbers([1, 2, 3]))
    print(process_data({"first_name": "Laxmi", "last_name": "Sarki"}))
    print(optional_greeting(name))
    print(optional_greeting(None))
    print(Person(name, age))
