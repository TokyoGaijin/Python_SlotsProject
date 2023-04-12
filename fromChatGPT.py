import time
import random

# Define the symbols on the reels
symbols = ["🍒", "🍊", "🍋", "🍉", "🍇", "🍓", "🍍", "🔔", "💰"]

# Define the payouts for winning combinations
payouts = {"🍒🍒🍒": 50, "🍊🍊🍊": 40, "🍋🍋🍋": 30, "🍉🍉🍉": 20, "🍇🍇🍇": 10}

# Define the number of reels and symbols per reel
num_reels = 3
num_symbols = len(symbols)

# Spin the reels
reels = [random.randint(0, num_symbols-1) for i in range(num_reels)]

# Check for a cherry in the first reel
if symbols[reels[0]] == "🍒":
    payout = payouts[min(payouts, key=payouts.get)]
    print(f"\nCongratulations, you won {payout} points for a single cherry!")
    exit()

# Print the reels and wait for a moment
for i in range(10):
    # Print the current state of the reels
    print(f"\rSpinning... ", end='')
    for j in range(num_reels):
        print(f"{symbols[reels[j]]}", end=' ')
    time.sleep(0.1)
    
    # Spin the reels again
    reels = [random.randint(0, num_symbols-1) for i in range(num_reels)]
    
# Print the final state of the reels
print(f"\r", end='')
for j in range(num_reels):
    print(f"{symbols[reels[j]]}", end=' ')
    
# Check for winning combinations
winning_combination = "".join([symbols[reels[j]] for j in range(num_reels)])
if winning_combination in payouts:
    payout = payouts[winning_combination]
    print(f"\nCongratulations, you won {payout} points!")
else:
    print("\nSorry, no winning combination this time.")
