from lib.diary_entry import DiaryEntry


#---------- DiaryEntry
"""
DiaryEntry constructed with title & contents
Add diary entry
Set Title
Set Contents
"""
def test_diary_entry_contructs():
    entry = DiaryEntry("Title", "Contents")
    assert entry.title == "Title"
    assert entry.contents == "Contents"