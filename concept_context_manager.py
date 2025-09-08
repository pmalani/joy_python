from contextlib import contextmanager

try:
    f = open('concept_context_manager.py', 'r')
    print(f)
finally:
    f.close()

with open('concept_context_manager.py', 'r') as g:
    print(g)

class MyCustomContextManager1:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print(f"entering {self.value}")
        return 42

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"exiting {self.value}")
        print(exc_type, exc_val, exc_tb)

with MyCustomContextManager1(1) as h1:
    print(h1)
    # raise ValueError("demo error")

@contextmanager
def my_custom_context_manager_2(value):
    print(f"entering {value}")
    try:
        yield
    finally:
        print(f"exiting {value}")

with my_custom_context_manager_2(2) as h2:
    print(h2)

# @MyCustomContextManager1()
# def h3():
#     print("h3")
#
# h3()

@my_custom_context_manager_2(3)
def h4():
    print("h4")

h4()