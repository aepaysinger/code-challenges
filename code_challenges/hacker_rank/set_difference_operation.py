def learning_difference(roll_numbers_english, roll_numbers_french):
    english_set = set(roll_numbers_english)
    french_set = set(roll_numbers_french)
    english_only = english_set.difference(french_set)
    print(len(english_only))


if __name__ == '__main__':
    student_english_paper = int(input())
    roll_numbers_english = input().split(' ')
    student_french_paper = int(input())
    roll_numbers_french = input().split(' ')
    learning_difference(roll_numbers_english, roll_numbers_french)