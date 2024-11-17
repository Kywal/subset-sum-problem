from instance_generator import instance_generator
from generator_ui import *
from inst_gen_io import write_instance, instance_to_str

s = int(input(welcome_text()))

range_input_message = "Por favor insira o intervalo ao quais os números do multiset devem pertencer(Intervalo fechado):\n"

rng = (int(input(range_input_message)),int(input()))

result = instance_generator(s,rng)
print_result(result)

# instance = instance_to_str(result[0], result[1][0], result[1][1])
# write_instance(instance)




