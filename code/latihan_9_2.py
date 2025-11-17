hotel_rooms = [
    [" ", "X", " ", " ", "X"],  # Floor 0
    [" ", " ", " ", " ", " "],  # Floor 1
    ["X", " ", " ", "X", " "]   # Floor 2
]

while True:
    print("\n--- Pradita Hotel Manager ---")
    print("Commands: 'display', 'book', 'exit'")
    command = input("Enter your command: ").lower()

    if command == 'display':
        print("\nHotel Room Status:")
        num_rooms = len(hotel_rooms[0])
        idx_line = "Rooms: "
        for j in range(num_rooms):
            idx_line += f"[{j}] "
        print(idx_line)
        print("-" * len(idx_line))
        for i, floor in enumerate(hotel_rooms):
            line = f"Floor {i}: "
            for cell in floor:
                line += f"[{cell}] "
            print(line)

    elif command == 'book':
        print("\nBook a new room:")
        try:
            floor_num = int(input("Enter floor number: "))
            room_num = int(input("Enter room number: "))
        except ValueError:
            print("Invalid input. Enter numeric floor and room numbers.")
            continue

        if not (0 <= floor_num < len(hotel_rooms) & 0 <= room_num < len(hotel_rooms[0])):
            print("Invalid floor and room number.")
            continue
        if not (0 <= floor_num < len(hotel_rooms)):
            print("Invalid floor number.")
            continue
        if not (0 <= room_num < len(hotel_rooms[0])):
            print("Invalid room number.")
            continue

        if hotel_rooms[floor_num][room_num] == "X":
            print("That room is already booked.")
        else:
            hotel_rooms[floor_num][room_num] = "X"
            print(f"Room booked: Floor {floor_num}, Room {room_num}.")

    elif command == 'exit':
        print("Goodbye!")
        break

    else:
        print("Invalid command. Please try again.")
