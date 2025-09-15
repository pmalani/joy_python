from concept_duck import Duck, RubberDuck

if __name__ == '__main__':
    ducks: list[Duck | RubberDuck] = [Duck(), RubberDuck()]
    for duck in ducks:
        print(duck.say())