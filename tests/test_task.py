from lib.task import Task

#---------- Task
"""
Task constructed with title
"""
def test_task_constructs():

    task = Task("Walk the dog")
    
    assert task.title == "Walk the dog"


"""
Task newly constructed tasks are not complete
"""
def test_task_constructs_incomplete_tasks():
    
    task = Task("Walk the dog")

    assert task.complete == False


"""
Mark Test Complete -- reflected in complete property
"""
def test_marks_task_as_complete():

    task = Task("Walk the dog")

    task.mark_complete()

    assert task.complete == True