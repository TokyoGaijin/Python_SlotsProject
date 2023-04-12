import random
import time

SLOT_SYMBOLS = ["🍒", "🍇", "🍊", "💖", "💰", "🍎", "🍉", "🔔", "🍋", "7"]
WINNING_VALUES = [10, 50, 100, 500]

class Slot():
    def __init__(self):
        self.slot_value = None

    def spin_slot(self):
        # animate symbols
        for i in range(30):
            print(SLOT_SYMBOLS[random.randrange(0, len(SLOT_SYMBOLS))], end = ' ')
            time.sleep(0.1)

        self.slot_value = SLOT_SYMBOLS[random.randrange(0, len(SLOT_SYMBOLS))]
        return self.slot_value


slot_1, slot_2, slot_3 = Slot(), Slot(), Slot()


def check_win(slot1Value, slot2Value, slot3Value):
    winnings = 0
    isWin = False

    if slot1Value == "🍒" and slot2Value != slot1Value:
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
    while True:
        pass



if __name__ == '__main__':
    run()