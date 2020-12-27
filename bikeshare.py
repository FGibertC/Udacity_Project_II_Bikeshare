#!/usr/bin/env python
# coding: utf-8

# ## Importing libraries

# In[54]:


import pandas as pd
import numpy as np
import datetime


# In[55]:


CH = pd.read_csv("D://Escritorio//Udacity Projects//Project II//DATA//chicago.csv")
NY = pd.read_csv("D://Escritorio//Udacity Projects//Project II//DATA//new_york_city.csv")
WS = pd.read_csv("D://Escritorio//Udacity Projects//Project II//DATA//washington.csv")


# In[56]:


NY


# ### Functions 

# In[78]:


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
        return "Not a valid input"
    
    

def get_year(df,choice):
    try:
        if choice == "early":
            return str(int(df['Birth_Year'].min()))
        elif choice == "recent": 
            return str(int(df['Birth_Year'].max()))
        elif choice == "mode":
            return (int(df['Birth_Year'].mode()[0]))
    except:
        return "Not a valid input"
    
  

        
    



# ## Transforming dataframes

# In[58]:


CH = Table_Trans(CH)
NY = Table_Trans(NY)
WS = Table_Trans(WS)


# ## Checking variables types

# In[1]:


CH.dtypes
NY.dtypes
WS.dtypes


# ## Answers 

# ## 1.- Popular times of travel 

# In[45]:


#1 Popular times of travel (i.e., occurs most often in the start time)

#most common month
print("Most common month for travel in Chicago is {}, for New York is {} and in Washigton is {}".format(get_month(CH),get_month(NY),get_month(WS)) )


#most common day
print("Most common day for travel in Chicago is {}, for New York is {} and in Washigton is {}".format(get_day(CH),get_day(NY),get_day(WS)) )


#most common hour of day
print("Most common hour for travel in Chicago is {}, for New York is {} and in Washigton is {}".format(get_time(CH),get_time(NY),get_time(WS)) )


# ## 2.- Popular stations and trip

# In[46]:



#most common start station
print ("Most common station in Chicago is: {}, in New York is: {} and finally in Washigton is {}".format(get_station(CH,"start"),get_station(NY,"start"),get_station(WS,"start")) )


#most common end station
print ("Most common station in Chicago is: {}, in New York is: {} and finally in Washigton is {}".format(get_station(CH,"end"),get_station(NY,"end"),get_station(WS,"end")) )

#most common trip from start to end (i.e., most frequent combination of start station and end station)

print ("Most common trip in Chicago is: {}, in New York is: {} and finally in Washigton is {}".format(get_station(CH,"trip"),get_station(NY,"trip"),get_station(WS,"trip")) )


# ## 3.- Trip duration

# In[81]:


#total travel time
print ("The total travel time for Chicago is: {}, in New York is: {} and finally in Washigton is {}".format(get_travel(CH,"total"),get_travel(NY,"total"),get_travel(WS,"total")) )

#average travel time
print ("The total travel time for Chicago is: {} minutes, in New York is: {} minutes and finally in Washigton is {} minutes".format(get_travel(CH,"avg"),get_travel(NY,"avg"),get_travel(WS,"avg")) )


# ## 4.-User Info

# In[81]:


#counts of each user type

print ("The amount of customers,dependent and suscribers in Chicago are: {}, {} and {}".format(str(get_cust(CH,"user").iloc[0,1]),str(get_cust(CH,"user").iloc[1,1]),str(get_cust(CH,"user").iloc[2,1])))
print ("The amount of customers,and suscribers in New York are: {} and {}".format(str(get_cust(NY,"user").iloc[0,1]),str(get_cust(NY,"user").iloc[1,1])))
print ("The amount of customers,and suscribers in Washington are: {} and {}".format(str(get_cust(WS,"user").iloc[0,1]),str(get_cust(WS,"user").iloc[1,1])))

#counts of each gender (only available for NYC and Chicago)

print ("The amount of users per type is in Chicago is: {} female and {} male".format(str(get_cust(CH,"gender").iloc[0,1]),str(get_cust(CH,"gender").iloc[1,1])))
print ("The amount of users per type is in New York is: {} female and {} male".format(str(get_cust(NY,"gender").iloc[0,1]),str(get_cust(NY,"gender").iloc[1,1])))

#earliest, most recent, most common year of birth (only available for NYC and Chicago)

