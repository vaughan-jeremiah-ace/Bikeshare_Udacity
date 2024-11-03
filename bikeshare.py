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
    city_check = ['chicago', 'new york city', 'washington']
    while True:
        try:
            test_city = input("What city would you like to investigate? \nThe three options include chicago, new york city or washington.\n").lower()
            if test_city in city_check:
                city = test_city
                break
            else:
                print('Please check your spelling.')
        except:
            print('This is outside of our area')                  

    # TO DO: get user input for month (all, january, february, ... , june)
    months_check = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
        try:
            month_check = input("\nWhich month would you like to review?\nThe options include (all, january, february, ... , june).\n").lower()
            if month_check in months_check:
                month = month_check
                break
            else:
                print('Please check your spelling.')
        except:
            print('This is outside of our date range') 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_check = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        try:
            day_check = input("\nWhat day of the week would you like to review?\nThe options include (all, monday, tuesday, .... sunday.\n").lower()
            if day_check in days_check:
                day = day_check
                break
            else:
                print('Please check your spelling.')
        except:
            print('This is outside of our date range') 

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()    
    # TO DO: display the most common month
    '''Confirms if more then 1 month selected before providing favorite month'''
    unique_month = df['Month'].nunique()
    if unique_month >1:  
        popular_month = df['Month'].mode()[0]
        print('The most popular month is: {}. \n'.format(popular_month))
        month_complete = time.time()
    else:
       print('Only one month selected, so unable to calculate most frequent month.')
     
    # TO DO: display the most common day of week
    '''Confirms if more then 1 day selected before providing favorite day'''    
    unique_day = df['day_of_week'].nunique()
    if unique_day >1:
        weekday_start_time = time.time()
        popular_weekday = df['day_of_week'].mode()[0]
        print('The most popular day of the week is: {}. \n'.format(popular_weekday))
        day_complete = time.time()
    else:
       print('Only one weekday selected, so unable to calculate most frequent day')
 
    # TO DO: display the most common start hour
    hour_start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is: {} (24hrs).\n'.format(popular_hour))
    hour_complete = time.time()
    print('The time to retrieve data is: %s seconds.\n' % (hour_complete - hour_start_time))   

    #Total Calculation time
    print("\nTotal calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_point = df['Start Station'].mode()[0]
    print('The most frequently visited station to start a trip is \n',common_start_point)

    # TO DO: display most commonly used end station
    common_end_point = df['End Station'].mode()[0]
    print('\nThe most frequent final destination is \n',common_end_point)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Trip'] = df['Start Station'] + ' ---> ' + df['End Station']
    most_frequent_trip = df['Combined Trip'].mode()[0]
    print('\nThe most frequent trip is \n',most_frequent_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total trip time for the selected time period is {} hours. \n'.format(((df['Trip Duration'].sum())/60).round(2)))
       
    # TO DO: display mean travel time
    print('The average trip time for the selected time period is {} minutes. \n'.format(df['Trip Duration'].mean().round(2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    # TO DO: Display counts of user types
    subscriber = (df['User Type'] == 'Subscriber').sum()
    customer = (df['User Type'] == 'Customer').sum()
    dependent = (df['User Type'] == 'Dependent').sum()
    blank_subscriber = df['User Type'].isna().sum()
    print('Here is a quick breakdown of our current user vs subscriber counts.\n')
    print('{} riders were listed as a subscriber\n{} were listed as a customer\n{} were listed as dependent\n'.format(subscriber, customer, dependent))
    print('We were not able to capture the subscription status on {} riders.\n'.format(blank_subscriber))

    '''Currently Washington does not provide user information and provides a error if selected'''        
    try:
        male = (df['Gender'] == 'Male').sum()
        female = (df['Gender'] == 'Female').sum()
        blank = df['Gender'].isna().sum()
        total_rows = male+female+blank
        # TO DO: Display counts of gender
        print('Here is a breakdown of the genders that use our product. \n')
        print('Of the {} trips made:\n{} were male\n{} were female\n{} left the information blank.\n'.format(total_rows, male, female, blank))

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Our oldest user was born in: {} \n'.format(df['Birth Year'].min().astype(int)))
        print('Our youngest user was born in: {} \n'.format(df['Birth Year'].max().astype(int)))
        print('Most of our users were born in born in: {} \n'.format(df['Birth Year'].mode()[0].astype(int)))  
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except KeyError:
        print('Currently this city does not have User gender/birth year information at this time.\n')
      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        ## removes columns that were created for the reporting script#####
        df.drop(['Combined Trip','hour', 'month','Month','day_of_week'],axis=1, inplace=True)
        
        ## creates a loop for pulling raw data##
        print_data = input('Would you like to review data that was used for this report?\nPlease select y/n.\n').lower()
        while True:
            try:
                if print_data =='y':
                    row = 0
                    section = 5
                    stop = 'y'
                    while row < len(df) and stop =='y':
                        print(df.iloc[row:row+section])
                        row +=section
                        stop = input('Would you like to view more data? y/n\n').lower()
                    else:
                        break
                else:
                    break
            except:
                break
  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
