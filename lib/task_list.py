class TaskList:

    def __init__(self):

        #  creates empty list to hold tasks in TaskList
        self._tasks = []
    

    def add(self, task):
        
        #  adds current task to TaskList
        self._tasks.append(task)


    def all_incomplete(self):
        
        #   returns list of incompleted tasks
        #   added complete attribute to Task Class
        #       complete = False
        return [
            task for task in self._tasks
            if not task.complete
        ]
    


    def all_complete(self):
       
        #   added complete attribute to Task Class
        #       complete = True
        return [
            task for task in self._tasks
            if task.complete
        ]