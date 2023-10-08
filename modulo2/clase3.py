# trabajo con archivos CSV
import csv
from pathlib import Path

FILE_PATH = Path('users.csv')


def read_csv():
    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row.get('first_name'), ' ', row.get('email'))
    except:
        print('No se encontro el archivo')


def write_csv():
    try:
        with open(FILE_PATH, 'a') as file:
            writer = csv.DictWriter(
                file, fieldnames=['first_name', 'last_name', 'email']
            )

            writer.writerows([
                {
                    'first_name': 'Cristian',
                    'last_name': 'Segovia',
                    'email': 'cristiansegovia@gmail.com'
                },
                {
                    'first_name': 'Jimena',
                    'last_name': 'Chipi',
                    'email': 'jimechipi@gmail.com'
                }
            ])
            print('Datos agregados correctamente')
    except:
        print('Datos no agregados!')


if __name__ == '__main__':
    read_csv()
    print('=============')
    write_csv()
    print('=============')
    read_csv()
    print('=============')
