class game_map:
    def __init__(self, map_file, guard_file):
        try:
            # function created to read content of file containing map
            self.map_grid = self.get_map(map_file)
            # the list of guard objects is created
            self.guard_list = []
            # created method to read txt with guards attributes and save to list
            self.guard_list = self.get_guard_from_file(guard_file)
            print(self.guard_list)
            self.row_player = 0
            self.col_player = 0
            # Save the start location of Player
            map_list = self.get_grid()
            for i in range(len(map_list)):
                for j in range(len(map_list[i])):
                    if map_list[i][j] == 'P':
                        self.row_player = i
                        self.col_player = j
                        self.map_grid = self.map_grid.replace('P', ' ')
                    # saves the coordinates of exit
                    if map_list[i][j] == 'E':
                        self.exit = (i, j)
        except FileNotFoundError:
            print("File could not be found")
            quit()
        except NameError:
            print("Error, variable is not found")
            quit()

    # get_grid function is used to create a 2d list and return it
    def get_grid(self):
        # create 2d list from the lists of self.map_grid
        self.map_grid
        map_list2d = []
        map_list1d = [one_char for one_char in self.map_grid]
        x = 0
        row = 16
        for i in range(12):
            map_list2d.append(map_list1d[x:row])
            x = x + 16
            row = row + 16
        guard_list = self.get_guards()
        # adds the guards and player to the list
        for the_guard in guard_list:
            map_list2d[the_guard.row][the_guard.col] = 'G'
        map_list2d[self.row_player][self.col_player] = 'P'
        # returns the 2d list of map
        return map_list2d

    # get_guards function is used to get the list of guards
    def get_guards(self):
        # has no parameter
        # returns the list of guards
        return self.guard_list

    # update_player function is used to update the location of player and save the coordinates
    def update_player(self, direction):
        # The direction that is passed as parameter is checks which one it is
        # based on direction the row or column is changed
        if direction == 'L':
            new_player_location = (self.row_player, self.col_player - 1)
        elif direction == 'R':
            new_player_location = (self.row_player, self.col_player + 1)
        elif direction == 'U':
            new_player_location = (self.row_player - 1, self.col_player)
        elif direction == 'D':
            new_player_location = (self.row_player + 1, self.col_player)
        # the get_grid method is called
        current_grid = self.get_grid()
        # this checks if there is a wall or the exit to where the payer want's to move
        # if it is true to either statements then the new coordinates are saved
        if current_grid[new_player_location[0]][new_player_location[1]] == ' ' or \
                current_grid[new_player_location[0]][new_player_location[1]] == 'E':
            self.row_player = new_player_location[0]
            self.col_player = new_player_location[1]

    # update_guards functions updates the guards location
    def update_guards(self):
        # loop through the guard list
        for tmp_guard in self.get_guards():
            # calls the move function to get the new position of guards
            new_location = guard.move(tmp_guard, self.get_grid())
            # saves the new row and col
            tmp_guard.row = new_location[0]
            tmp_guard.col = new_location[1]

    # player_wins function is used to determine if the player has reached the exit
    def player_wins(self):
        # checks if player is on the exit square
        if self.row_player == self.exit[0] and self.col_player == self.exit[1]:
            return True
        else:
            return False

    # player_losses function is used to determine if the player has lost the game
    def player_loses(self):
        # loop through guards
        for the_guard in self.get_guards():
            # calls the enemy_in_range function to determine if the player is within range
            loses = guard.enemy_in_range(the_guard, self.row_player, self.col_player)
            if loses:
                return True
        else:
            return False

    def get_map(self, map_file):
        # opens the file to read and save the txt files map information
        # this with open does not require to use close()
        with open(map_file, 'r') as file:
            # saves the map as a string
            map_grid = file.read()
            # prints the grid for the tutorial assignment part
            print(map_grid)
            # from the string the \n is taken out
            map_grid = map_grid.replace('\n', '')
            return map_grid

    def get_guard_from_file(self, guard_file):
        # read the txt file containing the guard information
        # this with open does not require to use close()
        with open(guard_file, 'r') as file:
            # saves the info as a list
            # each value is a guard
            guard_file_contents = file.readlines()
        guard_list = []
        for x in guard_file_contents:  # x is each line saved in list
            guard_attributes = x.replace('\n', '').split(' ')  # saves each character into list
            # movement list
            # creates a new object guard for each guard in the txt file
            # sends the parameters of row, column, attack range, and movements
            new_guard = guard(guard_attributes[0], guard_attributes[1], guard_attributes[2], guard_attributes[3:])
            # saves all objects in list
            guard_list.append(new_guard)
        return guard_list


#############################################


