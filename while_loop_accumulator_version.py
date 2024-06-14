def get_starting_number():
    counter = 1
    while counter >= 1:
        response = input("With how many bottles of beer on the wall would you like to start? ").strip()
        if response.isnumeric() is False or int(response) < 1:
            print("Invalid response.")
            counter += 1
        else:
            return int(response)

def sing(number_of_bottles):
    """
    @param number_of_bottles the number of bottles of beer on the wall at the beginning of the song
    """ 
    while number_of_bottles > 0:
        if number_of_bottles == 1:
            lyrics = "{x} bottle of beer on the wall, {x} bottle of beer.\nTake it down, pass it around, {y} bottles of beer on the wall!".format(x = number_of_bottles, y = "no more")
            print(lyrics)
            number_of_bottles -= 1
        elif number_of_bottles == 2:
            lyrics = "{x} bottles of beer on the wall, {x} bottles of beer.\nTake one down, pass it around, {y} bottle of beer on the wall.\n".format(x = number_of_bottles, y = number_of_bottles - 1)
            print(lyrics)
            number_of_bottles -= 1
        else:
            lyrics = "{x} bottles of beer on the wall, {x} bottles of beer.\nTake one down, pass it around, {y} bottles of beer on the wall.\n".format(x = number_of_bottles, y = number_of_bottles - 1)
            print(lyrics)
            number_of_bottles -= 1