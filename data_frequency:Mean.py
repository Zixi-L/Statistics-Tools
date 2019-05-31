# This program will construct a data frequency table and return the sample mean

from collections import Counter
data = []
finished = False

while finished == False:
    try:
        x = float(input('Please input data: '))
        data.append(x)
        bottom = input('Please press Y if you are done, otherwise press enter: ')
        if bottom == 'Y':
            finished = True      
    except:
        print('Error! Please input a real number.')
    
count = Counter(data)
for k in sorted(count):
    print ('X: ',k, ' Frequency: ',count[k])

total = 0
for i in data:
    total += i

print('\nThe sample mean is: ', '{0:.3f}'.format(total/len(data)))