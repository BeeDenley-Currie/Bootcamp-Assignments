import random
import requests

# I decided to make a console application that will return either a historical event, birth, or death, for
# a given day. This uses the zenquotes api, which is free and requires no key. I am calling all the Event, Birth, and Death info from the API

def instructions():
    # printing the instructions for how to use the app
    print("_______________________________")
    print("Welcome to 'On This Day'!")
    print("_______________________________")
    print()
    print("INSTRUCTIONS:")
    print("1. You will enter your chosen date")
    print("2. Choose whether you would like to see a historical event, birth, or death")
    print("3. A fun fact is printed, and written to a log .txt file")
    print("You then have the option to rerun with another date or to end the program")
    print("Historical data provided by https://zenquotes.io/")
    print("Enjoy!"+"\n")

def date_info():
    # user inputs date as string, use string slicing to extract necessary parts for URL
    # Gets the zenquotes On This Day API. No need to log in/authenticate
    # creates a dictionary that contains the facts to print
    date = input("What date would you like to search? Use format DD/MM: ")
    day = date[0:2]
    month = date[3:5]
    global on_day
    on_day = f"Day: {day}, Month: {month}"
    url = 'https://today.zenquotes.io/api/{}/{}'.format(month, day)
    response = requests.get(url)
    data = response.json()
    return {
        'Event': data['data']['Events'],
        'Birth': data['data']['Births'],
        'Death': data['data']['Deaths']
    }

def choice():
    option = input("Would you like an Event, Birth, or Death? ")
    # using if statement for data validation, loops function until valid input used
    if option not in ["Event", "Birth", "Death"]:
        print("Sorry, I need the format either Event, Birth, or Death")
        choice()
    else:
        # using the length of the option list to form the range for random number generation. import random at start allows us to use randrange
        random_index = random.randrange(len(my_date[option]))
        # get the value for the text key in this random dictionary
        random_item = my_date[option][random_index]['text']
        # split on a character used in all the text json fields, normally to give colour information
        # this also removes these unneeded characters - bonus!
        output_list = random_item.split(" &#8211; ")
        #if statement to add different value to fun_fact variable depending on option chosen, cuts down on recursive code
        if option == "Event":
                fun_fact = f"Fun fact! On this day in {output_list[0]}, {output_list[1]}"+"\n"
        elif option == "Birth":
                fun_fact = f"Fun Fact! On this day in {output_list[0]}, {output_list[1]} was born"+"\n"
        elif option == "Death":
                fun_fact = f"...somewhat Fun Fact! On this day in {output_list[0]}, {output_list[1]} died"+"\n"
        # originally I only wrote to the text file, but it wasn't immediately clear that everything had worked.
        # this way it's more obvious if there's an error, and is also a reminder to view the log file
        print(fun_fact + "\nThis has been written to the On This Day log\n")
        with open("on_this_day.txt", "a+") as otd:
            otd.write(fun_fact)
            otd.seek(0, 2)

# Function for running the On This Day output
def run():
    global my_date
    my_date = date_info()
    with open("on_this_day.txt", "a+") as otd:
        otd.write(on_day+"\n")
        otd.seek(0,2)
    choice()

instructions()
run()
# ask the user if they want to keep going.
# If yes, run again. If not, print the message "bye!"
while input("Do you want to go again? y/n: ") in ['y', 'Y']:
  run()
print("bye!")
