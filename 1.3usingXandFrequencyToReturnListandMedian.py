# This program will use X value and its frequence to return mean and median of the data list
# This program will print out the full data list also the sorted full data list and the median.

import statistics
print ("Please input each X followed by its frequency: ", 
       '\n(using space key to seperate each input and press enter to end)')

x_f_list = list(map(float, input( ). split ( )))
total = 0
i = 0
n = 0
while i in range(len(x_f_list)):
    total += x_f_list[i]*x_f_list[i+1]
    n += x_f_list[i+1]
    i += 2

x_list = x_f_list[0::2]
frequence_list = x_f_list[1::2]
frequence_list = [int(i) for i in frequence_list]
full_x_list = []
for i,j in zip(x_list,frequence_list):
    full_x_list.extend([i]*j)

print('The full data is: ',full_x_list)
print('The sorted full data is: ', sorted(full_x_list))
print('The median of the list is: ', statistics.median(full_x_list))
print('The sample mean is: ', '{0:.3f}'.format(total / n))