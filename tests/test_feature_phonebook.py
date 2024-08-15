from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.phone_number_extractor import PhoneNumberExtractor



# ------------------------ PhoneNumberExtractor -----------------------------
"""
Add multiple diary entries
CALL EXTRACT FUNCTION -- PhoneNumberExtractor
Returns lists of phone numbers from all diary entries
"""
def test_extract_phone_numbers():

    # initialise Parent(Diary)
    diary = Diary()

    # initialise & add entry to Child(DiaryEntry)
    entry_1 = DiaryEntry("Title 1", "My friend is 07800000001 and 07800000002")
    entry_2 = DiaryEntry("Title 2", "Contents 2")
    # entry_3 = DiaryEntry("Title 3", "My friend is 07800000003")

    # update Parent(Diary)
    diary.add(entry_1)
    diary.add(entry_2)
    # diary.add(entry_3)

    # initialise & add diary to Child(PhoneNumberExtractor)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == ["07800000001", "07800000002"]

    # not registering third entry...
    #   assert extractor.extract() == ["07800000001", "07800000002", "07800000003"]



# """
# Add diary entry
# CALL EXTRACT FUNCTION -- PhoneNumberExtractor
# IGNORES DUPLICATES PHONE NUMBER 
# """
# diary = Diary()

# # all numbers the same, saved once
# entry_1 = DiaryEntry("Title 1", "My friend is 07800000001 and 07800000001")
# entry_2 = DiaryEntry("Title 2", "My friend is 07800000002")

# diary.add(entry_1)
# diary.add(entry_2)

# extractor = PhoneNumberExtractor(diary)
# extractor.extract() -> ["07800000000"]



# """
# Add diary entry
# CALL EXTRACT FUNCTION -- PhoneNumberExtractor
# IGNORES NON-VALID PHONE NUMBER -- less/more than 11 digits
# """
# diary = Diary()

# entry_1 = DiaryEntry("Title 1", "My friend is 07800000000 and 0790000000 and 0780 13141")

# diary.add(entry_1)

# extractor = PhoneNumberExtractor(diary)

# extractor.extract() -> []



# """
# NO DIARY ENTRY ADDED
# CALL EXTRACT FUNCTION -- PhoneNumberExtractor
# RETURNS AN EMPTY LIST
# """
# diary = Diary()

# extractor = PhoneNumberExtractor(diary)

# extractor.extract() -> []


