# To bedzie plik na ktroym bede pracował z repo.
def hello(name):
	return "Hello" + str(name)

def dodaj(a,b):
	wynik = float(a)+float(b)
	return wynik
pierwsza = input()
druga = input()

def odejmij(a,b):
	return a-b

print("Hello world")
print(dodaj(pierwsza,druga))
