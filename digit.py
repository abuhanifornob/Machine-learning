class Digit:
    def zero(self):
        for row in range(5):
            for col in range(5):
                if (col == 4 or col == 0) or ((row == 0 or row == 4) and (col > 0 and col < 4)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()


    # ......................... 1.....................
    def one(self):
        for row in range(6):
            for col in range(5):
                if col == 3:
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # .............. 2...............
    def two(self):
        for row in range(5):
            for col in range(5):
                if (row == 0 or row == 2 or row == 4) or (col == 4 and row == 1) or (col == 0 and row == 3):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # ......................3.....................
    def three(self):
        for row in range(5):
            for col in range(5):
                if (row == 0 or row == 2 or row == 4) or (col == 4 and row == 1) or (col == 4 and row == 3):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # ...............4................
    def four(self):
        for row in range(5):
            for col in range(5):
                if col == 4 or (row == 2 and col < 4) or (col == 0 and row < 2):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # ....................5.............
    def five(self):
        for row in range(5):
            for col in range(5):
                if (row == 0 or row == 2 or row == 4) or (col == 0 and row == 1) or (col == 4 and row == 3):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # ......................6.......................
    def six(self):
        for row in range(5):
            for col in range(5):
                if col == 0 or ((row == 0 or row == 2 or row == 4) and col > 0) or (col == 4 and row == 3):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # ................7...................
    def seven(self):
        for row in range(5):
            for col in range(5):
                if col == 4 or ((row == 0 or row == 2) and col < 4):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # .................8..................
    def eight(self):
        for row in range(5):
            for col in range(5):
                if (col == 4 or col == 0) or ((row == 0 or row == 2 or row == 4) and (col > 0)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    # .................9........................

    def nine(self):
        for row in range(5):
            for col in range(5):
                if (col == 4) or ((row == 0 or row == 2 or row == 4) and (col < 4)) or (col == 0 and row == 1):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()