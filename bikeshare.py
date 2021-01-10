#!/usr/bin/env python
# coding: utf-8

# ## Importing libraries

# In[17]:


import pandas as pd
import numpy as np
import datetime


# In[18]:


CH = pd.read_csv("C://Users//felip//Desktop//Udacity Projects//chicago.csv")
NY = pd.read_csv("C://Users//felip\Desktop//Udacity Projects//new_york_city.csv")
WS = pd.read_csv("C://Users//felip\Desktop//Udacity Projects//washington.csv")


# ### Functions 

# In[19]:


def Table_Trans(df):
    df.columns = df.columns.str.replace(' ', '_')
    
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['End_Time'] = pd.to_datetime(df['End_Time'])
    
    df['start_month'] = df['Start_Time'].dt.month
    df['start_day'] = df['Start_Time'].dt.day
    df['start_hour'] = df['Start_Time'].dt.hour
    
    df['Trip'] = df['Start_Station']+ " to " + df['End_Station']
    df['Travel_Time'] = df['End_Time'] - df['Start_Time'] 
    
    df = df.drop(['Unnamed:_0'], axis=1)
    
    
    return df

def get_month(df):    
      
    return datetime.date(1900, df["start_month"].mode()[0], 1).strftime('%B')

def get_day(df):
    return df['Start_Time'].mode()[0].strftime("%A")

def get_time(df):
    return int(df['start_hour'].mode()[0])

def get_station(df,stage):
    if stage == "start":
        return df['Start_Station'].mode()[0]
    elif stage == "end":
        return df['End_Station'].mode()[0]
    elif stage == "trip":
        return df['Trip'].mode()[0]
    else:
        return "Not found"
def get_travel(df,measure):
    if measure == "total":
        return str(df["Travel_Time"].sum())
    if measure == "avg":
        return str(str(int((df["Travel_Time"].mean().seconds)/60)))
    
def get_cust(df,choice):
    try:
        if choice == "user":
            return df.groupby(['User_Type']).size().reset_index(name='Counts')
        elif choice == "gender":
            return df.groupby(['Gender']).size().reset_index(name='Counts')
    except:
        return "Oops, sorry! We still does not have info for that"
    
    

def get_year(df,choice):
    try:
        if choice == "early":
            return str(int(df['Birth_Year'].min()))
        elif choice == "recent": 
            return str(int(df['Birth_Year'].max()))
        elif choice == "mode":
            return (int(df['Birth_Year'].mode()[0]))
    except:
        return "Oops, sorry! We still does not have info for that"
    
