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

to_str_object = ToString[object]()
to_str_person = ToString[Person]()
to_str_worker = ToString[Worker]()

test_to_str(to_str_object)
test_to_str(to_str_person)
test_to_str(to_str_worker)

Q = TypeVar('Q', covariant=True)
class ToPrint(Generic[Q]):
    def to_print(self) -> None:
        print("covariant")

def test_to_print(x : ToPrint[Person]) -> None:
    x.to_print()

to_print_object = ToPrint[object]()
to_print_person = ToPrint[Person]()
to_print_worker = ToPrint[Worker]()

test_to_print(to_print_object)
test_to_print(to_print_person)
test_to_print(to_print_worker)

R = TypeVar('R', contravariant=True)
class ToAct(Generic[R]):
    def to_act(self) -> None:
        print("contravariant")

def test_to_act(x : ToAct[Person]) -> None:
    x.to_act()

to_act_object = ToAct[object]()
to_act_person = ToAct[Person]()
to_act_worker = ToAct[Worker]()

test_to_act(to_act_object)
test_to_act(to_act_person)
test_to_act(to_act_worker)