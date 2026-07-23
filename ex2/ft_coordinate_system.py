import math

def get_player_pos() -> None:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(',')
        
        if len(parts) != 3:
            print("Invalid syntax")
            continue
            
        coords = []
        valid = True
        for p in parts:
            p_clean = p.strip()
            try:
                coords.append(float(p_clean))
            except ValueError:
                print(f"Error on parameter '{p_clean}': could not convert string to float: '{p_clean}'")
                valid = False
                break   
        if valid:
            return tuple(coords)

print("=== Game Coordinate System ===")
print("Get a first set of coordinates")
pos1 = get_player_pos()

print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
print(f"Distance to center: {round(dist_center, 4)}")

print("Get a second set of coordinates")
pos2 = get_player_pos()

dist_between = math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 + (pos2[2]-pos1[2])**2)
print(f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}")