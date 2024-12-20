from utils.interface_manager import  menu, subset_sum_ascii_banner, print_menu
from exact_subset_sum_simple.src.exact_subset_sum_simple import all_subset_sums_simple
from exact_subset_sum_fft.src.exact_subset_sum_fft import all_subset_sums_fft

print(subset_sum_ascii_banner())
print_menu()
item_menu = input()

menu(item_menu)
