'''
Problem 2: Count the number of combinations of vowels from a sequence of morse code without spaces
'''

def main():
    n = int(input())
    morse_code = input().strip()

    morse_code_list = list(morse_code)

    print(count_vowel_sequences(morse_code_list, n))

def count_vowel_sequences(morse_code_list, size):

    n = size
    num_vowels_matrix = [[0, 0, 0] for _ in range(n)]

    for offset in range(n):
        # Check for a vowel of length 1
        check_1 = vowel_at_position_with_len_1(
            offset, morse_code_list
        )

        if check_1:
            if offset == 0:
                num_vowels_matrix[offset][0] = 1
            else:
                previous_vowel_num = sum(
                    num_vowels_matrix[offset - 1]
                )
                num_vowels_matrix[offset][0] = previous_vowel_num

        # Check for a vowel of length 2
        check_2 = vowel_at_position_with_len_2(
            offset, morse_code_list
        )

        if check_2:
            if offset == 1:
                num_vowels_matrix[offset][1] = 1
            else:
                previous_vowel_num = sum(
                    num_vowels_matrix[offset - 2]
                )
                num_vowels_matrix[offset][1] = previous_vowel_num

        # Check for a vowel of length 3
        check_3 = vowel_at_position_with_len_3(
            offset, morse_code_list
        )

        if check_3:
            if offset == 2:
                num_vowels_matrix[offset][2] = 1
            else:
                previous_vowel_num = sum(
                    num_vowels_matrix[offset - 3]
                )
                num_vowels_matrix[offset][2] = previous_vowel_num

    # Add the possible sequences ending at the final position.
    answer = sum(num_vowels_matrix[n - 1])

    return answer


#valid vowel only if it is a dot, returns true if so
def vowel_at_position_with_len_1(offset, morse_code_list):
    return morse_code_list[offset] == '.'

#valid if two dots or dot dash
def vowel_at_position_with_len_2(offset, morse_code_list):
    if offset < 1:
        return False

    code = morse_code_list[offset - 1] + morse_code_list[offset]

    return code == '..' or code == '.-'

#valid if dot dot dash or dot dot dot
def vowel_at_position_with_len_3(offset, morse_code_list):
    if offset < 2:
        return False

    code = (morse_code_list[offset - 2]
            + morse_code_list[offset - 1]
            + morse_code_list[offset])

    return code == '..-' or code == '---'



if __name__ == "__main__":
    main()