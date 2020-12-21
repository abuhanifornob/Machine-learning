class Letter:
    def __init__(self):
        pass
    def A(self):
        for row in range(7):
            for col in range(5):
                if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def B(self):
        for row in range(7):
            for col in range(5):
                if ((col == 0) or (col == 4 and row != 3 and row != 0 and row != 6)) or (
                        (row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def C(self):
        for row in range(7):
            for col in range(5):
                if ((col == 0) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and (col > 0)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def D(self):
        for row in range(7):
            for col in range(5):
                if ((col == 0 or col == 4) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col < 4)):
                    print("*", end=' ')
                else:
                    print(end="  ")
            print()

    def E(self):
        for row in range(7):
            for col in range(5):
                if (col == 0) or ((row == 0 or row == 3 or row == 6) and (col > 0)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def F(self):
        for row in range(7):
            for col in range(5):
                if (col == 0) or ((row == 0 or row == 3) and col > 0):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def G(self):
        for row in range(7):
            for col in range(6):
                if (col == 0) or (col == 4 and (row != 1 and row != 2)) or \
                        ((row == 0 or row == 6) and (col > 0 and col < 5)) or (row == 3 and (col == 3 or col == 5)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def H(self):
        for row in range(7):
            for col in range(5):
                if (col == 0 or col == 4) or (row == 3 and (col > 0 and col < 4)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def I(self):
        for row in range(7):
            for col in range(5):
                if (row == 0 or row == 6) or (col == 2 and (row != 0 or row != 6)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def J(self):
        for row in range(7):
            for col in range(5):
                if (row == 0) or (col == 2 and (row != 0)) or (row == 6 and (col == 0 or col == 1)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def K(self):
        i = 0
        j = 4
        for row in range(7):
            for col in range(5):
                if (col == 0) or (row == col + 2 and col > 1):
                    print("k", end=" ")
                elif ((row == i and col == j) and col > 0):
                    print("k", end=" ")
                    i += 1
                    j -= 1
                else:
                    print(end="  ")
            print()

    def L(self):
        for row in range(7):
            for col in range(5):
                if col == 0 or (row == 6 and col > 0):
                    print("l", end=" ")
                else:
                    print(end="  ")
            print()

    def M(self):
        for row in range(7):
            for col in range(7):
                if (col == 0 or col == 6) or (row == col and (row > 0 and col < 4)) or \
                        (row == 1 and col == 5) or (row == 2 and col == 4):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def N(self):
        for row in range(6):
            for col in range(6):
                if (col == 0 or col == 5) or (row == col and (col > 0 and col < 5)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def O(self):
        for row in range(7):
            for col in range(5):
                if ((col == 0 or col == 4) and (row != 0 and row != 6)) or (
                        (row == 0 or row == 6) and (col > 0 and col < 4)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def P(self):
        for row in range(7):
            for col in range(5):
                if col == 0 or ((row == 0 or row == 3) and (col > 0 and col < 4)) or (row == 1 and col == 4) or (
                        row == 2 and col == 4):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def Q(self):
        for row in range(8):
            for col in range(5):
                if ((col == 0 or col == 4) and (row > 0 and row < 6)) or (row == 0 and col > 0 and col < 4) or (
                        col == 2 and row == 6) \
                        or (col == 1 and row == 5) or (col == 1 and row == 6) or (col == 3 and row == 6) or (
                        col == 3 and row == 7):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def R(self):
        for row in range(7):
            for col in range(5):
                if ((col == 0) or (row == 0 or row == 3) and (col > 0 and col < 4)) or (
                        col == 4 and (row != 0 and row != 3)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def S(self):
        for row in range(7):
            for col in range(5):
                if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)) or (
                        col == 0 and (row == 1 or row == 2)) \
                        or (col == 4 and (row == 4 or row == 5)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def T(self):
        for row in range(6):
            for col in range(5):
                if (row == 0) or (col == 2 and row > 0):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def U(self):
        for row in range(7):
            for col in range(5):
                if ((col == 0 or col == 4) and row != 6) or row == 6 and (col > 0 and col < 4):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def V(self):
        i = 0
        j = 6
        for row in range(4):
            for col in range(7):
                if (col == row):
                    print("*", end=" ")
                elif (row == i and col == j):
                    print("*", end=" ")
                    i += 1
                    j -= 1

                else:
                    print(end="  ")
            print()

    def W(self):
        i = 0
        j = 3
        for row in range(4):
            for col in range(7):
                if (col == 0 or col == 6):
                    print("*", end=" ")
                elif (row == i and col == j):
                    print("*", end=" ")
                    i += 1
                    j -= 1
                elif (row == 1 and col == 4) or (row == 2 and col == 5):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def X(self):
        i = 0
        j = 4
        for row in range(5):
            for col in range(5):
                if row == col:
                    print("*", end=' ')
                elif ((row == i and col == j)):
                    print("*", end=' ')
                    i += 1
                    j -= 1
                elif (row == 3 and col == 1) or (row == 4 and col == 0):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def Y(self):
        for row in range(5):
            for col in range(5):
                if ((col == row) and col < 3) or (col == 2 and row > 2) or (col == 4 and row == 0) or (
                        col == 3 and row == 1):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()

    def Z(self):
        i = 1
        j = 4
        for row in range(7):
            for col in range(7):
                if (row == 0 or row == 6):
                    print("*", end=" ")
                elif (row == i and col == j):
                    print("*", end=" ")
                    i += 1
                    j -= 1
                else:
                    print(end="  ")
            print()