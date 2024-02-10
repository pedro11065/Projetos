"""
Quero descobrir quanto tempo vai demorar (em dias)
para eu terminar determinado curso de x horas vendo y horas por dia
"""

time_curse = int(input("Quantas horas de duração o curso tem? "))
time_per_day = int(input("Você vai estudar quantas horas por dia? "))
time_total = time_curse / time_per_day

print(f'Você vai estudar por aproximadamente {time_total} dias. Bons estudos!!!')
#1