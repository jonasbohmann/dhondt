# ======== D'hondt calculator ========

def main():

    quota = {}
    votes = {}
    wonSeats = {}
    allocatedSeats = 0

    print("==== D'HONDT CALCULATOR ====\n")

    while True:
        try:
            seats = int(input("How many seats are up for election?\n"))
            break
        except ValueError:
            print("The amount of seats has to be a positive integer!")


    while True:
        try:
            amountOfParties = int(input("How many parties participated in the election?\n"))
            break
        except ValueError:
            print("The amount of parties has to be a positive integer!")



    for x in range(amountOfParties):
        while True:
            try:
                party = str(input("Name of Party #" + str(x+1) + ": "))
                break
            except ValueError:
                print("The name of a party has cannot be empty!")


        while True:
            try:
                inputVotes = int(input("Amount of Votes for " + party + ": "))
                break
            except ValueError:
                print("The amount of votes of a party has to be a positive integer!")

        quota[party] = inputVotes
        votes[party] = inputVotes
        wonSeats[party] = 0



    print("\n==== CALCULATION ====")
    while allocatedSeats < seats:
        winner = max(quota.values())
        winnerKeys = [key for (key, value) in quota.items() if value == winner]

        # If there's a tie between the quotas of at least 2 parties, the seat goes to the first party
        winnerKey = winnerKeys[0]

        # Gives out warning if there's a tie between at least 2 quotas in the calculation
        if len(winnerKeys) > 1:
            print("WARNING! - There was a tie between " + str(winnerKeys) + ". The seat went to the party that you "
                  "entered first in the beginning.")

        # Result output
        print(str(winnerKey) + " wins seat #" + str(allocatedSeats + 1) + " with the highest quota of " + str(quota[winnerKey]))

        # Give seat to winner & calculate new quota
        wonSeats[winnerKey] = wonSeats[winnerKey] + 1
        quota[winnerKey] = votes[winnerKey] / (wonSeats[winnerKey] + 1)
        allocatedSeats += 1

    print("\n==== RESULTS ====")
    for key in wonSeats:
        print("Amount of seats for %s: %s" % (key, wonSeats[key]))


    # For windows users who use the python launcher
    x = input("\nPress 'ENTER' to exit... ")
    if len(x) >= 0:
        quit()

if __name__ == "__main__":
    main()
