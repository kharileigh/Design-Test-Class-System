from lib.diary import Diary
from lib.diary_entry import DiaryEntry


#--------------------------- DIARY + DIARY ENTRY ------------------------------
# new diary entry created -- added to Diary(Parent) -- updates list
"""
Add multiple diary entries
All lists - order they were added
"""
def test_adds_and_lists_entries():
    diary = Diary()

    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "Contents 2")
    entry_3 = DiaryEntry("Title 3", "Contents 3")

    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)

    assert diary.all() == [entry_1, entry_2, entry_3]