import random

def get_turn(data, empty = " "):
    win_list = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [2, 4, 6], [0, 4, 8]
    ]

    for line in win_list:
        vals = [data[i] for i in line]
        # Win if we can
        if vals.count("O") == 2 and vals.count(empty) == 1:
            return line[vals.index(empty)]
        
    for line in win_list:
        vals = [data[i] for i in line]
        # Block adversaire turn
        if vals.count("X") == 2 and vals.count(empty) == 1:
            return line[vals.index(empty)]
        
    for line in win_list:
        vals = [data[i] for i in line]
        # Continue line
        if vals.count("O") == 1 and vals.count(empty) == 2:
            return line[vals.index(empty)]
        
    # Place in center
    if data[4] == empty:
        return 4
        
    # Place in corner
    corners = [0, 2, 6, 8]
    free_corners = [c for c in corners if data[c] == empty]
    if free_corners:
        return random.choice(free_corners)
            
    free_place = [i for i, val in enumerate(data) if val ==  empty]
    if free_place:
        return random.choice(free_place)
    else: 
        return - 1   