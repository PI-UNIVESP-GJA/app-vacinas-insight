import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "BCG.csv"

nome =[]
col1 =[]
col2 =[]
col3 =[]
valores=[]

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ';')
    fields = next(csvreader)
    for idx,row in enumerate(csvreader):
        valores.append([])
        if idx>4:
            break
        nome.append(row[0])
        col1.append(float(row[1].replace(',',".")))
        col2.append(float(row[2].replace(',',".")))
        col3.append(float(row[3].replace(',',".")))
        for i in range(1,26):
            valores[idx].append(float(row[i].replace(',','.')))


    
#print(nome)
        
  
fig, ax = plt.subplots()  
ax.plot(fields[1:],valores[0], color = 'g', label=nome[0])
ax.plot(fields[1:],valores[1], color = 'r', label=nome[1])
ax.plot(fields[1:],valores[2], color = 'b', label=nome[2])

ax.legend()
ax.grid()

plt.show()
 
##
#print("Total no. of rows: %d"%(csvreader.line_num))
 

#print('Field names are: ' + ', '.join(field for field in fields))

#print('\nElements:\n')
#for row in col1[:5]:
#        print(float(row.replace(',',"."))),

    