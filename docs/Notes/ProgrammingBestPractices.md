
# Programming Notes / Best practices 

## Notes for running helpful dev packages / modules
- for formatting, black {source_file_or_directory}
- for static checking, mypy {program.py}
- Run code tracker in terminal
cd $HOME/.vscode/extensions/hangxingliu.vscode-coding-tracker-0.6.0; npm start -- -t CodeTracker


To get reports:
http://127.0.0.1:10345/report/?token=CodeTracker

## Naming Vars
- The length of a variable name should correspond to its scope. 
- Use prefixes like is, has, can, or should for boolean variables
- Names should be easily pronounceable and searchable through the codebase.
- Constants should be named using all uppercase letters with underscores separating words.
- Avoid magic numbers, Instead of hardcoding numbers directly in operations, define them as named constants at the top of your file or configuration
- (Personal) Functions or methods should have a verb in them (ideally start with one) to denote they do something & what they do

## UNIT TESTS
Unit tests evaluate the smallest parts of an application—typically individual functions or methods—to ensure they perform expected tasks correctly. Testing: Implement unit tests to cover various use cases and edge cases, ensuring the code behaves as expected.
Good unit tests are:
Isolated: Tests should not depend on external systems or the results of other tests.
Repeatable: Tests should provide the same results every time you run them.
Comprehensive: They should cover all cases, including typical use cases, edge cases, and potential error conditions.

## Keys() vs list()
Keys() vs list() so for non printing cases where I need the keys .keys() is slightly more efficenty. But if I need it to print out i need to use list() on the keys so i dont get that weird dict_keys thing at the beginning. But overall doesn't really matter. The .keys() in pyhton 3x is a veiw object which is slightly more memory efficent. But unless bottleneck then prioritize readability. But if need .keys a bunch, easier just to create a list.

## == vs is
You use == when comparing values and is when comparing identities.
is compares two objects in memory, == compares their values.

## IN
in is a memebership operator, but also part of the for loop syntax for iteration
or combines conditional statments, and returns True if at least one of the conditions evaluates to True, and false otherwise. Returns true on first operand that is Truthy and does not eval the rest. Use to see if something in a list for example is true. DONT CONFUSE WITH AND

## When fixing nested control statments and or figuring out if should make something a function
- Don't repeat myself
- Find common conditions - no need to check for extra (integrate into one logic)
- KISS
- The less nesting the better
- Can privatize functions
- Encapsulatoin
- Single responsibility
- Dont try to pre optimize to much, run a profiler and optimize based on the results from there

## When to use constants??

## When to use pass data as arguments vs make it a class attribute


## Documentation
Documentation: Provide detailed comments and documentation explaining the purpose of the code, how to use it, and describing the parameters and return values of functions.

## Modularization

When to modularize, diff between packages and modules etc.

### Organization
    - """Use clear, descriptive names for modules and functions to indicate what they do.
    Keep related functions within the same module to maintain coherence in your codebase.
    Avoid circular imports, where two modules import each other as this can lead to problems in execution. You can often resolve circular imports by reorganizing your functions into different modules or creating a new module for shared functions.
    Use a __init__.py file in each directory that should be treated as a package. This isn’t necessary in Python 3.3 and above, but it can still be useful for clarifying package structure.
    Limit the use of global variables between modules. Instead, pass data to functions as parameters."""

## Errrors
try else

# Code Notes and Style ---------


# Optimization ---------------

https://wiki.python.org/moin/TimeComplexity
Python time complexity operations

Builtin functions are faster than custom ones, as they are often implemented in C.
Data Structures: Choose appropriate data structures for your problem. For example, dictionaries offer constant-time lookups, while lists may require linear time for certain operations.
Avoid Unnecessary Work: Review your code and eliminate any unnecessary computations or redundant operations.
Cache Results: If your function repeatedly performs the same calculations with identical inputs, consider caching the results to avoid redundant computation.
Parallelization: If your task is highly parallelizable, you can leverage Python's multiprocessing or threading modules to distribute the workload across multiple CPU cores.
