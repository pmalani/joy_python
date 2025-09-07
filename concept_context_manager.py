try:
    f = open('concept_context_manager.py', 'r')
    print(f)
finally:
    f.close()

with open('concept_context_manager.py', 'r') as g:
    print(g)

class MyCustomContextManager:
    def __enter__(self):
        print("entering")
        return 42

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting")
        print(exc_type, exc_val, exc_tb)

with MyCustomContextManager() as h:
    print(h)
    raise ValueError("demo error")