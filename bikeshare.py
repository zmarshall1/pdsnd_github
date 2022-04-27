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
    while True:
        city = input("Which city would you like to analyze?")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry, not a valid input, please try again")
            continue
       



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month do you want to filter by? January, February, March, April, May, June, or type 'all'")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("This is not a valid input, please try again")
            continue
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want details for a specific day? If yes, type day name or type 'all'")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input")
        
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
# TO DO: load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #TO DO: convert the Start Time colum to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #TO DO: extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #TO DO: filter by month if applicablwe
    if month != 'all':
        # use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #TO DO: filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        #TO DO:filter by day of week if applicable 
        if day != 'all':
            #TO DO: filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
        


    return df

       


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is", df['month'].mode()[0], "\n")


    # TO DO: display the most common day of week
    print("The most common day of week is", df['day_of_week'].mode()[0], "\n")


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   # TO DO: display most commonly used start station
    print("The most commonly use start station is ", df['Start Station'].mode()[0], "\n")
                                                                                
                                                                                
    # TO DO: display most commonly used end station
    print("The most commonly used end station is", df['End Station'].mode()[0], "\n")
          

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "" + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
          
          
         

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel Time:', Total_Travel_Time/86400, "Days")


    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean Travel Time:', Mean_Travel_Time/60, "Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\nThe most recent year of birth: {recent}\nThe most common year of birth:{common_year}")
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth:{common_year}")
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
