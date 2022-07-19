import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("please enter the name of the city >> enter /n CH for chicago , NY for new york city , W for washington:  ").lower()
    
    while city not in ["ch","ny","w"]:
        city= input("Invalid city, please try again: ").lower()
        
        
    if city == "ch":
        city= 'chicago'
    elif city == "ny":
        city= 'new york city'
    elif city == "w":
        city= 'washington'
     
    

            # TO DO: get user input for month (all, january, february, ... , june)
    month= input("please enter the month or 'all' to apply no month filter: ").lower()
    while month not in ["january" ,"february" , "march" , "april" , "may" , "june" , "all"]:
        month= input("Invalid month, please try again: ").lower()

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please enter the day or 'all' to apply no day filter: ").lower()
    while day not in ["saturday" , "sunday" , "monday" , "tuesday" , "wednesday" , "thursday", "friday" , "all"]:
        day= input("Invalid day, please try again: ").lower()



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("the most common month is: {}" .format(most_common_month))


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("the most common day of week is: {}" .format(most_common_day))


    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print("the most common hour is: {}"  .format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_S_S = df['Start Station'].value_counts().idxmax()
    print ("The most commonly used start station is: {}" .format(common_S_S))


    # TO DO: display most commonly used end station
    common_E_S = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is: {}" .format(common_E_S))


    # TO DO: display most frequent combination of start station and end station trip
    x , y = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is {}   and   {}" . format(x,y))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print("total travel time = {}" .format(total))


    # TO DO: display mean travel time
    avg= df['Trip Duration'].mean()
    print("average travel time = {}" .format(avg))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("number of each type: ")
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print("number of each gender: ")
        print(user_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        common_year = df['Birth Year'].value_counts().idxmax()
        max_year = df['Birth Year'].max()
        min_year = df['Birth Year'].min()
        print("The most common year of birth is {} " .format(common_year))
        print("The most recent of birth is {} " .format(max_year))
        print("The earliest year of birth is {} " .format(min_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    """ display 5 rows by 5 rows """
    i = 0
    df = df.drop(["month" , "day_of_week" , "hour"] , axis=1)
       # TO DO: convert the user input to lower case using lower() function
    raw = input("do you want to see the raw data?  ").lower()
    while raw not in ["yes" , "ye" , "y" , "no" , "n"]:
        raw= input("invalid answer ,do you want to see the raw data?  ").lower()
    (x,y)= df.shape   
    while raw in ["yes" , "ye" , "y"]:
        if i >= x:
            break
            
        print(df[i:i+5])
        i+= 5
        raw = input("do you want to see more data?  ").lower()
        while raw not in ["yes" , "ye" , "y" , "no" , "n"]:
            raw= input("invalid answer ,do you want to see the raw data?  ").lower()
        
  
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes' , 'ye' , 'y']:
            break


if __name__ == "__main__":
	main()

    
