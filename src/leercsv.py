import csv

def leer_csv():

    path_archivo = 'data/empleados.csv'

    with open(path_archivo) as csv_file:
        reader = csv.reader(csv_file)
        for linea in reader:
            print(linea)




if __name__ == '__main__':
    leer_csv()