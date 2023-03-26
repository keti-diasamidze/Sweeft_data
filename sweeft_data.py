import sqlite3
import os
import subprocess
import pandas as pd

# setting up very basic sqlite database, inserting some values,connecting to database
conn = sqlite3.connect('employees_db.sqlite')
cursor = conn.cursor()


# cursor.execute('''
#           CREATE TABLE IF NOT EXISTS employees
#           ([id] INTEGER PRIMARY KEY, [first_name] TEXT, [last_name] TEXT, [age] INTEGER)
#           ''')
#
# cursor.execute('''
# INSERT INTO employees(id, first_name,last_name,age)
#
#  VALUES
#  (1,'Keti','Diasamidze',19 ),
#  (2,'Giorgi', 'Giorgadze',23),
#  (3,'Nino', 'Ninoshvili',25),
#  (4,'Mariam', 'Mamardashvili',32),
#  (5,'Ekaterine', 'Abashidze',45)
#  ''')
# conn.commit()


def connect():
    print('you are connected to database. you can search through table "employees" ')


def execute_query(query):
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

        # here i use pandas library to store query results in a file in a more readable way
        answer = input('do you want to save results to a file? y/n ')
        if answer == 'y':
            df = pd.read_sql_query(query, conn)
            filename = input('input file name here: ')
            with open(filename, 'w') as f:
                f.write(str(df.head()))
                print('data saved successfully')

    except sqlite3.Error as e:
        print(f'there is some kind of error: {e}')


def linux_commands(command):
    if command == 'pwd':
        print(os.getcwd())
    elif command == 'ls':
        content = (os.listdir())
        for each in content:
            print(each)
    elif command == 'cd':
        path = input('enter path here: ')
        try:
            os.chdir(path)
            print(os.getcwd())
        except FileNotFoundError as e:
            print(e)


def run_script(script):
    if os.path.exists(script):
        subprocess.run(['python', script])
    else:
        print('no such file or directory')


if __name__ == '__main__':
    while True:
        command = input('choose desirable command: connect to database, execute query,run python script ,navigate the file system,exit: ')
        if command.startswith('connect'):
            connect()
        elif command.startswith('execute'):
            query = input('enter your query here: ')
            execute_query(query)
        elif command.startswith('navigate'):
            linux_com = input('choose which command u want to run: ls,cd or pwd ')
            linux_commands(linux_com)
        elif command.startswith('run'):
            script = input('enter script name here: ')
            run_script(script)

        elif command == 'exit':
            conn.close()
            print('connection closed')
            break
        else:
            print('please, choose valid option')
