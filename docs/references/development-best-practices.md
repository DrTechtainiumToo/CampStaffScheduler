
# Programming Notes / Best practices 


## Naming Vars
- For more details and general info on naming see: [Python Naming Conventions](/docs/references/python-naming-conventions.md)
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

## When fixing nested control statments and or figuring out if should make something a function
- Don't repeat myself
- Find common conditions - no need to check for extra (integrate into one logic)
- KISS
- The less nesting the better
- Can privatize functions
- Encapsulatoin
- Single responsibility
- Dont try to pre optimize to much, run a profiler and optimize based on the results from there

## Building out new features
#Good approach on how to build out new features
Detail Out Each Function: Outline what each function should do, its inputs, outputs, and how it fits into the larger task assignment process.
Start Implementing in Stages: Begin with the foundational elements like data handling and move up to more complex logic like the probabilistic assignments.
Iterate Based on Feedback: Test each component as you build it and refine your approach based on the results.


## When to use pass data as arguments vs make it a class attribute

## Organization
    - """Use clear, descriptive names for modules and functions to indicate what they do.
    Keep related functions within the same module to maintain coherence in your codebase.
    Avoid circular imports, where two modules import each other as this can lead to problems in execution. You can often resolve circular imports by reorganizing your functions into different modules or creating a new module for shared functions.
    Use a __init__.py file in each directory that should be treated as a package. This isn’t necessary in Python 3.3 and above, but it can still be useful for clarifying package structure.
    Limit the use of global variables between modules. Instead, pass data to functions as parameters."""

### File Naming
Kebab-case (-) is more common for documentation and web-based URLs.
Snake_case (_) is better for Python and scripts.

## Documentation
Documentation: Provide detailed comments and documentation explaining the purpose of the code, how to use it, and describing the parameters and return values of functions.

# Optimization ---------------

https://wiki.python.org/moin/TimeComplexity
Python time complexity operations

Builtin functions are faster than custom ones, as they are often implemented in C.
Data Structures: Choose appropriate data structures for your problem. For example, dictionaries offer constant-time lookups, while lists may require linear time for certain operations.
Avoid Unnecessary Work: Review your code and eliminate any unnecessary computations or redundant operations.
Cache Results: If your function repeatedly performs the same calculations with identical inputs, consider caching the results to avoid redundant computation.
Parallelization: If your task is highly parallelizable, you can leverage Python's multiprocessing or threading modules to distribute the workload across multiple CPU cores.
