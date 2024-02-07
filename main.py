import turtle

WIDTH, HEIGTH = 500, 500

screen = turtle.Screen()
screen.setup(WIDTH, HEIGTH)
screen.title('Turtle_racing')

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Wprowadz ilosc Zółwi (2 - 10): ")

        if racers.isdigit():
            racers = int(racers)
        else:
            print("Wprowadzona wartosc nie jest liczba!  Wprowadz poprawna wartosc!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Liczba nie jest z przedziału od 2 do 10!  Spróbuj ponowanie!")

racers = get_number_of_racers()
print(racers)