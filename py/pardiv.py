# Enter your code here. Read input from STDIN. Print output to STDOUT
def pardiv7(inicio, fim):
  cont = 0
  for n in range(inicio, fim + 1):
    if n % 2 == 0 and n % 7 == 0:
      cont += 1
  return cont

print pardiv7(input(), input())

