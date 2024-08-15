class Diary:
    
    
    def __init__(self):

        #  creates empty list to hold diary entries in Diary
        self._entries = []


    
    def add(self, diary_entry):

        #  adds current diary entry to list in Diary
        self._entries.append(diary_entry)



    def all(self):
        
        #  list of diary entries in Diary
        return self._entries