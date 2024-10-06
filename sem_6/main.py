import word_count
import remove_duplicates
import unique_to_both_lists
import sys
import date_validator
import chess

print(word_count.count_wors_occurrences(['apple', 'banana', 'apple', 'orange']))

print(remove_duplicates.remove_consecutive_duplicates('aaabbcaaa'))

print(unique_to_both_lists.unique_to_both_lists([1, 2, 3], [3, 4, 5]))

if len(sys.argv) != 2:
    print("Usage: python data_validator.py DD.MM.YYYY")
    sys.exit(1)

date_input = sys.argv[1]

if date_validator.is_valid_date(date_input):
    print("True")
else:
    print("False")

if len(sys.argv) != 9:
    print("Usage: python main.py row1 col1 row2 col2 ... row8 col8")
    sys.exit(1)
positions = [(int(sys.argv[i]), int(sys.argv[i + 1])) for i in range(1, len(sys.argv), 2)]

if chess.are_queens_safe(positions):
    print("True")
else:
    print("False")