def answering_system(QQ,city,name):
    if QQ[:4] == "time":
        QQ2 = input("Do you want to know about common months, day or hour for travel?").lower()                
        if QQ2[0] == "m": 
            print ("Most common month for travel in {} is {}".format(name,get_month(city)))
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
                        
                        
        elif QQ2[0] == "d":
            print("Most common day for travel in {} is {}".format(name,get_day(city)))
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
                        
                        
        elif QQ2[0] == "h":
            print("Most common hour for travel in {} is at {} hrs.".format(name,get_time(city)))
            ans = input("Do you want another operation? Y/N").lower()
            
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                return ("Thanks you for using our answering system")
                cond = False
                return cond
            else:
                print("Invalid input, please start again")
                cond = True
                return cond
                    
                    
    elif QQ[:4] == "stat":
        QQ2 = input("Do you want to know about common start stations,common end stations or most common route?").lower()
        QQ2 = QQ2.split()
        if "start" in QQ2[0]: 
            print("Most common month start station in {} is {}".format(name,get_station(city,"start")))
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
            
            
        elif "end" in QQ2:
            print("Most common end station in {} is {}".format(name,get_station(city,"end")))
            
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
            
            
        elif "route" in QQ2:
            print("Most common route for travel in {} is {}".format(name,get_station(city,"trip")))
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
            
        else:
            print("Invalid input, please start again")
            cond = True
            return cond
        
    elif QQ[:3] == "tri":
        QQ2 = input("Do you want to know total travel time or average travel time?").lower()
        QQ2 = QQ2.split()
        if "total" in QQ2: 
            print("The total travel time in {}is {}".format(name,get_travel(city,"total")))
            
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
        elif "average" in QQ2:
            print("The average travel time in {} is {} minutes".format(name,get_travel(city,"avg")))
          
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
        else:
            print("Invalid input, please start again")
            cond = True
            return cond
   

    elif QQ[:3] == "use":
        QQ2 = input("Do you want to know users types,users genders or users birthdays?").lower()
        QQ2 = QQ2.split()
        if "types" or "type" in QQ2[0]: 
            print ("The amount of customers,and suscribers in {} are: {} and {}".format(name,str(get_cust(city,"user").iloc[0,1]),str(get_cust(city,"user").iloc[1,1])))
        
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
        elif "genders" or "gender" in QQ2:
            print ("The amount of users per gender is in {} is: {} female and {} male".format(name,str(get_cust(city,"gender").iloc[0,1]),str(get_cust(city,"gender").iloc[1,1])))
            
            ans = input("Do you want another operation? Y/N").lower()
            if ans[0] == "y":
                cond = True
                return cond
            elif ans[0] == "n":
                print ("Thanks you for using our answering system")
                cond = False
                return cond
        elif "birthday" or "birthdays" or "birth" in QQ2:
            QQ3 = input ("Do you you want to know the earliest year of birth, the more recent, ot the most common birthday year?")   
            QQ3 = QQ3.split()
            if "earliest" or "early" in QQ3:
                print("In {} the earliest year of birth is:".format(name,get_year(city,"early")))                                  
                ans = input("Do you want another operation? Y/N").lower()
                if ans[0] == "y":
                    cond = True
                    return cond
                elif ans[0] == "n":
                    return ("Thanks you for using our answering system")
                    cond = False
                    return cond
                else:
                    print("Invalid input, please start again")
                    cond = True
                    return cond
            elif "recent" in QQ3:
                print("In {} most recent year of birth is: {}".format(name,get_year(city,"recent")))
                                                                           
                ans = input("Do you want another operation? Y/N").lower()
                if ans == "y":
                    cond = True
                    return cond
                elif ans == "n":
                    print ("Thanks you for using our answering system")
                    cond = False
                    return cond
                else:
                    print("Invalid input, please start again")
                    cond = True
                    return cond
                                                                          
            elif "common" in QQ3:
                print("In {} most common year of birth is: {}".format(name,get_year(city,"mode")))                                  
                
                ans = input("Do you want another operation? Y/N").lower()
                if ans[0] == "y":
                    cond = True
                    return cond
                elif ans[0] == "n":
                    print ("Thanks you for using our answering system")
                    cond = False
                    return cond
                else:
                    print ("Invalid input, please start again")
                    cond = True
                    return cond
    

CH = Table_Trans(CH)
NY = Table_Trans(NY)
WS = Table_Trans(WS)
    
  

        
    



# ## Answers 

# In[78]:


cond = True
while cond == True:
    start = input("What city do you want to review? New York (NY), Chicago (CH), Washington (WS)").lower()
    if start[0] == "n":
        city = NY
        name = "New York"
        QQ = input("Do you like to know about Times,stations,trips or users").lower()
        cond = answering_system(QQ,city,name)
    elif start[0] == "c":
        city = CH
        name = "Chicago"
        QQ = input("Do you like to know about Times,stations,trips or users").lower()
        cond  = answering_system(QQ,city,name)
    elif start [0] == "w":
        city = WS
        name = "Washington"
        QQ = input("Do you like to know about Times,stations,trips or users").lower()
        condt =answering_system(QQ,city,name)
    else:
        print ("Incorrect city")


# In[ ]:




