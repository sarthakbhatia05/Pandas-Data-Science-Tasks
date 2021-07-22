import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('Sales Merge.csv')
#cleaning data




#dropping all NAN values from the df
sales = sales.dropna(how='all')

#dropping all unwanted 'Or' values in the list
sales = sales[sales['Order Date'].str[0:2] != 'Or']

#converting data to correct numeric
sales['Quantity Ordered'] = pd.to_numeric(sales['Quantity Ordered'])
sales['Price Each'] = pd.to_numeric(sales['Price Each'])


sales['Month'] = sales['Order Date'].str[0:2]
sales['Month'] = sales['Month'].astype('int32')

#adding sales column

sales['Total Sale'] = sales['Quantity Ordered'] * sales['Price Each']
sales = sales.sort_values(['Order Date'],ascending= True)

#grouping all data for each month
group = sales.groupby('Month').sum()
print(group.sort_values(['Total Sale'],ascending=False))

x = group['Total Sale']
months = range(1,13)

#plotting a bar graph for the data

plt.bar(months,group['Total Sale'])
plt.title('Total Sale Over the Months',fontdict={'fontweight':'bold'})

plt.xlabel('Months')
plt.ylabel('Total Sale')

plt.yticks(group['Total Sale'])
plt.show()


print(sales)

