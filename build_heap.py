# python3
# Mareks Siņica-Siņavskis 221RDB430

def build_heap(data,n):
    swaps = []
    def Veidot_koku(i):
        keisais_berns = 2 * i + 1
        labais_berns = 2 * i + 2
        mazakais = i

        if keisais_berns < n and data[keisais_berns] < data[mazakais]:
            mazakais = keisais_berns
        if labais_berns < n and data[labais_berns] < data[mazakais]:
            mazakais = labais_berns
        if mazakais != i:
            data[i], data[mazakais] = data[mazakais], data[i]
            swaps.append((i, mazakais))
            Veidot_koku(mazakais)

    for i in range(n // 2 - 1, -1, -1):
        Veidot_koku(i)

    return swaps


def main():
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_type = input()
    if input_type[:1] == 'F':
        file_name = input()
        try:
            with open("test/"+file_name+"") as text_file:
                n = int(text_file.readline())
                data = text_file.readline()
                data = list(map(int, data.split()))
        except IOError:
            print('Invalid file name')
            return
    elif input_type[:1] == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    else:
        print('Invalid input!')
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data,n)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
