from instance_generator_aux import instance_generator
from generator_ui import *

s = int(input(welcome_text()))

range_input_message = "Por favor insira o intervalo ao quais os números do multiset devem pertencer(Intervalo fechado):\n"

rng = (int(input(range_input_message)),int(input()))

result = instance_generator(s,rng)
print_result(result)
