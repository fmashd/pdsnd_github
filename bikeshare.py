import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\tHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nPlease enter the city you want to Explore from: the cities are chicago, new york or washington')
    city = input('\tType Here : ').lower()
    while True:     
            if city == 'chicago':
                print("\nChicago City! Okay Let's go further\n")
                break
            if city == 'new york':
                print("\nNew York City! Okay let's go further\n")
                break
            elif city == 'washington':
                print("\nWashington! Okay let's go further\n")
                break
            else:
                print('\nPlease enter within this cities chicago, new york or washington\n')
                city = input('Please choose the city for which you would like to see the Statistics: ')
                city = city.lower()
    
    # get user input for month (all, january, february, ... , june)
    #print('Would you live to filter the Data by month, day, both or not? type "none" for no time filter')
    
    print('\nEnter the Month you want to analyze Data from : january, february, march, april, may, june')  
    month = input('\tType Here : ').lower()
    while True:
            if month == 'january':
                print("\nYou Picked the month of JANUARY \n")
                break
            if month == 'february':
                print("\nYou Picked the month of FEBRUARY \n")
                break
            if month == 'march':
                print("\nYou Picked the month of MARCH \n")
                break
            if month == 'april':
                print("\nYou Picked the month of APRIL \n")
                break
            if month == 'may':
                print("\nYou Picked the month of MAY \n")
                break
            elif month == 'june':
                print("\nYou Picked the month of June \n")
                break
            else:
                print('\nWRONG INPUT ENTER MONTHS WITHIN january, february, march, april, may, june\n')
                month = input('\tType Here : ').lower()
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nEnter the Day you want to analyze Data from : monday, tuesday, wednesday, thursday, friday, saturday, sunday')
    day = input('\tType Here : ').lower()
    while True:
            if day == 'monday':
                print("\nYou Picked MONDAY \n")
                break
            if day == 'tuesday':
                print("\nYou Picked TUESDAY\n")
                break
            if day == 'wednesday':
                print("\nYou Picked WEDNESDAY\n")
                break
            if day == 'thursday':
                print("\nYou Picked THURSDAY\n")
                break
            if day == 'friday':
                print("\nYou Picked FRIDAY\n")
                break
            if day == 'saturday':
                print("\nYou Picked SATURDAY\n")
                break
            elif day == 'sunday':
                print("\nYou Picked SUNDAY\n")
                break
            else:
                print('\nWRONG INPUT ENTER DAYS WITHIN monday, tuesday, wednesday, thursday, friday, saturday, sunday\n')
                day = input('\tType Here : ').lower()

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]


    if day != 'all':
        
        df = df[ df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n\nCalculating Ststistic of Times...\n')
    start_time = time.time()

    # display the most common month
    mstcom_month = df['month'].value_counts().idxmax()
    print("Most common month is :", mstcom_month)

    # display the most common day of week
    mstcom_day = df['day_of_week'].value_counts().idxmax()
    print("Most common day of week is :", mstcom_day)

    # display the most common start hour
    mstcom_start_hour = df['hour'].value_counts().idxmax()
    print("Most common start hour is :", mstcom_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\nCalculating Statistic of Stations...\n')
    start_time = time.time()

    # display most commonly used start station
    mstcom_start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station :", mstcom_start_station)


    # display most commonly used end station
    mstcom_end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used end station :", mstcom_end_station)

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    mstcom_start_end_station = df['Start End'].value_counts().idxmax()
    print("Most freqent combination of start station and end station : ", mstcom_start_end_station)

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Statistic of Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time Statistic:", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time Statistic:", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n\nCalculating Statistic of User...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of User Types Statistic:\n")
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    
    print()
    
    # Display counts of gender
    print()
    if 'Gender' not in df:
        print("There is no gender data for this city \n")
    else:
        print("Counts of Gender Statistic:\n")
        gender_counts = df['Gender'].value_counts()
        for index,gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))
    
    print()

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("Data related to birth year of users is not available for this city.\n")
    else:
        print("\n Earliest year of birth")
        print(max(df['Birth Year']))
        print("\n Most recent year of birth")
        print(min(df['Birth Year']))     
        print("\n Most common year of birth")
        print(df['Birth Year'].mode())   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#This function was not there at first like others it was type to diplay data of at user request
def display_data(df):
    choice = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()
    if choice=='yes' or choice=='y' or choice=='yus':
        choice=True
    elif choice=='no' or choice=='n' or choice=='nope':
        choice=False
    else:
        print('You did not enter a valid choice. Let\'s try that again. ')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Another five? Yes/No ').lower()
            if choice=='yes' or choice=='y' or choice=='yus':
                continue
            elif choice=='no' or choice=='n' or choice=='nope':
                break
            else:
                print('You did not enter a valid choice.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
