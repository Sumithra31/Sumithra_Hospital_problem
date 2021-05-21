# -*- coding: utf-8 -*-
"""
Created on Fri May 21 23:21:53 2021

@author: Sumithra V Aradhya
"""

import pandas as pd
import datetime


def date_compare(date1 , date2 , greater):
    a , b , c = date1.split('/')
    d , e , f = date2.split('/')
    date1 = datetime.datetime(int(c),int(b),int(a))
    date2 = datetime.datetime(int(f),int(e),int(d))
    if(greater):
        return date1 >= date2
    else:
        return date1 <= date2
    

file = open(r"C:\Users\Sumithra V Aradhya\OneDrive\Desktop\Sumithra.csv", mode='w', encoding='utf-8')
file.write("name , age , branch , date ,address\n")
while True:
    print('enter details...')
    name = input('enter name : ')
    age = int(input('enter age : '))
    branch = input('enter branch :')
    date = input('enter date : ')
    address = input('enter address : ')
    details = name +','+str(age) +','+ branch +','+date + ','+ address +'\n'
    print(details)
    file.write(details)
    check_available_patients = input('enter c to check patients count else enter any key')
    if(check_available_patients == 'c'):
        file.close()
        break
dataset = pd.read_csv(r"C:\Users\Sumithra V Aradhya\OneDrive\Desktop\Sumithra.csv")
df = pd.DataFrame(dataset)
date_column , address_column = df[df.columns[3]] , df[df.columns[4]]
start_date = input('enter start date : ')
end_date = input('enter end date : ')
banglore = []
non_banglore = []
for date , address in zip(date_column,address_column):
    if(date_compare(date , start_date ,True)  and date_compare(date , end_date , False)):
        print('satisfied')
        if((address == 'banglore') or (address == 'bengaluru') or (address == 'blr')):
            banglore.append(address)
        else:
            non_banglore.append(address)
print('number of patients from banglore is ', len(banglore))
print('number of patients from other than banglore is ', len(non_banglore))