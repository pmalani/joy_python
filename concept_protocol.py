from typing_extensions import Protocol

from concept_duck import Duck, RubberDuck

class SayProtocol(Protocol):
    def say(self):
        pass

if __name__ == '__main__':
    ducks: list[SayProtocol] = [Duck(), RubberDuck()]
    for duck in ducks:
        print(duck.say())