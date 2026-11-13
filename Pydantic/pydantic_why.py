def insert_patient_data_problem(name, age):

    print(name)
    print(age)

    return 'Inserted into database...'


#in above code, logically the age should be and integer but if we do : insert_patient_data_problem('Shubham', 'Twenty') it will run OKAY!


def insert_patient_data_pythonHint(name: str, age: int):

    print(name)
    print(age)

    print('Inserted into database...')


#this can only give the type hinting if we again do: insert_patient_data_pythonHint('Shubham', 'Twenty'), it will again run and wont give any error!


def insert_patient_data_strictEnforce(name: str, age: int):

    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('Inserted into database...')

    else:
        raise TypeError('Incorrect data type')

insert_patient_data_strictEnforce('Shubham', 'Twenty')


#but its not SCALABLE







