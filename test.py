import matplotlib.pyplot as plt
import csv

x = ["Less than $150", "Less than $300", "Less than $450", "Greater than $450"]
y = [0,0,0,0]

with open('pokemon+first+edition+holooutput.csv', 'r') as csvfile:  
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        if row[1] != 'price':
            if int(float(row[1])) < 150:
                y[0] += 1
            elif int(float(row[1])) >= 150 and int(float(row[1])) < 300:
                y[1] += 1
            elif int(float(row[1])) >= 300 and int(float(row[1])) < 450:
                y[2] += 1
            else:
                y[3] += 1
        # x.append(row[0])
        # y.append(row[1])
  
plt.bar(x, y, color = 'orange', width = 0.5, label = "Range of Prices")
plt.xlabel('Range of Sale')
plt.ylabel('Number of Cards Sold')
plt.title('Record Of PSA 10 Card Trading Sales Today')
plt.show()