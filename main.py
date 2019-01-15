# ======== D'hondt calculator ========
class dhondt():

    def getSeats(self):
        seats = int(input("How many seats are up for re-election?\n"))

    def getVotes(self):
        print("Enter the amount of votes each party received.")

        votesCDU = int(input("CDU: "))
        votesSPD = int(input("SPD: "))
        votesGruene = int(input("Die Grünen: "))
        votesFDP = int(input("FDP: "))
        votesLinke = int(input("Die Linken: "))

        # Total seats
        print(votesCDU + votesSPD + votesGruene + votesSPD + votesLinke)

    def getQuota(self):
        pass


def main():
    election = dhondt()
    election.getSeats()
    election.getVotes()
    election.getQuota()
    print("Alles gut!")

if __name__ == "__main__":
    main()
