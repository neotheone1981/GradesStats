import pandas as pd
import matplotlib.pyplot as plt 

def getAs(val):
    sum1=val['A']+val['A+']+val['A-']
    sum2=val['B']+val['B+']+val['B-']
    sum3=val['C']+val['C+']+val['C-']
    sum4=val['D']+val['D+']
    sum5=val['F']+val['W']
    return sum1,sum2,sum3,sum4,sum5

data = pd.read_excel (r'./grades.xlsx')

x=data.head()

x=x.iloc[-1]

res1,res2,res3,res4,res5=getAs(x)

print(x)

print('Total number of As is %s' % res1)
print('Total number of Bs is %s' % res2)
print('Total number of Cs is %s' % res3)
print('Total number of Ds is %s' % res4)
print('Total number of A and Ws is %s' % res5)

# Data to plot
labels = 'As', 'Bs', 'Cs', 'Ds','Fs and Ws'
sizes = [res1, res2, res3, res4, res5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
explode = (0, 0, 0, 0, 0.1)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

plt.bar(labels, sizes, align='center', alpha=0.5, color=colors)
plt.xticks(labels)
plt.ylabel('Frequency')
plt.title('Grades Histgram')

plt.show()
