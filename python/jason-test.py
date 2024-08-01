#! /usr/bin/env python3

import json

class Person:
    def __init__(self, name: str, dob: str, id: int, email: str, phone_number: str):
        self.name = name
        self.dob = dob
        self.id = id
        self.email = email
        self.phone_number = phone_number
    # Function to return a string representation of the person object
    def __str__(self):
        return f"Person(name={self.name}, dob={self.dob}, id={self.id}, email={self.email}, phone_number={self.phone_number})"
    
    # Function to return a JSON string representation of the person object
    def to_json(self):
        return json.dumps(self.__dict__)
    
    # Function to create a person object from a JSON string
    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Person(data["name"], data["dob"], data["id"], data["email"], data["phone_number"])

# Function write_person_to_file to write a person's information to a file as a JSON string
def write_person_to_file(person: Person, file_name: str):
    with open(file_name, "w") as file:
        file.write(person.to_json())

# Function read_person_from_file to read a person's information from a file as a JSON string
def read_person_from_file(file_name: str):
    with open(file_name, "r") as file:
        return file.read()
    
# Main function to test the Person class and the write_person_to_file and read_person_from_file functions
def main():
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

