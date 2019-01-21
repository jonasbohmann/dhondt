# ======== D'hondt calculator ========
def main():
    quota = {}
    wonSeats = {}
    votes = {}
    allocatedSeats = 0

    print("==== D'HONDT CALCULATOR ====")
    seats = int(input("How many seats are up for election?\n"))
    amountOfParties = int(input("How many parties participated in the election?\n"))

    for x in range(amountOfParties):
        party = str(input("Name of Party: "))
        inputVotes = int(input("Amount of Votes for " + party + ": "))
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


if __name__ == "__main__":
    main()
