import csv

liste_ip = ['127.0.0.1']
liste_port = ['6969']
liste_al = []

with open("./test.csv") as file:
  csvreader = csv.reader(file, delimiter=';')
  for row in csvreader:
    print(row)
    
print(liste_al)