import pickle

ascii = """     /$$                                                        
    | $$                                                        
    | $$        /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$ 
    | $$       /$$__  $$ |____  $$ /$$__  $$| $$__  $$ /$$__  $$
    | $$      | $$$$$$$$  /$$$$$$$| $$  \__/| $$  \ $$| $$  \ $$
    | $$      | $$_____/ /$$__  $$| $$      | $$  | $$| $$  | $$
    | $$$$$$$$|  $$$$$$$|  $$$$$$$| $$      | $$  | $$|  $$$$$$/
    |________/ \_______/ \_______/|__/      |__/  |__/ \______/ """

pc = """         ________________________________________________
        /                                                \\
       |    _________________________________________     |
       |   |root@root:~#                             |    |
       |   |    Choose your Desired Option:          |    |
       |   |        0. Run Setup                     |    |
       |   |        1. Import from txt               |    |
       |   |                                         |    |
       |   |    Use Presets: (Coming soon)           |    |
       |   |        2. Derivatives                   |    |
       |   |        3. trigonometric values          |    |
       |   |                                         |    |
       |   |                                         |    |
       |   |                                         |    |
       |   |                                         |    |
       |   |Learn your formulas from notifications ;)|    |
       |   |_________________________________________|    |
       |                                                  |
        \_________________________________________________/
               \___________________________________/"""
def DinoBino(Formulas):
    Time = int(input("How much notifiations you want to get per hour?: "))
    dic1 = {
        "Formulas": Formulas,
        "Time": Time
    }

    with open("config.bin","wb") as f:
        pickle.dump(dic1,f)
    
    print(f"Loaded {len(Formulas)} Formulas and you will get {Time} Notifiations per hour, Happy learning.")

def Setup():
    Number_of_Formulas = int(input("How much formulas you want to enter?: "))
    print("")

    Formulas = []
    for i in range(Number_of_Formulas):
        Formula = input(f"Enter formula {i+1}: ")
        Formulas.append(Formula)

    DinoBino(Formulas)

def ImportFromFile(filelocation):
    Formulas = []
    with open(filelocation,"r") as f:
        Formulas = f.readlines()
    
    test = []
    for i in Formulas:
        a = i.rstrip("\n")
        test.append(a)

    DinoBino(test)

if __name__ == '__main__':
    print(ascii)
    print(pc) #nice
    print("")

    while True:
        select = int(input("Select your option (0/3): "))
        
        if select == 0:
            Setup()
            break
        
        elif select == 1:
            print("Note: Keep 1 formula per line. please dont confuse my algorithm :P")
            print("")

            location = input("Enter File location (.txt): ")
            ImportFromFile(location)

            break

        elif select == 2:
            print("Coming soon..")
            break

        elif select == 3:
            print("Coming soon..")
            break

        else:
            print("Invalid Option :(")
