
- #TODO GPT suggestion:
Organize into markdown file or **Jupyter notebook (also help with Interactive Learning)**
where you can categorize topics by language features, debugging tips, best practices, etc. This will make it easier to navigate and update your notes as they grow.

- ***Reorganize things by category**

- Cross-Referencing Sources: Adding references to other materials, such as textbooks, official documentation, or reliable online tutorials, can enrich your notes. 
- Reflection and Meta-Learning: Reflect on your learning process itself—what methods have helped you learn most effectively? Documenting the strategies that work for you can refine your approach to learning new technologies and programming languages in the future.
- Periodic Reviews: Set aside time periodically to review your notes. This can help you identify areas that need more understanding or additional examples. 

**See Juypter Notebook for more interactive examples and, also update it as I go**

# Language features / programming techniques ------------------------------:
Not comprehensive

#LEARNING CONCEPT if getting "dict_keys" at beginning of list, cus trying to get the keys, then call list() on the dictionary instead, this is when printing tho
#LEARNING - I keep accidentally doing == evaluator operator # instead of = assignment operator when I use T/F for loops and then I wonder why the loop doesn't work
#LEARNING CONCEPT: - strings are immutable so have to specifically assign shit to them
#LEARNING CONCEPT: - can use (string name).replace("thing to replace", "thing to replace with") to replace stuff in a string
#LEARNING CONCEPT GPT4 - python treats empty strings ("") as False and non-empty strings as True when evaluated in a Boolean context.
#LEARNING CONCEPT: GPT-4 Assigning data to obj.attr (obj.attr = userData) doesn't actually change the attribute named attr. To set an attribute on an object dynamically, use setattr(obj, attr_name, value) instead of obj.attr = value.
#LEARNING CONCEPT: dir() function to get a list of all the attributes (including methods) of an object.
#LEARNING CONCEPT: use the getattr(obj,attr) function to retrieve the value of each attribute.
#LEARNING CONCEPT: You'll want to filter out methods and focus on attributes, which you can do by using the callable() function or checking attribute types, 
#LEARNING CONCEPT: - range (timeAPeriod,timeBPeriod+1) why +1, because the range funciton is sort of like a list where it starts at 0, so to have it include the end digit you have to give it+1
#LEARNING CONCEPT: If not - The if not statement in Python checks for the opposite of the condition specified, is used to execute a block of code if a condition evaluates to False.
#LEANRING CONCEPT: Not operator is a logical operator that inverts the truth value of the condition that follows it
#LEARNING CONCEPT: In operator is used to check if a value exists within a sequence or collection, such as a list, tuple, string, dictionary, or set. 
#LEARNING CONCEPT: The error message you're seeing, TypeError: 'str' object is not callable, suggests that somewhere in your code, you're treating a string like a function—trying to "call" it with parentheses as if it were a method or function, but it's actually a string object. A common cause for this type of error is shadowing built-in functions with variables. For example, if at some point in your code before this input() call, you've assigned a string to a variable named input, you'd be shadowing the built-in input() function. Here's an example of how this might happen: To resolve this issue, check your code for any variable named input and rename it to something else that doesn't collide with Python's built-in functions. This kind of issue can occur with any built-in function (like str, list, dict, etc.), not just input, so it's a good practice to avoid using names of built-in functions for your variables.
#LEANRING CONCEPT: Formate datetime parser to be without leading zeros with "-","%-I:%M %p"
#LEARNING CONCEPT: dont do this('exit'.lower()), its redundant. use: if userData is None or userData.lower() == 'exit':
#LEARNING CONCEPT: Can access class variables outside of class by directly via the class name from outside the class. aka Classname.varAcessing then blah blah blah
#LEARNING CONCEPT, .cls is similar to .self
#LEANRING CONCEPT: Using TODO in VS Code. Mark with a '+' marks as complete. Can also use #FIXME and #NOTE, also see how to guid for exstension I installed.
#LEARNING CONCEPT - can put if & else statments all one line: weekday = 1 if weekday == 7 else weekday + 1. "(x if condition else y) The ternary operator is used for selecting between two values based on a condition, not for executing statements."
#LEARNING CONCEPT when you call list on dict, it returns list of keys. list(dayTimeSlots)
#LEARNING CONCEPT,, & KEY POINT - len gives me one more than index number, so keep in mind when using len to go thru indexs.  lengthDayTimeSlots = len(time_slot_keys)-1
#LEARNING CONCEPT - Basic dicitonary comprehension {key_expression: value_expression for item in iterable}
#LEARNING CONCEPT: strip(), Return a copy of the string with leading and trailing whitespace removed.
#LEARNING - If broken check to make sure dont have something twice, like an input or variable if it is broken via search / find like Issac did
#WHEN DEBUGGING remeber that everyhting is imported from csv so might need to use int()
#LEARNING CONCEPT: - HOW TO MAKE PYHTON WAIT BEFORE EXECUTING SOMETHING, import time, then time.sleep(x)
#LEARNING CONCEPT: - https://docs.python.org/3/howto/logging.html loggging
#LEARNING CONCEPT: - Dict & List Unpacking + Functions, literally *args and **kwargs are just the argument versions of **dict and *list unpackings.
#LEARNING CONCEPT: - .get() is a dict method? can provide default if no key to avoid KeyError. If default not given auto gives None.
#LEARNING CONCEPT: - iterating over kwargs iters over the keys not the values
#LEARNING CONCEPT: - Q: what about if I want to see if a word is inside a string? A: 
#LEARNING CONCEPT: - Use 'continue' to skip if statments and other conditionals say if dont want to execute on certain conditions, but do on others
#LEARNING CONCEPT: - GPT explains my mistake to me, in importance = row.get(row['Importance'], None), get() wont protect me bc row is fecting the dictionary so I need to use get() on the row. Thus will use: importance = row.get('Importance', None)
#LEARNING CONCEPT: - any() generator
#LEARNING CONCEPT: __init__.py marks a directory as a Python package, allowing its modules to be imported.
#LEARNING CONCEPT: Generators - (expression for item in iterable if condition)
#LEARNING CONCEPT: - DICTIONARY COMPREHENSIONs {key_expression: value_expression for item in iterable}
#LEARNING CONCPET: - LIST COMPREHENSIONs [expression/value for item in iterable]
#LEANRING CONCEPT: - **unpack dictionary into keyword arguments bc function expects them
#LEANRING CONCEPT: - Use a set if you are only interested in the presence or absence of items.
#LEANRING CONCEPT: - Can format fstrings directly aka ue formate specifiers. ex: f"Round this number to 2 digits {number: } Details: This is bc fString is evaled at runtime using the __format__(), thus uses the **formatting protocol** (same as format() method). See also s! and r! for user vs dev rep of string 
#LEANRING CONCEPT: - Can use f strings to easily store and dynamically change file paths. Ex: SWAT_NIGHT_CHORES_INFO_CSV = f"{PROJECT_ROOT}/{CSV_DATA_FOLDER}/SWATNightChoresInfo.csv"
#LEARNING CONCPET: - Interpolate: insert (something of a different nature) into something else
#LEARNING CONCPET: - raw or "r" string when you dont want \ mucking things up, can use with f strings, ex: rf"{xyz}\{abc}"
#LEARNING CONCPET: - Self-Documenting Expressions for Debugging: Can use fString to easily print var name and value for debug statments. Example: f"{variable = }" >>> variable = 'Some mysterious value'



