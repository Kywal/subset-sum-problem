from utils.interface_manager import  menu, subset_sum_ascii_banner, print_menu
from exact_subset_sum.src.exact_subset_sum import all_subset_sums_card, all_subset_sums
import sys
sys.setrecursionlimit(30000)

print(subset_sum_ascii_banner())
print_menu()
item_menu = input()

menu(item_menu)
