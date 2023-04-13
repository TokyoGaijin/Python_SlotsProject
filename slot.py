import random
import time


SLOT_SYMBOLS = ["🍒", "🍇", "🍊", "💖", "💰", "🍎", "🍉", "🔔", "🍋", "7"]
bank = 200

class Slot():
    def __init__(self):
        self.slot_value = None

    def spin(self):
        # animate symbols
        for i in range(50):
            print(f"\r{SLOT_SYMBOLS[random.randrange(0, len(SLOT_SYMBOLS))]} {SLOT_SYMBOLS[random.randrange(0, len(SLOT_SYMBOLS))]} {SLOT_SYMBOLS[random.randrange(0, len(SLOT_SYMBOLS))]}", end='')
            time.sleep(0.015)

        self.slot_value = SLOT_SYMBOLS[random.randrange(0, len(SLOT_SYMBOLS))]
        return self.slot_value


slot_1, slot_2, slot_3 = Slot(), Slot(), Slot()


def check_win(slot1Value, slot2Value, slot3Value):
    winnings = 0
    isWin = False

    if slot1Value == "🍒" and slot2Value != "🍒" and slot3Value != "🍒":
        print("You Win with 1 Cherry!")
        isWin = True
        winnings = 20
    elif slot1Value == slot2Value and slot1Value == slot3Value:
        if slot1Value == "🍇":
            winnings = 100
            isWin = True
        elif slot1Value == "💖":
            winnings = 200
            isWin = True
        elif slot1Value == "🍋":
            winnings = 300
            isWin = True
        elif slot1Value == "🔔":
            winnings = 400
            isWin = True
        elif slot1Value == "7":
            winnings = 1000
            isWin = True
    else:
        print("Sorry, you lose!")
        winnings = -20
        isWin = False

    return isWin, winnings


def run():
    global bank
    while True:
        print(f"You currently have ${bank}!")
        choice = input("Press ENTER to spin or type 'q' to quit>")
        if choice.lower() == 'q':
            break
        else:
            print(f"\r{slot_1.spin()} {slot_2.spin()} {slot_3.spin()}", end=' ')
            bank += check_win(slot_1.slot_value, slot_2.slot_value, slot_3.slot_value)[1]
            if bank <= 0:
                print("Game over!")
                choice = input("[P]lay again? [Q]uit? >").lower()
                if choice == 'p':
                    bank = 200
                    continue
                else:
                    print("Thank you for playing.")
                    break
            else:
                print(f"You have ${bank}!")
                choice = input("[S]pin again? [Q]uit? >").lower()
                if choice == 's':
                    continue
                else:
                    print(f"You won a total of ${bank}! Good job!")
                    print("Thank you for playing.")
                    break



if __name__ == '__main__':
    run()