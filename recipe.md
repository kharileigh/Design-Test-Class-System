## 1. Describe the Problem

*User Story*

***As a user***
***So that I can record my experiences***
***I want to keep a regular diary***

***As a user***
***So that I can reflect on my experiences***
***I want to read my past diary entries***

***As a user***
***So that I can reflect on my experiences in my busy day***
***I want to select diary entries to read based on how much time I have and my reading speed***

***As a user***
***So that I can keep track of my tasks***
***I want to keep a todo list along with my diary***

***As a user***
***So that I can keep track of my contacts***
***I want to see a list of all of the mobile phone numbers in all my diary entries***


Nouns : classes & attributes
Verbs : methods & functionality


## 2. Design the Class Interface

-  initializer
- public properties
- public methods with all parameters
- return values
- side-effects (anything that does other than the intended functionality // mutates something like adding to a list)


```python

class Parent:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   
        # Side effects:
        #  
        pass

    def (self):
        # Parameters:
        #   
        # Returns:
        #   
        # Side-effects
        #  
        pass 

    def (self):
        # Returns:
        #   
        # Side-effects:
        #   
        pass 

class Child:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   
        # Side effects:
        #  
        pass

    def (self):
        # Parameters:
        #   
        # Returns:
        #   
        # Side-effects
        #  
        pass 

    def (self):
        # Returns:
        #   
        # Side-effects:
        #   
        pass

```

## 3. Create Examples as Tests



``` python
# EXAMPLE

"""
Given no input
#raises exception
"""
instance = Class()
instance.function_call() -- error

"""
Given correct input
#returns desired result
"""
instance = Class()
instance.function_call(arg) -- assert vaue

```


## 4. Implement the Behaviour

Write Test -- (RED) Fail Test -- Implement Behaviour -- (GREEN) Pass Test 
Write New Test -- (RED) Fail Test -- Refactor to Implement Added Behaviour -- (GREEN) Pass Test 

*repeat until program is complete*  
