

filename = '/Users/ekaterina/home_work_data/file.txt'
with open(filename,'w') as file:
    file.write('A man can stand anything except a succession of ordinary days\n')
    
with open(filename,'r') as file:
    readline = file.readline() 
    print(readline)

















