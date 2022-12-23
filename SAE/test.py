import csv

liste_ip = ['127.0.0.1']
liste_port = ['6969']
liste_al = []

with open("./test.csv") as file:
  csvreader = csv.reader(file)
  csvr = csvreader.split(";")[1]
  for row in csvr:
    print(row)