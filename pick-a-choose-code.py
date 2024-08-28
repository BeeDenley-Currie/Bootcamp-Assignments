import random
import requests
import csv
import time
#installation of ASCII MAGIC - taken from internet to enable us to show the photo of the Pokémon
from ascii_magic import AsciiArt


def instructions():
  """  Print the game instructions to the screen."""
  print("_______________________________")
  print("Welcome to Pokémon Top Trumps!")
  print("_______________________________")
  print()
  print("INSTRUCTIONS:")
  print(
      "1. You will be given a random Pokémon card with different stats. Select one of the stats."
  )
  print("2. Another random card is selected for your opponent (the computer).")
  print("3. The stats of the two cards are compared.")
  print("4. The player with the higher stat wins.")
  print("Good luck!")
  print()


def random_pokemon():
  """ Generate a random number between 1 and 151 to use as the Pokémon ID number.
  Using the Pokémon API get a Pokémon based on its ID number.
  Create a dictionary that contains the returned Pokémon's stats.
  """
  pokemon_number = random.randint(1, 151)
  url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
  response = requests.get(url)
  pokemon = response.json()

  return {
      'name': pokemon['name'],
      'id': pokemon['id'],
      'height': pokemon['height'],
      'weight': pokemon['weight'],
      'experience': pokemon['base_experience'],
      #line added to enable print from internet
      'image_url': pokemon['sprites']['front_default']
  }


def print_image(url):
  """ Download an image from url, convert it to Ascii Art 
  and print it to the screen.
  :param url: is the url of the pokémon Ascii image
  """
  # Download the image
  img_data = requests.get(url).content
  # Save the image to tmp.jpg file
  with open('tmp.jpg', 'wb') as image:
    image.write(img_data)
  # Convert the file into Ascii Art and print
  AsciiArt.from_image("tmp.jpg").to_terminal()


def highscore(player_name, count_wins):
  """ Record the players' scores, store them in a file 
  and print the top 5 scores to the screen.
  :param player_name: is the name of the player.
  :param count_wins: is the number of rounds the player has won at the end of a game.
  """
  # empty list for the new player score
  newscore_list = []
  # adding the player's name and score to the newscore list
  newscore_list.append({'player': player_name, 'score': count_wins})

  # add the header (player,score) to the csv file when it writes to the file for the first time
  # append new score to the csv file with all the scores
  with open('highscore.csv', 'a') as csv_file:
    field_names = ['player', 'score']
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    if csv_file.tell() == 0:
      spreadsheet.writeheader()
    spreadsheet.writerows(newscore_list)

  # read the dictionary with the updated scores
  # create a list of dictionaries with the updated scores
  with open('highscore.csv', 'r') as csv_file:
    fullscores_list = []
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
      fullscores_list.append(row)

  # sort the updated scores list in order of higher to lower score and print it to the screen
  print('_____________')
  print('TOP 5 SCORES:')
  fullscoressorted_list = sorted(fullscores_list,
                                 key=lambda x: x['score'],
                                 reverse=True)
  for row in fullscoressorted_list[:5]:
    print('{} - {}'.format(row['player'], row['score']))
  print('_____________')


def choose_stat():
  """Ask user to choose a stat and return the stat name.
  Allow to choose the stat just by typing the first character or the whole name.
  Ask again if the input is invalid.
  """
  stat = None
  stats = ["id", "height", "weight", "experience"]
  while stat not in stats:
    stat_choice = input(
        "Which stat do you want to use? ([i]d, [h]eight, [w]eight, [e]xperience) "
    ).lower()
    stat = {s[0]: s for s in stats}.get(stat_choice, stat_choice)
  return stat


  # We were printing the stats in 2 places for my_pokemon and opponent_pokemon so
  # We turned it into a function and used it on those 2 places
def print_stats(pokemon):
  """Print the stats of a given pokémon."""
  # adding tab to the results
  # We split a string into several strings and they act as one
  # We named the placeholders then use named arguments in .format() individually
  print("\tID: {id} \n"
        "\tHeight: {height} \n"
        "\tWeight: {weight} \n"
        "\tExperience: {experience}".format(id=pokemon['id'],
                                            height=pokemon['height'],
                                            weight=pokemon['weight'],
                                            experience=pokemon['experience']))


def run():
  """ Main game loop.
  Prompt the player for number of rounds.
  Run the rounds, comparing the selected stat.
  Work out the winner for each round.
  Save the player score and present the top 5 scores.
  """

  instructions()
  count_wins = 0

  # Ask the user how many rounds to play.
  # Check if the input is numeric and convert it to an integer.
  # If it is  numeric, come out of the loop.
  # If it is not numeric, ask the user to enter a number and start the loop again.
  while True:
    rounds_str = input('How many rounds do you want to play? ')
    if rounds_str.isnumeric():
      break
    else:
      print("Please, enter a number.")
  rounds_input = int(rounds_str)

  # Loop for each round
  for i in range(1, rounds_input + 1):
    print()
    print('ROUND NUMBER {}:'.format(i))
    print()

    # generate player's pokémon
    my_pokemon = random_pokemon()
    print('You were given {}.'.format(my_pokemon['name'].title()))
    # .title() capitalizes the first letter of the string
    time.sleep(2)
    # print player's pokémon image and stats
    print_image(my_pokemon["image_url"])
    time.sleep(2)
    print("Your stats are: ")
    print_stats(my_pokemon)
    # adding indentation to the printed stats. See function explanation above
    print()

    # Player chooses the stat to play with
    # input: turn the question into the function that give shortcut and handle error when the user input is invalid. See function explanation above
    stat_choice = choose_stat()

    # Generate the opponent's (computer) pokémon
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}.'.format(opponent_pokemon['name'].title()))
    # .tite() capitalizes the first letter of the string
    time.sleep(2)
    # print opponent's (computer) pokémon image and stats
    print_image(opponent_pokemon["image_url"])
    time.sleep(2)
    print("The opponent's stats are: ")
    print_stats(opponent_pokemon)
    print()

    # get stat for player and opponent (computer) and print them to the screen
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    print("Your {} is {}. Your opponent's {} is {}.".format(
        stat_choice, my_stat, stat_choice, opponent_stat))

    # compare player and opponent stat (the largest value wins)
    # add color to the print
    if my_stat > opponent_stat:
      count_wins += 1
      print("\n\033[92m You Win!\033[00m")
    elif my_stat < opponent_stat:
      print("\n\033[91m You Lose!\033[00m")
    else:
      print("\n\033[93m Draw!\033[00m")

    # Print how many rounds the player has won
    print("\nYou have won {} of {} rounds\n".format(count_wins, rounds_input))

  # All rounds of the game have finished.
  # The player enters their name, which is stored in the highscore file
  player_name = input('Please, enter your name: ')
  highscore(player_name, count_wins)


# call run function
run()

# ask the user if they want to keep playing.
# If yes, continue playing. If not, print the message "bye!"
while input("Do you want to play again? y/n ") in ['y', 'Y']:
  run()
print("bye!")
