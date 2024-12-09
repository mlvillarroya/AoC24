from numpy.ma.mrecords import reserved_fields


def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read()
    file_structure = extract_file_structure(content)
    combine_arrays(file_structure)
    print(calculate_checksum(file_structure))

def calculate_checksum(file_structure):
    checksum = 0
    for i in range(len(file_structure)):
        try:
            checksum += i*int(file_structure[i])
        except:
            pass
    return checksum

def combine_arrays(my_array):
    reverse_array = my_array[::-1]
    i=0
    while i<len(reverse_array):
        if reverse_array[i] == '.':
            i += 1
        else:
            size = 1
            j=i
            while j<len(reverse_array)-1 and reverse_array[j] == reverse_array[j+1]:
                size += 1
                j += 1
                if j == len(reverse_array)-1:
                    break
            k=0
            while k<len(my_array):
                if my_array[k] != '.':
                    k += 1
                else:
                    l = k
                    size_gap = 0
                    while my_array[l] == '.':
                        size_gap += 1
                        l += 1
                        if l == len(my_array):
                            break
                    if size_gap >= size and k<len(my_array)-i:
                        for m in range(0, j-i+1):
                            my_array[k+m] = reverse_array[i+m]
                            my_array[len(my_array)-i-m-1] = '.'
                        break
                    k+=size_gap
            i=j+1



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