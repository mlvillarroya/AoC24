TOTAL_ROUNDS = 25


def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content =  archivo.read().split()
    result = 0
    for element in content:
        result+=calculate_blinking_number(0, element)
    print(result)

def calculate_blinking_number(round_number, string_number):
    if round_number == TOTAL_ROUNDS:
        #print(string_number)
        return 1
    else:
        if int(string_number) == 0:
            return calculate_blinking_number(round_number + 1, '1')
        if len(string_number) % 2 == 0:
            half_len = int(len(string_number)/2)
            return calculate_blinking_number(round_number + 1, str(int(string_number[:half_len]))) + calculate_blinking_number(round_number + 1, str(int(string_number[half_len:])))
        else:
            return calculate_blinking_number(round_number + 1, str(int(string_number)*2024))


if __name__ == "__main__":
    main()