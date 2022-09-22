def discreet_card(number):
        new_number = ""
        stars = "*"
        for star in range(len(number)-4):
            new_number = new_number + stars
        new_number = new_number + number[:-4]
        return(new_number)
print(discreet_card("4556364607935616"))

