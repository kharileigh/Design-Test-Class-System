# #--------------------------- TASK + TASKLIST -----------------------------
# # new task created -- added to TaskList(Parent) -- updates incomplete list 
# """
# Add multiple tasks
# NONE MARKED AS COMPLETE
# all_incomplete only lists the incomplete tasks
# """
# task_list = TaskList()

# task_1 = Task("Walk the dog")
# task_2 = Task("Walk the cat")
# task_3 = Task("Walk the frog")

# task_list.add(task_1)
# task_list.add(task_2)
# task_list.add(task_3)

# task_list.all_incomplete() -> [task_1, task_3]


# """
# Add multiple tasks
# MARK 1 AS COMPLETE
# all_complete only lists the complete tasks
# """
# task_list = TaskList()

# task_1 = Task("Walk the dog")
# task_2 = Task("Walk the cat")
# task_3 = Task("Walk the frog")

# task_list.add(task_1)
# task_list.add(task_2)
# task_list.add(task_3)

# task_2.mark_complete()

# task_list.all_complete() -> [task_2]

