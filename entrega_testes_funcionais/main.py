# # import os
# # current_dir = os.path.dirname(os.path.abspath(__file__))
# # Aluguel =  os.path.join(current_dir, 'Aluguel.py')
from Aluguel import Aluguel

aluguel = Aluguel(400, 9)

valor_aluguel = aluguel.calcular_valor()

print("Valor calculado do aluguel: " + str(valor_aluguel))