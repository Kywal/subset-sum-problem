# from utils.interface_manager import print_menu, subset_sum_ascii_banner, menu
from utils.interface_manager_exact import read_file, write_report, menu, subset_sum_ascii_banner,  print_menu
from exact_subset_sum.src.exact_subset_sum import all_subset_sums_card, all_subset_sums
import sys
sys.setrecursionlimit(30000)

print(subset_sum_ascii_banner())
print_menu()
item_menu = input()

menu(item_menu)
# from utils.interface_manager import read_file, write_report, print_menu, subset_sum_ascii_banner, menu


print(subset_sum_ascii_banner())
print_menu()
item_menu = input()

menu(item_menu)
