# 7. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = 1
y = 1
z = 1
i = not(x or y or z)
j = not x and not y and not z
k = i == j
print(k)

