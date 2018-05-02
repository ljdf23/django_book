from django.test import TestCase

# Create your tests here.
lista = [ele for ele in (1,'f',3)]
print (lista)

lista2 = { k : k+1 for k in (1,2,3) }
print(lista2)

with open(r'C:\\Luis\\Python\\Django_Book\\django_book\\toys\\models.py') as myfile:
    for line in myfile:
        print(line)