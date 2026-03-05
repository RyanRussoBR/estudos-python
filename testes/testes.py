#While True executa o algoritmo que está contido para sempre!!!
# cont = 1
# while True:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou')

# n = s = 0
# while n != 999:
#     n = int(input('Digite um número: '))
#     s += n

# print(s-999)

# n = s = 0
# while True:
#     if n != 999:
#         n = int(input('Digite um número: '))
#         s += n
#     else:
#        s -= 999 
#        break
# print(s)

#Essa minha solução funciona, porém há uma forma melhor de fazer isso:

# n = s = 0
# while True:
#     n = int(input('Digite um número -> '))
#     if n == 999:
#         break
#     s += n
# print(s)
