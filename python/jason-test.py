#! /usr/bin/env python3

import json

class Person:
    def __init__(self, name: str, dob: str, id: int, email: str, phone_number: str):
        self.name = name
        self.dob = dob
        self.id = id
        self.email = email
        self.phone_number = phone_number

    def to_json(self) -> str:
        """Convert the Person object to a JSON string."""
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str: str):
        """
        Create a Person object from a JSON string.

        Args:
            json_str (str): A JSON string representing a Person.

        Returns:
            Person: A Person object created from the JSON string.
        """
        data = json.loads(json_str)
        return Person(data["name"], data["dob"], data["id"], data["email"], data["phone_number"])

def write_person_to_file(person: Person, file_name: str):
    """
    Write a Person's information to a file as a JSON string.

    Args:
        person (Person): The Person object to write to the file.
        file_name (str): The name of the file to write to.
    """
    with open(file_name, "w") as file:
        file.write(person.to_json())

def read_person_from_file(file_name: str) -> str:
    """
    Read a Person's information from a file as a JSON string.

    Args:
        file_name (str): The name of the file to read from.

    Returns:
        str: The JSON string read from the file.
    """
    with open(file_name, "r") as file:
        return file.read()

def main():
    """
    Main function to test the Person class and the write_person_to_file and read_person_from_file functions.
    """
    # Create a new person object
    person = Person("Jason", "01-01-2000", 12345, "jason@example.com", "123-456-7890")
    print(person)
    
    # Write the person object to a file
    write_person_to_file(person, "person.json")
    
    # Read the person object from the file
    person_str = read_person_from_file("person.json")
    person2 = Person.from_json(person_str)
    print(person2)

if __name__ == "__main__":
    main()

