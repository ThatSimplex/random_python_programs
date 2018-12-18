

class Player:
    def __init__(self, name, rating, club):
        self._name = name
        self._club = club
        self._rating = rating
        self._status = 'on'
        self._score = 0
        self._results = {}
    
    def calculateScore(self):
        for result in self._results.keys():
            self._score += self._results[result]
        
        return self._score

    def getRating(self):
        return self._rating
    
    def getClub(self):
        return self._club