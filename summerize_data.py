import pandas as pd
file_path = "Grouped_Imports_by_Group_All_Years.csv"
df = pd.read_csv(file_path)

#stroing quntities and values of each year in array
Quanties_year_array= []
Value_year_array = []
years = ["2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22"]
for year in years:
    qty_lst = df[f"{year} QTY"]
    val_lst = df[f"{year} VAL"]
    Quanties_year_array.append(qty_lst)
    Value_year_array.append(val_lst)

Avarage_Quanties_year_array = []
for i in range(len(Quanties_year_array)):
    sum = 0 
    for j in range(len(Quanties_year_array[i])):
        sum += Quanties_year_array[i][j]
    Avg = round(sum/len(Quanties_year_array[i]),3) #rounding to 3 decimal points
    Avarage_Quanties_year_array.append(Avg)
    # Avarage_Quanties_year_array.append(sum/len(Quanties_year_array[i]))

Avarage_value_year_array = []
for i in range(len(Value_year_array)):
    sum = 0 
    for j in range(len(Value_year_array[i])):
        sum+=Value_year_array[i][j]
    Avg = round(sum/len(Value_year_array[i]),3) #rounding to 3 decimal points
    Avarage_value_year_array.append(Avg)
    # Avarage_value_year_array.append(sum/len(Value_year_array[i]))

print("Average Quantities by year : " ,Avarage_Quanties_year_array);
print("Average Values by year : " ,Avarage_value_year_array);

'''Calculating standard deviation fo each year'''
std_div_quantiy = []
std_div_value = []
for i in range(len(Quanties_year_array)):
    sum = 0
    for j in range(len(Quanties_year_array[i])):
        sum+=(Quanties_year_array[i][j] - Avarage_Quanties_year_array[i])**2
    std_div = round((sum/ (len(Quanties_year_array[i])) -1) ** 0.5,3) #rounding to 3 decimal points
    std_div_quantiy.append(std_div)

for i in range(len(Value_year_array)):
    sum = 0
    for j in range(len(Value_year_array[i])):
        sum+=(Value_year_array[i][j] - Avarage_value_year_array[i])**2
    std_div = round( (sum / (len(Value_year_array[i])-1)) ** 0.5,3) #rounding to 3 decimal points
    std_div_value.append(std_div)

print("Standard Deviation of Quantities by year : " ,std_div_quantiy);
print("Standard Deviation of Values by year : " ,std_div_value);