

#Python Collections -Data Structures


#List - Ordered/Index based/Duplicate/Dynamic
#Tuple - Ordered/Index based/Duplicate/static
#Set - Unordered and unindexed
#Dictionary - Unordered / Key and Value eg name: prakashr97@gmail.com


'''''
List is Index based
List syntax []
List allowed duplicates values
List allowed mixed data types
List is Dynamic
'''''


cars=['BMW','Volvo',12,12.5,True,12]
cars.append(45)
cars.pop(3)#based on value index to remove
cars.insert(2,"Honda")
cars.remove("BMW")#based on value to remove
# cars.clear()#it will remove entire list
# del cars

print(cars)

