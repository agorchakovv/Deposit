per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
deposit = []
money = int (input("Введите количество денег для депозита: "))
for key in per_cent:
    per_cent[key] = money * per_cent[key] /100
    deposit.append(per_cent[key])
print (deposit)
print ("Максимальный депозит: ",max(deposit))