#LEARNING CONCEPT: Git commit messages best practices:
Short (50 chars or less) summary of changes

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Further paragraphs come after blank lines.

- Bullet points are okay, too
- Typically a hyphen or asterisk is used for the bullet, preceded by a
  single space, with blank lines in between, but conventions vary here
- Use a hanging indent


#LEARNING CONCEPT & CODE snippet efficency
#easier way to return t/f values in a function

"""
Concise way:
return response in yesAnswers #if not then false is returned

Verbose way:
if response in yesAnswers:
    response = True
    return response
else: 
    response = False
    return response
    """

"""
ChatGPT
The use of enumerate in a for loop is a common Python idiom for iterating over a sequence when you need both the index and the value of each item in the sequence. 
The function enumerate takes an iterable (like a list, tuple, or string) as an input and returns an iterator that produces pairs of indexes and values from the iterable.

enumerate(timeListToSortAlgo): This call to enumerate takes the list timeListToSortAlgo as an argument. 
timeListToSortAlgo is assumed to be a list of strings, where each string represents a time (e.g., "12:30", "09:45").
enumerate Functionality: For each item in timeListToSortAlgo, enumerate generates a pair consisting of an index (starting from 0) and the value at that index in the list. 
So, if timeListToSortAlgo is ["12:30", "09:45", "23:59"], enumerate(timeListToSortAlgo) would produce (0, "12:30"), (1, "09:45"), and (2, "23:59") in successive iterations.
for index, timeStr in enumerate(timeListToSortAlgo): This unpacks each pair generated by enumerate into index and timeStr. In the first iteration, index would be 0 and timeStr would be "12:30", in the second iteration, index would be 1 and timeStr would be "09:45", and so on. 
This allows you to use both the index of each item (to access or modify items in the list by their position) and the value of each item (to work with the content directly) within the loop.
"""
#BIG LEARNING CONCEPT: (Or statements) if dateValue == 7 or 6: This condition does not check if dateValue is either 7 or 6. Instead, it checks if dateValue is 7, or if 6 is true. Since non-zero integers are considered truthy in Python, 6 is always true, making the condition always evaluate to true. if dateValue == 7 or dateValue == 6: is the proper way to implement a comparing "or" type argument
