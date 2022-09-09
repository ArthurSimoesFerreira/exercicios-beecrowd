n = int(input())
print(n)
d1 = n // 100
print("%i nota(s) de R$ 100,00"%d1)
d2 = (n % 100) 
d21 = d2 // 50
print("%i nota(s) de R$ 50,00"%d21)
d3 = d2 % 50
d31 = d3 // 20
print("%i nota(s) de R$ 20,00"%d31)
d4 = d3 % 20
d41 = d4 // 10 
print("%i nota(s) de R$ 10,00"%d41)
d5 = d4 % 10
d51 = d5 // 5
print("%i nota(s) de R$ 5,00"%d51)
d6 = d5 % 5
d61 = d6 // 2
print("%i nota(s) de R$ 2,00"%d61)
d7 = d6 % 2
d71 = d7 // 1
print("%i nota(s) de R$ 1,00"%d71)