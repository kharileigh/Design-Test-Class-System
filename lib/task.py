class Task():

    # PUBLIC PROPERTIES -- expose them
    #   title -- str - job to do
    #   complete - boolean 
    #       False when initiated
    #       True when mark complete method called
    def __init__(self, title):
        
        self.title = title
        self.complete = False


    def mark_complete(self): 
        
        self.complete = True