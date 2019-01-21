# ======== D'hondt calculator ========
import time

def main():

    quota = {}
    votes = {}
    wonSeats = {}
    allocatedSeats = 0

    print("==== D'HONDT CALCULATOR ====")


    try:
        seats = int(input("How many seats are up for election?\n"))
    except ValueError:
        print("The amount of seats has to be a positive integer.\nThe program will now quit.")
        time.sleep(3)
        quit()

    try:
        amountOfParties = int(input("How many parties participated in the election?\n"))
    except ValueError:
        print("The amount of parties has to be a positive integer.\nThe program will now quit. ")
        time.sleep(3)
        quit()

    for x in range(amountOfParties):
        try:
            party = str(input("Name of Party: "))
        except ValueError:
            print("The name of a party has cannot be empty.\nThe program will now quit.")
            time.sleep(3)
            quit()

        try:
            inputVotes = int(input("Amount of Votes for " + party + ": "))
        except ValueError:
            print("The amount of votes of a party has to be a positive integer.\nThe program will now quit.")
            time.sleep(3)
            quit()

        quota[party] = inputVotes
        votes[party] = inputVotes
        wonSeats[party] = 0



    print("\n==== CALCULATION ====")
    while allocatedSeats < seats:
        winner = max(quota.values())
        winnerKeys = [key for (key, value) in quota.items() if value == winner]
        winnerKey = winnerKeys[0]
        print(str(winnerKey) + " wins seat #" + str(allocatedSeats + 1))
        wonSeats[winnerKey] = wonSeats[winnerKey] + 1
        quota[winnerKey] = votes[winnerKey] / (wonSeats[winnerKey] + 1)
        allocatedSeats += 1

    print("\n==== RESULTS ====")
    for key in wonSeats:
        print("Amount of seats for %s: %s" % (key, wonSeats[key]))

    print("\nThe program will quit after 10 seconds.")
    time.sleep(10)
    quit()

if __name__ == "__main__":
    main()
