def discreet_card(number):
        new_number = ""
        stars = "*"
        for star in range(len(number)-4):
            new_number = new_number + stars
        for digit in range(len(number)-4, len(number)):
            new_number = new_number + number[digit]
        print(new_number)
discreet_card("4556364607935616")

