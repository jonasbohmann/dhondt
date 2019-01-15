# ======== D'hondt calculator ========
def main():

    print("==== D'HONDT CALCULATOR ====")

    seats = int(input("How many seats are up for election?\n"))

    print("Enter the amount of votes each party received.")

    votesCDU = int(input("CDU: "))
    votesSPD = int(input("SPD: "))
    votesFDP = int(input("FDP: "))

    votes = {"CDU": votesCDU, "SPD": votesSPD, "FDP": votesFDP}

    round = 0
    allocatedSeats = 0
    seatsCDU = 0
    seatsSPD = 0
    seatsFDP = 0
    qCDU = 0
    qSPD = 0
    qFDP = 0

    print("\n==== CALCULATION ====")

    while allocatedSeats < seats:
        winner = max(votes.values())
        winnerKey = [key for (key, value) in votes.items() if value == winner]
        print(str(winnerKey) + " wins round " + str(round))

        if winnerKey == ['CDU']:
            seatsCDU += 1
            qCDU = votesCDU / (seatsCDU + 1)
            votes["CDU"] = qCDU

        if winnerKey == ['SPD']:
            seatsSPD += 1
            qSPD = votesSPD / (seatsSPD + 1)
            votes["SPD"] = qSPD

        if winnerKey == ['FDP']:
            seatsFDP += 1
            qFDP = votesFDP / (seatsFDP + 1)
            votes["FDP"] = qFDP

        # Tie "Breaker", aber nicht wirklich
        # Ich wusste nicht wie ich den Sitz losen konnte
        if qCDU == qSPD or qCDU == qFDP or qSPD == qFDP:
            print("ERROR!  -  There appears to be a tie between at least 2 parties in the calculation of the quota. As "
                  "such, the seat of this round will not be allocted.")

        allocatedSeats += 1
        round += 1

    print("\n==== RESULTS ====")
    print("Amount of seats for the CDU: " + str(seatsCDU))
    print("Amount of seats for the SPD: " + str(seatsSPD))
    print("Amount of seats for the FDP: " + str(seatsFDP))


if __name__ == "__main__":
    main()
