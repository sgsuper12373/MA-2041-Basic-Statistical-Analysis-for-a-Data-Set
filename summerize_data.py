''' In this we are going to calculate the the avarage Quantities of petrochemical compounds bougth each year same way we are going to calcalate the avarage Values spend for petrochemical compund
    Then we will be standard deviation between petrochemical compunds quantity and value per year. 
    all of above results will be stored in the form of array
'''


import pandas as pd
file_path = "Grouped_Imports_by_Group_All_Years.csv"
df = pd.read_csv(file_path)

#stroing quntities and values of each year in array
def covariance(X,Y):
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    cov = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)) / n
    return cov
def correlation_coefficient(X, Y):
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    cov = covariance(X, Y)
    std_X = (sum((X[i] - mean_X) ** 2 for i in range(n)) / n) ** 0.5
    std_Y = (sum((Y[i] - mean_Y) ** 2 for i in range(n)) / n) ** 0.5
    return cov / (std_X * std_Y)

#np.mean(lst) if using numpy
def average(lst):
    return round(sum(lst) / len(lst),3)
#np.std_dev if using numpy
def std_div(lst):
    n = len(lst)
    mean = average(lst)
    variance = sum((x - mean) ** 2 for x in lst) / (n - 1)
    return round(variance ** 0.5,3)


#Array which will contain the year wise petrochemical compunds quantity purchased same way we have Value_year_array
Quanties_year_array= []
Value_year_array = []
years = ["2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22"]

# print(Quanties_year_array)
for year in years:
    qty_lst = df[f"{year} QTY"]
    val_lst = df[f"{year} VAL"]
    Quanties_year_array.append(qty_lst)
    Value_year_array.append(val_lst)


#Calcuating and storing avarage qunatites of petrochemical compound import by year (form 2014-2015 to 2020-2021)
Avarage_Quanties_year_array = []
for i in range(len(Quanties_year_array)):
    Avarage_Quanties_year_array.append(average(Quanties_year_array[i]))
Avarage_value_year_array = []
for i in range(len(Value_year_array)):
    Avarage_value_year_array.append(average(Value_year_array[i]))

print("Average Quantities by year : " ,Avarage_Quanties_year_array)
print("Average Values by year : " ,Avarage_value_year_array)

'''Calculating standard deviation fo each year'''
std_div_quantiy = []
std_div_value = []
for i in range(len(Quanties_year_array)):
    std_div_quantiy.append(std_div(Quanties_year_array[i]))
for i in range(len(Value_year_array)):
    std_div_value.append(std_div(Value_year_array[i]))

print("Standard Deviation of Quantities by year : " ,std_div_quantiy)
print("Standard Deviation of Values by year : " ,std_div_value)


corr_per_year = [round(correlation_coefficient(Quanties_year_array[i] , Value_year_array[i]),3) for i in range(len(Quanties_year_array))]
print("correlation coefficient between Quantity and Val for each year: ", corr_per_year)




'''Calculating correlation coefficient of total quantities and toatal values'''
Total_Quantities_per_year = [sum(Quanties_year_array[i]) for i in range(len(Quanties_year_array))]
Total_Value_per_year = [sum(Value_year_array[i]) for i in range(len(Value_year_array))]

corr= round(correlation_coefficient(Total_Quantities_per_year , Total_Value_per_year), 3);
print("Correlation coefficinet between Total Quatities from year 2014->2021 and Total Values from year 2014->2021 : ", corr)
