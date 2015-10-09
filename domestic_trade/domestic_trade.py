# DOMESTIC TRADE
# LANGUAGE: PYTHON

# You have been hired by a trade company to write a program.

# They have given you a CSV (comma separated value, used in spreadsheets) file containing sales data by transaction
#for 10,000 sales transactions.

# Write a function that calculates the grand total of sales for a given item across all stores.

# Your output should be in a form of a dictionary, with total_KSH as a key and the total as a value.

# Additionally, the company wants to know which store location made the largest sales for that item. Add that as another hash key-value pair.

# Notes:
#  - Check out this website for an intro to handling CSV files

# Example:

#   Given a `TRANS.csv` of:

#   store,sku,amount
#   Nairobi,DM1210,7000 KSH
#   Nairobi,DM1182,1968 KSH
#   Naivasha,DM1182,5858 KSH
#   Mombasa,DM1210,6876 KSH
#   Nakuru,DM1182,5464 KSH

# If we enter 'DM1182', you program should return:
# {:total_KSH=> 13290, :largest=> 'Nairobi'}.
import csv
def read_csv(item_id):
    #global variables and data structures
    line = ""
    splited = []
    output_dict = {}
    list_of_cities = []
    largest = ""
    total = 0
    final_dict = {}
    #read the csv file
    with open('TRANS.csv', 'rb') as csvfile:    
        city_cash_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in city_cash_reader:
            line = ', '.join(row)
            #check if the requested id exists in the line
            if line.find(item_id) != -1:
                #append to an empty list
                splited.append(line.split(','))
    #iterate the list that containes the line as an array           
    for item in splited:
        #fill the city dictionary with city and price values
        dict_of_cities = {'city': item[0], 'price': int(item[2])}
        #appened the dictionary to a list
        list_of_cities.append(dict_of_cities)
    #iterate the dictionary of cities
    for the_city in list_of_cities:
        #check if the output dictionary is still empty if so fill it with the city and price;
        if the_city['city'] not in output_dict:
            output_dict[the_city['city']] =  the_city['price']
        #then sum the values of simillar keys
        else:
             output_dict[the_city['city']] +=  the_city['price']
        #find the key that has the largest value
        largest = max(output_dict.iterkeys(), key = lambda k: output_dict[k])
        total = output_dict[largest]
        
    final_dict = {':total_KSH =>':total,':largest => ':largest}
    return final_dict
print(read_csv("DM1182"))
