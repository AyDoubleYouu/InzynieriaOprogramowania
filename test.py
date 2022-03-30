# To bedzie plik na którym bede pracował z repo.
def hello(name):
	return "Hello" + str(name)

def dodaj(a,b):
	wynik = float(a)+float(b)
	return wynik

def odejmij(a,b):
	wynik = float(a)-float(b)
	return wynik

pierwsza = input()
druga = input()

print(dodaj(pierwsza,druga))
