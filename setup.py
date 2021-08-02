from configparser import ConfigParser

ascii = """ /$$                                                        
| $$                                                        
| $$        /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$ 
| $$       /$$__  $$ |____  $$ /$$__  $$| $$__  $$ /$$__  $$
| $$      | $$$$$$$$  /$$$$$$$| $$  \__/| $$  \ $$| $$  \ $$
| $$      | $$_____/ /$$__  $$| $$      | $$  | $$| $$  | $$
| $$$$$$$$|  $$$$$$$|  $$$$$$$| $$      | $$  | $$|  $$$$$$/
|________/ \_______/ \_______/|__/      |__/  |__/ \______/ """

import pickle

if __name__ == '__main__':
    print(ascii)
    print("")
    print("Learn your formulas from notifications ;)")
    print("")

    Time_interval = int(input("How much notifiations you want to get per hour?: "))
    Number_of_Formulas = int(input("How much formulas you want to enter?: "))
    print("")

    Formulas = []

    for i in range(Number_of_Formulas):
        Formula = input(f"Enter formula {i+1}: ")
        Formulas.append(Formula)

    with open("E:\Python\codes\Learnig\config.bin","wb") as f:
        pickle.dump(Formulas, f)
        pickle.dump(Time_interval, f)
    
    with open("E:\Python\codes\Learnig\config.txt","w+") as f:
        f.write(str(Time_interval))

    print("")
    print(f"Thanks for using Learno, You will get {Time_interval} notifications per hour and a total of {Number_of_Formulas} formulas. Enjoy learning :)")
