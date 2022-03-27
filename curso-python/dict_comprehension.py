def main():

    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i]=i**3

    print(my_dict)


    dict_natura = {i:i**3 for i in range(1,101) if i % 3 != 0}

    print(dict_natura)

    dict_reto = {i:round(i**0.5,2) for i in range(1,1001)}

    print(dict_reto)

    

if __name__ == '__main__':
    main()