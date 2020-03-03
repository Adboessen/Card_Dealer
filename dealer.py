from deck import Deck
import random

class Dealer(object):
    
    def __init__(self):
        self.work()
        
    def __str__(self):
        return(f'''{self.megaDeck}''')
    
    def combineDecks(self):
        self.megaDeck = []
        for i in range(4):
            self.megaDeck.append(Deck())
    
    def shuffle(self):
        n = len(self.megaDeck)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            self.megaDeck[i],self.megaDeck[j] = self.megaDeck[j],self.megaDeck[i]
            
    def deal(self):
        self.dealtCards = []
        self.dealtCards.append(self.megaDeck[0])
        return self.megaDeck[0]
        self.megaDeck.pop(0)
        
    def work(self):
        responce = input(f"Deal one card? Y or N: ")
        if responce == "Y":
            self.deal()  
          