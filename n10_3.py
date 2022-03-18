import pickle
class Persone:

    def __init__(self, name, age):
        self.name = str(name) 
        self.age = int(age)
        


persons = []

persons.append(Persone('Kat',20))
persons.append(Persone('Mari',15))
persons.append(Persone('Bob',34))







data_filename = '/Users/ekaterina/home_work_data/ser.txt'

with open(data_filename,'wb') as file:
    dump = pickle.dumps(persons)
    file.write(dump)

with open(data_filename, 'rb') as file:
    dump = file.read()
    loaded_persons = pickle.loads(dump)
    print(loaded_persons)



