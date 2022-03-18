import json
from numpy import append, number
import yaml

from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder
from typing import List


data = {
    'age':45,
    'name':'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city':None
}

json_filename = '/Users/ekaterina/home_work_data/data_file.json'



with open(json_filename,'w') as write_file:
    json.dump(data, write_file)
    print(json.dump)
    

with open(json_filename, 'r') as write_file:
    loaded_data = json.load(write_file)
    print(loaded_data)

yaml_filename ='/Users/ekaterina/home_work_data/data_file.yaml'


with open(yaml_filename,'w') as write_file:
    yaml.dump(data, write_file)
    print(yaml.dump)
    

with open(yaml_filename, 'r') as write_file:
    loaded_data = yaml.full_load(write_file)
    print(loaded_data)


@dataclass
class Person:
    age: int
    name: str
    children: list
    married: bool
    city: str

    def __init__(self, name, age, children, married, city):
        self.name = name 
        self.age = age
        self.children = children
        self.married = married
        self.city = city

children=[]
children.append(Person('Alice',3,[],False,''))

person = Person('Peter', 45, children, True, None)

print(json.dumps(person, indent=4, default=pydantic_encoder))







