import json
import random

try:
    with open("player.json") as file:
        player = json.load(file)
       
except FileNotFoundError:
       player= {}

def playgame(name):
    items = [
                {"name": "Apple", "description": "A round fruit with red or green skin and a white, juicy interior."},
                {"name": "Banana", "description": "A long, curved fruit with a yellow or green skin and soft, sweet flesh."},
                {"name": "Carrot", "description": "A long, thin, orange root vegetable with a crisp texture."},
                {"name": "Dog", "description": "A four-legged mammal with fur, a wagging tail, and a friendly disposition."},
                {"name": "Egg", "description": "An oval shaped, white, or brown, oval shaped food item that comes from chickens."},
                {"name": "Flower", "description": "A plant with brightly coloured petals and a sweet fragrance, often given as a gift."},
                {"name": "Guitar", "description": "A musical instrument with six strings and a hollow body, used for playing a variety of music."},
                {"name": "Hat", "description": "A head covering worn for warmth, protection from the sun or rain, or as a fashion accessory."},
                {"name": "Ice cream", "description": "A sweet, creamy frozen dessert made from milk, cream, and sugar."},
                {"name": "Jacket", "description": "A type of clothing worn on the upper body, typically made of a warm material."},
                {"name": "Kangaroo", "description": "A marsupial native to Australia, known for its powerful hind legs and tail used for hopping."},
                {"name": "Lemon", "description": "A small, round citrus fruit with a sour, acidic taste and a bright yellow skin."},
                {"name": "Moon", "description": "A natural satellite of the Earth, visible at night as a bright, round object in the sky."},
                {"name": "Newspaper", "description": "A printed publication containing news, articles, and information, often distributed daily."},
                {"name": "Ocean", "description": "A vast body of salt water that covers more than 70% of the Earth's surface."},
                {"name": "Pen", "description": "A writing instrument with a small, replaceable ink cartridge, used for writing on paper."},
                {"name": "Quilt", "description": "A type of bedding made of two layers of fabric stitched together with padding in between."},
                {"name": "Raccoon", "description": "A mammal with a distinctive black and white face, known for its intelligence and adaptability."},
                {"name": "Sunflower", "description": "A tall, yellow-flowered plant with large, ray-like petals and a dark central disk."},
                {"name": "Table", "description": "A piece of furniture with a flat top and one or more legs, used for supporting objects or holding things."},
                {"name": "Umbrella", "description": "A portable, collapsible canopy supported on a central pole, used for protection from rain or sun."},
                {"name": "Violin", "description": "A stringed musical instrument with four strings, held between the chin and shoulder and played with a bow."},
                {"name": "Watch", "description": "A small timepiece worn on the wrist or carried in a pocket, used for keeping track of time."},
                {"name": "Xylophone", "description": "A musical instrument consisting of a set of wooden bars that are struck with a mallet to produce musical tones."}
    ]
    select_items = random.sample(items, 6)

    for item in select_items:
        for i in range(3):
            answer = input(item["description"] + " What am I?")
            if answer.lower() == item["name"].lower():
                player[name]["score"]+= 1
                with open("player.json", "w") as file:
                    json.dump(player,file)
                print(f"Your score is: {player[name]['score']}" )
                break
            else:
                print("Incorrect. Try again.")
        else:  
            print("Game over.")
        
            break

def new_player():
    name=input("Enter your name: ")
    player[name] = {"score": 0}
    playgame(name)
    with open("player.json", "w") as file:
        json.dump(player,file)
    return name

def existing_player():
 
    name = input("Enter your name: ")
    if name in player :
        print(f"Welcome back,{name}.Your score is  {player[name]['score']}")
        playgame(name)
    else:
        print(f"Player {name} not found.")


def showleague():
  
    players_list = list(player.items())
    n = len(players_list) 


    for i in range(1, n):
        key = players_list[i]
        j = i - 1
        while j >= 0 and key[1]["score"] > players_list[j][1]["score"]:
            players_list[j + 1] = players_list[j]
            j -= 1
        players_list[j + 1] = key

    print("League Table: ", players_list)


def main():
    
  while True:
    print("Main menu:")
    print("1. League table")
    print("2. New player")
    print("3. Existing player")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
      print("League Table: ")
      showleague()
    elif choice == '2':
        new_player()
    elif choice == '3':
      existing_player()
    elif choice == '4':
      break
    else:
      print("Invalid choice.")

if __name__ == '__main__':
  main()
