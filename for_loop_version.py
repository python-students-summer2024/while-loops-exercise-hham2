def get_starting_number():
    list = [0]
    for i in list:
        response = input("With how many bottles of beer on the wall would you like to start? ")
        if response.isnumeric() is False or int(response) < 1:
            print("Invalid response.")
            list.append(0)
        else:
            return int(response)

def sing(number_of_bottles):
    """
    @param number_of_bottles the number of bottles of beer on the wall at the beginning of the song
    """ 
    num_bottles = number_of_bottles
    lyrics = "{x} bottles of beer on the wall, {x} bottles of beer.\nTake one down, pass it around, {y} bottles of beer on the wall.".format(x = number_of_bottles, y = number_of_bottles - 1)
    for i in range(number_of_bottles):
        if number_of_bottles == 1:
            lyrics = "{x} bottle of beer on the wall, {x} bottle of beer.\nTake one down, pass it around, {y} bottles of beer on the wall.".format(x = number_of_bottles, y = "no more")
            print(lyrics)
            break
        elif number_of_bottles == 2:
            lyrics = "{x} bottles of beer on the wall, {x} bottles of beer.\nTake one down, pass it around, {y} bottle of beer on the wall.".format(x = number_of_bottles, y = number_of_bottles - 1)
            print(lyrics.format())
            number_of_bottles -= 1
        else:
            print(lyrics.format(x = number_of_bottles, y = number_of_bottles - 1))
            number_of_bottles -= 1

sing(5)