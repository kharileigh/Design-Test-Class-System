import re

class PhoneNumberExtractor:


    def __init__(self, diary):
    
        #   set diary property
        self._diary = diary
        
        

    def extract(self): 
        # Returns:
        #   list of phone numbers -- saved as strings
        phone_numbers = []

        for entry in self._diary.all():

            contents = entry.contents

            phone_numbers += re.findall(r"0[0-9]{10}", contents)

            return phone_numbers

















        # # store extracted phone numbers in a list
        # phone_numbers = []

        # # for every entry in all diary entries
        # for entry in self._diary.all():

        #     # get contents from entry
        #     contents = entry.contents
        #     numbers = "0123456789"

        #     if numbers in contents and len(contents) == 10:
            
        #         phone_numbers += contents
        
        # return phone_numbers












        # # find entries with phone numbers
        # numbers = "0123456789"
        # if numbers in contents:
        #     if numbers.startswith("0") and len(numbers) == 10:
        #         phone_numbers.append(numbers)
        # return phone_numbers
            










        
        # # gets diary
        # # get all entries from diary using all method
        # entries = self.diary.all()

        # # separate entries to individual entry
        # # single_entry = [entry.split(',') for entry in entries]
        # single_entry = [entries.contents.split(',') for contents in entries]

        # # split string into words
        # word = single_entry.split()

        # # check if word in string contains phone numbers
        # #   starts with 0
        # #   length is 10(index starts at 0)
        # if word.startswith('0') and len(word) == 10:

        #     phone_number = word
            
        #     return phone_number