class guard:
    def __init__(self, row, col, attack_range, movements):
        self.row = int(row)
        self.col = int(col)
        self.attack_range = int(attack_range)
        self.movements = movements
        self.move_index = 0  # used later to determine which direction the guard moves in

    # get_location is used to determine the location of guard
    def get_location(self):
        guard_location = (self.row, self.col)
        # Returns: a tuple of (int, int), representing
        # the row and column of this guard's current location
        return guard_location

    # move function is used to move the guard by one square according to the next command on the movement list
    def move(self, current_grid):
        # index needs to reset to zero
        self.move_index  # move index to loop through each time
        self.movements  # movements list of guard
        current_grid  # the grid location to see if there is a wall or not
        new_location = []

        # get new location of guard (maybe put into function)
        if self.movements[self.move_index] == 'L':
            new_location = [self.row, self.col - 1]
        elif self.movements[self.move_index] == 'R':
            new_location = [self.row, self.col + 1]
        elif self.movements[self.move_index] == 'U':
            new_location = [self.row - 1, self.col]
        elif self.movements[self.move_index] == 'D':
            new_location = [self.row + 1, self.col]
        # checks that the space on the grid is empty and within range
        if current_grid[new_location[0]][new_location[1]] == ' ':
            if self.move_index + 1 < len(self.movements):
                self.move_index += 1
            else:
                self.move_index = 0
            return new_location[0], new_location[1]
        else:
            if self.move_index + 1 < len(self.movements):
                self.move_index += 1
            else:
                self.move_index = 0
            return self.row, self.col

    # get_far_left function is used to determine the far left col is within range of the grid
    def get_far_left(self, guard_col, guard_attack):
        within_range = False
        while not within_range:
            # checks if it does not go into the negatives as it will cause out of bounds
            if (guard_col - guard_attack) >= 0:
                what_is_being_returned = guard_col - guard_attack
                return what_is_being_returned
            guard_col = guard_col + 1
        return guard_col

    # get_far_right function is used to determine if the far right col is within range of grid
    def get_far_right(self, guard_col, guard_attack):
        within_range = False
        while not within_range:
            # checks if it does not go beyond the grid size of 16
            if (guard_col + guard_attack) <= 16:
                what_is_being_returned = guard_col + guard_attack
                return what_is_being_returned
            guard_col = guard_col - 1
        return guard_col

    # enemy_in_range function is used to check if player is within shooting range of guards
    def enemy_in_range(self, enemy_row, enemy_col):
        # save the guards' col, row and attack range in variables so that we can manipulate it
        upper_guard_col = self.col
        upper_guard_row = self.row
        upper_guard_attack = self.attack_range

        # this is for loop for the upper part of the diamond
        for i in range(0, self.attack_range + 1):
            # check if the attack range is within bounds of grid
            far_left_column = self.get_far_left(upper_guard_col, upper_guard_attack)
            far_right_column = self.get_far_right(upper_guard_col, upper_guard_attack)

            # keeps looping as long as the far left col is not bigger then the right col
            # this creates the pyramid shape
            while far_left_column <= far_right_column:
                # checks if the players location is within the guards shooting range
                if upper_guard_row == enemy_row and far_left_column == enemy_col:
                    return True
                # moves the left column one in and checks the whole row
                far_left_column = far_left_column + 1
            # makes sure that row and attack don't go into negatives
            if upper_guard_row > 0 and upper_guard_attack > 0:
                # subtracts row minus one to move the shooting range row checking
                upper_guard_row = upper_guard_row - 1
                # makes the attack range smaller and allows to checks next row and make it smaller
                #####
                ###
                upper_guard_attack = upper_guard_attack - 1

        # lower part of diamond
        # save the guards' col, row and attack range in variables so that we can manipulate it
        # doesn't use the same ones as upper do to starting again from initial number
        lower_guard_col = self.col
        lower_guard_row = self.row + 1
        lower_guard_attack = self.attack_range - 1

        # this is for loop for the lower part of the diamond
        for x in range(0, self.attack_range):
            # check if the attack range is within bounds of grid
            far_left_column = self.get_far_left(lower_guard_col, lower_guard_attack)
            far_right_column = self.get_far_right(lower_guard_col, lower_guard_attack)
            # keeps looping as long as the far left col is not bigger then the right col
            # this creates the pyramid shape
            while far_left_column <= far_right_column:
                # checks if the players location is within the guards shooting range
                if lower_guard_row == enemy_row and far_left_column == enemy_col:
                    return True
                # moves the left column one in and checks the whole row
                far_left_column = far_left_column + 1
                # makes sure it does not go out of bounds of grid
            if lower_guard_row <= 12 and lower_guard_attack > 0:
                # adds row plus one to move the shooting range row checking
                lower_guard_row = lower_guard_row + 1
                # makes the attack range smaller and allows to checks next row and make it smaller
                #####
                ###
                lower_guard_attack = lower_guard_attack - 1