print("In New York the earliest year of birth is: {}, the more recent is: {} and the most common year is: {}".format(get_year(NY,"early"), get_year(NY,"recent"),get_year(NY,"mode")))
print("In Chicago the earliest year of birth is: {}, the more recent is: {} and the most common year is: {}".format(get_year(CH,"early"), get_year(CH,"recent"),get_year(CH,"mode")))


# ## 5.- Program Prototype

# In[90]:


cond = True
while cond == True:
    start = input("What city do you want to review? New York (NY), Chicago (CH), Washington (WS)").lower()
    if start[0] == "n":
        QQ = input("Do you like to know about Times,stations,trips or users").lower()
        if QQ == "times":
            print("Most common month for travel in New York is {}, and the day is {},finally the hour is {} hrs".format(get_month(NY),get_day(NY),get_time(NY)))
            cond = False
        
        elif QQ == "stations":
            print ("Most common start station in New York is: {}, the most common end station is: {} and finally most common trip is {}".format(get_station(NY,"start"),get_station(NY,"end"),get_station(WS,"trip")) )
            cond = False
        elif QQ == "trips":
            print ("the total travel time for New York is: {}, and the average travel time is: {} minutes".format(get_travel(NY,"total"),get_travel(NY,"avg")) )
            cond = False
        elif QQ == "users":
            print ("The amount of customers,and suscribers in New York are: {} and {}".format(str(get_cust(NY,"user").iloc[0,1]),str(get_cust(NY,"user").iloc[1,1])))
            print ("The amount of users per type is in New York is: {} female and {} male".format(str(get_cust(NY,"gender").iloc[0,1]),str(get_cust(NY,"gender").iloc[1,1])))
            print("In New York the earliest year of birth is: {}, the more recent is: {} and the most common year is: {}".format(get_year(NY,"early"), get_year(NY,"recent"),get_year(NY,"mode")))
            cond = False
        
    elif start[0] == "c":
        QQ = input("Do you like to know about Times,stations,trips or users").lower()
        if QQ == "times":
            print("Most common month for travel in Chicago is {}, and the day is {},finally the hour is {} hrs".format(get_month(CH),get_day(CH),get_time(CH)))
            cond = False
        
        elif QQ == "stations":
            print ("Most common start station in Chicago is: {}, the most common end station is: {} and finally most common trip is {}".format(get_station(CH,"start"),get_station(CH,"end"),get_station(CH,"trip")) )
            cond = False
        elif QQ == "trips":
            print ("the total travel time for Chicago is: {}, and the average travel time is: {} minutes".format(get_travel(CH,"total"),get_travel(CH,"avg")) )
            cond = False
        elif QQ == "users":
            print ("The amount of customers,and suscribers in Chicago are: {} and {}".format(str(get_cust(CH,"user").iloc[0,1]),str(get_cust(CH,"user").iloc[1,1])))
            print ("The amount of users per type is in Chicago is: {} female and {} male".format(str(get_cust(CH,"gender").iloc[0,1]),str(get_cust(CH,"gender").iloc[1,1])))
            print("In Chicago the earliest year of birth is: {}, the more recent is: {} and the most common year is: {}".format(get_year(CH,"early"), get_year(NY,"recent"),get_year(CH,"mode")))
            cond = False
        
    elif start[0] == "w":
        QQ = input("Do you like to know about Times,stations,trips or users").lower()
        if QQ == "times":
            print("Most common month for travel in Washington is {}, and the day is {},finally the hour is {} hrs.".format(get_month(WS),get_day(WS),get_time(WS)))
            cond = False
        
        elif QQ == "stations":
            print ("Most common start station in Washington is: {}, the most common end station is: {} and finally most common trip is {}".format(get_station(WS,"start"),get_station(WS,"end"),get_station(WS,"trip")) )
            cond = False
        elif QQ == "trips":
            print ("the total travel time for Washington is: {}, and the average travel time is: {} minutes".format(get_travel(WS,"total"),get_travel(WS,"avg")) )
            cond = False
        elif QQ == "users":
            print ("The amount of customers,and suscribers in Washington are: {} and {}".format(str(get_cust(WS,"user").iloc[0,1]),str(get_cust(WS,"user").iloc[1,1])))

            cond = False
        
    else:
        print ("Not a valid input")
        
        


# In[ ]:




