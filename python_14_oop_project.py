from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    
    def __init__(self):
        print("Creating New Ordred Deck!")
        self.card_list = [ (s,r) for s in SUITE for r in RANKS]

    def shuffling(self):
        shuffle(self.card_list)
    
    def splitting(self):
        return (self.card_list[:26],self.card_list[26:])

class Hand():
    def __init__(self,card_list):
        self.card = card_list

    def __str__(self):
        return "Contains {} cards".format(len(self.card))

    def add(self,add_list):
        self.card.extend(add_list)

    def remove(self):
        return self.card.pop()

class Player():
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    
    def paly_card(self):
        drawn_card = self.hand.remove()
        print("{} has palced: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.card) < 3:
            return self.hand.card
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player sill has cards left
        """
        return len(self.hand.card) != 0

#Main
print("Welcome to War")
d = Deck()
d.shuffling()
half1,half2 = d.splitting()
comp = Player("computer",Hand(half1))
name = input("What's your name?")
user = Player(name,Hand(half2))

total_round=0
war_count=0
while user.still_has_cards() and user.still_has_cards():
    total_round += 1
    print("Time for a new round")
    print("here are the current standing")
    print(user.name,"has the count: ",str(len(user.hand.card)))
    print(comp.name,"has the count: ",str(len(comp.hand.card)))
    print("Play card!")
    print("\n")

    table_cards = []
    c_card = comp.paly_card()
    p_card = user.paly_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("game over, number of rounds:"+str(total_round))
print("a war happended "+str(war_count)+" times")
print("Computer has:",comp.hand)
print("Human had:",user.hand)