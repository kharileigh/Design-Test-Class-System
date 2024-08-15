class DiaryEntry:
    
    # PUBLIC PROPERTIES 
    def __init__(self, title, contents):
    
        #   sets properties -- title, contents
        self.title = title
        self.contents = contents



"""
PUBLIC PROPERTIES CAN BE WRITTEN LIKE THIS ALSO :
from dataclasses import dataclass

@dataclass
class DiaryEntry():
    title : str
    contents : str
"""