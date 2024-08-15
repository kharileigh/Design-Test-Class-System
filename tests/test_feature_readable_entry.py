# # ------------------------ ReadableEntryExtractor ------------------------------
# """
# ADD 1 DIARY ENTRY THAT MATCHES GIVEN TIME
# Call ReadableEntryExtractor
# wpm = 2
# minutes = 2
# RETURNS DIARY ENTRY THAT WAS JUST ADDED
# """
# diary = Diary()

# entry_1 = DiaryEntry("Title", "one two three four")

# diary.add(entry_1)

# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) -> entry_1




# """
# ADD 1 DIARY ENTRY THAT DOES NOT MATCH GIVEN TIME
# Call ReadableEntryExtractor
# RETURNS NONE
# """
# diary = Diary()

# entry_1 = DiaryEntry("Title", "one two three four five")

# diary.add(entry_1)

# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) -> None



# """
# ADD MULTIPLE DIARY ENTRIES, ONE MATCHES
# Call ReadableEntryExtractor
# RETUNRS ONLY 1 THAT MATCHES
# """
# diary = Diary()

# entry_1 = DiaryEntry("Title", "one two three four five") #does not match
# entry_2 = DiaryEntry("Title", "one two three four") #matches

# diary.add(entry_1)
# diary.add(entry_2)

# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) -> entry_2


# """
# ADD MULTIPLE DIARY ENTRIES, MULTIPLE MATCHES
# Call ReadableEntryExtractor
# RETUNRS ONLY LONGEST READABLE & MATCHING TIME
# """
# diary = Diary()

# entry_1 = DiaryEntry("Title", "one two three four five") #does not match
# entry_2 = DiaryEntry("Title", "one two three four") #matches
# entry_3 = DiaryEntry("Title", "one two three") #does not match

# diary.add(entry_1)
# diary.add(entry_2)
# diary.add(entry_3)

# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) -> entry_2


# """
# ADD NO DIARY ENTRIES
# Call ReadableEntryExtractor
# RETUNRS NONE
# """
# diary = Diary()

# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) -> None
