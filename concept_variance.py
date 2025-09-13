from typing import TypeVar, Generic

class Person:
    pass

class Worker(Person):
    pass

P = TypeVar('P')
class ToString(Generic[P]):
    def to_str(self):
        print("invariant")

def test_to_str(x : ToString[Person]) -> None:
    return x.to_str()

test_to_str(ToString[object]())
test_to_str(ToString[Person]())
test_to_str(ToString[Worker]())

Q = TypeVar('Q', covariant=True)
class Producer(Generic[Q]):
    def produce(self) -> Q:  # type: ignore
        pass

def person_producer(x : Producer[Person]) -> Person:
    return x.produce()

person_producer(Producer[object]())
person_producer(Producer[Person]())
person_producer(Producer[Worker]())

R = TypeVar('R', contravariant=True)
class Consumer(Generic[R]):
    def consume(self, item: R) -> None:
        print(item)

def person_consumer(x : Consumer[Person], p : Person) -> None:
    x.consume(p)

person_consumer(Consumer[object](), Person())
person_consumer(Consumer[Person](), Person())
person_consumer(Consumer[Worker](), Person())
