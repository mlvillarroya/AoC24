
def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read()
    file_structure = extract_file_structure(content)
    new_array = combine_arrays(file_structure)
    print(calculate_checksum(new_array))

def calculate_checksum(file_structure):
    checksum = 0
    for i in range(len(file_structure)):
        try:
            checksum += i*int(file_structure[i])
        except:
            pass
    return checksum

def combine_arrays(my_array):
    char_number = len([char for char in my_array if char!='.'])
    new_array = []
    reverse_array = my_array[::-1]
    j=0
    for i in range(char_number):
        if my_array[i] != '.':
            new_array.append(my_array[i])
        else:
            while reverse_array[j] == '.':
                j+=1
            new_array.append(reverse_array[j])
            j+=1
    return new_array


def extract_file_structure(content):
    file_structure = []
    file_index = -1
    for i in range(len(content)):
        if i % 2 == 0:
            file_index += 1
            symbol_to_add = file_index
        else:
            symbol_to_add = '.'
        for i in range(int(content[i])):
            file_structure.append(symbol_to_add)
    return file_structure

if __name__ == "__main__":
    main()