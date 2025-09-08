# Joy of Programming Language Concepts in Python

## Equality
- [concept_eq.py](concept_eq.py)
- using `is` to check if same instance
- using `__eq__`
- using `@dataclass`

## Memoization
- Before
    - [concept_mem.py](concept_mem.py)
- After
    - [concept_mem_fix.py](concept_mem_fix.py)

## Duck Typing
- [concept_duck.py](concept_duck.py)

## Lambda
- [concept_lambda.py](concept_lambda.py)
- a.k.a. closure
- currying example with `double`
- lambdas as parameters with `do_something_useful`
- lambdas as return with `acc`
- currying with function using `partial`

## Decorator
- [concept_decorator.py](concept_decorator.py)
- a.k.a. annotation
- implement a function that returns a function wrapping the original function, e.g. `logged`
- use the `@wraps` decorator
  - to copy function metadata (name, help, etc.) from the original function to the newly wrapped function
- to create a decorator that accepts parameters
  - wrap in another function that returns the original decorator, e.g. `logged1`
- class decorator is a function that takes a class and manipulates its contents, e.g. `log_methods`
- removing code duplication between `logged` and `logged1` is left as homework?

## Metaclass
- [concept_metaclass.py](concept_metaclass.py)
- Create a new type by sub-classing `type`
- Allows customization of type in `__new__`
- Normal classes can now use the new type using `metaclass`

## Generators
- [concept_generator.py](concept_generator.py)
- `gen1` is not a tuple
- `sum(gen1)` is more efficient as intermediate list is not created
- Be careful as generators are use-once and exhausted, i.e, `sum3`
- Generator works by transferring the control flow using `yield`
- In general, generator allows for iteration (using `__iter__`)
    - e.g., using `for` syntax

## Comprehension
- [concept_comprehension.py](concept_comprehension.py)
- kinda like: select...from...where
- with list, set, dictionary
- filter with `if`
- for tuple with `tuple`
- what about group by (and others?)
  - use itertools
    - sort first using `sorted`
    - grouping `key` is not need in this particular example

## Destructuring
- [concept_destructuring.py](concept_destructuring.py)
- with tuples
- with lists
- with return types
- with dictionary
- with object with `__iter__`
- with object with pattern matching

## Pattern Matching
- [concept_pattern.py](concept_pattern.py)
- with enum
- using or
- conditional with `if`
- with list
- with tuple
- with dictionary

## Copy
- [concept_copy.py](concept_copy.py)
- `deepcopy` to make a deep copy
- `copy` to make a shallow copy
- Should make a copy in `from_postions`?

## Operator over-loading
- [concept_operators.py](concept_operators.py)
- see example of `+` with `__add__`
- minus is left as homework?

## Spread Operator
- [concept_spread.py](concept_spread.py)
- Also known as, spat or unpack
- with tuple
- with list
- with set
- with dictionary
- with method

## Pipe Operator
- [concept_pipe.py](concept_pipe.py)
- Very similar to spread operator
- Only on set and dictionary
- Not on tuple and list

## Variable Arguments
- [concept_variable_arguments.py](concept_variable_arguments.py)
- Now, if we already have a list (or some other type)
  - we have to unpack using spread operator
- pass in as `tuple`
- `*args` can only be the last argument
- `*args` is positional argument
- where as `**kwargs` is keyword argument
  - pass in as `dict`
- Possible to combine `*args` as well as `**kwargs`

## Context Manager
- [concept_context_manager.py](concept_context_manager.py)
- can also build a custom one
- a.k.a. try with resources / auto closeable

## Multiple Inheritance
- [concept_mi.py](concept_mi.py)
- How many name(s) does `Broker` have?
  - check the `mro` (method resolution order)
- Is non-virtual multiple inheritance possible in python?
- Who wins when there are conflicts? `HouseBoat` versus `BoatHouse`

## Object-Oriented Programming (OOP)
- [concept_dop_vs_oop_setup.py](concept_dop_vs_oop_setup.py)
  - Using `abc` and `abstractmethod`!
- Where does change come from?
- At least two main axes:
  - New shape(s)
  - New behavior(s)
- New shape is where OOP really shines
  - [concept_dop_vs_oop_add_shape.py](concept_dop_vs_oop_add_shape.py)
- New behavior requires lots of changes
  - [concept_dop_vs_oop_behavior.py](concept_dop_vs_oop_behavior.py)
- Non OOP answer (with Data-Oriented Programming (DOP))
  - [concept_dop_vs_oop_calculator.py](concept_dop_vs_oop_calculator.py)
  - using `if`, `elif`, and `else`
  - using pattern matching
  - using `singledispatch`
    - now we have a full circle
    - overloading in python

## Tail Recursion
- [concept_tail_recursion.py](concept_tail_recursion.py)
- If the last (`tail`) call is a recursive call (see `fac2` versus `fac1`)
  - then, it can be optimized away with a loop
- Not yet automatically implemented in python

## Monad
- [concept_monad.py](concept_monad.py)
- A monad is an object that wraps a value
  - providing additional functionality
- How to deal with divide by zero?
  - Not deal with it; propagate the exception (e.g. `div1`)
  - Return some default value (e.g. `div2`)
    - 0, 1, None?
  - Return a `Maybe` monad to force the caller to deal (e.g. `div3`)
  - `Optional` is just a type (typing?) hint (e.g. `div4`)
- There are many other types of monads
  - e.g. `Future` in asynchronous programming 
