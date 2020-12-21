from letter import Letter
from digit import Digit

letter = Letter()
digit=Digit()
userchose=input(" Hellow World! please Enter Letter(A-Z) or Digit(0- 9):> ").upper()

while True:
    if userchose == 'A':
        letter.A()
    elif userchose == 'B':
        letter.B()
    elif userchose == 'C':
        letter.C()
    elif userchose == 'D':
        letter.D()
    elif userchose == 'E':
        letter.E()
    elif userchose == 'F':
        letter.F()
    elif userchose == 'G':
        letter.G()
    elif userchose == 'H':
        letter.H()
    elif userchose == 'I':
        letter.I()
    elif userchose == 'J':
        letter.J()
    elif userchose == 'K':
        letter.K()
    elif userchose == 'L':
        letter.L()

    elif userchose == 'M':
        letter.M()
    elif userchose == 'N':
        letter.N()
    elif userchose == 'O':
        letter.O()
    elif userchose == 'P':
        letter.P()
    elif userchose == 'Q':
        letter.Q()
    elif userchose == 'R':
        letter.R()
    elif userchose == 'S':
        letter.S()
    elif userchose == 'T':
        letter.T()
    elif userchose == 'U':
        letter.U()

    elif userchose == 'V':
        letter.V()
    elif userchose == 'W':
        letter.W()
    elif userchose == 'X':
        letter.X()
    elif userchose == 'Y':
        letter.Y()
    elif userchose == 'Z':
        letter.Z()
    elif userchose == '0':
        digit.zero()
    elif userchose == '1':
        digit.one()
    elif userchose == '2':
        digit.two()
    elif userchose == '3':
        digit.three()

    elif userchose == '4':
        digit.four()
    elif userchose == '5':
        digit.five()
    elif userchose == '6':
        digit.six()
    elif userchose == '7':
        digit.seven()
    elif userchose == '8':
        digit.eight()
    elif userchose == '9':
        digit.nine()
    userchose = str(input("Would you like to ask another question? yes/no ")).lower()
    if userchose == 'no':
        print("Goodbye! Thanks for playing!")
        exit()
    elif userchose == 'yes':
        userchose = input(" Hellow World! please Enter Letter(A-Z) or Digit(0- 9):> ").upper()

    else:
        print('I apologies, I did not catch that. Please repeat.')







