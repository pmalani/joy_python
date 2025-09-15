class Duck(object):
    def say(self):
        return "quack"

class RubberDuck(object):
    def say(self):
        return "squeak"

if __name__ == '__main__':
    ducks = [Duck(), RubberDuck()]
    for duck in ducks:
        print(duck.say())