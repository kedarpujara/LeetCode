
dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
def main():
    print(phone_numbers("23"))

def phone_numbers(digits):
    combination = []

    def recurse(rest_of_word, path_so_far):

        if not rest_of_word:
            combination.append(path_so_far)
            return

        first, rest = rest_of_word[0], rest_of_word[1:]

        letters = dict[first]

        for letter in letters:
            recurse(rest, path_so_far + letter)
    recurse(digits, "")
    return combination

main()
