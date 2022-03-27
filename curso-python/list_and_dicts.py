def main():
    my_list = [1, "Hello", True, 4, 5]
    my_dict = {"first":1, 'lastname': 'Rodríguez'}

    super_list = [
        {"first":1, 'lastname': 'Rodríguez'},
        {"secund":2, 'lastname': 'Pérez'},
        {"third":3, 'lastname': 'Marín'},
        {"fourt":4, 'lastname': 'Galviz'},
        {"fivet":1, 'lastname': 'Ordúz'}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        'integer_nums': [4,3,5,2,1],
        'float_nums': [1.1,1.6,1.3]
    }

    for key, value in super_dict.items():
        print(key,'-', value)


    

if __name__ == '__main__':
    main()
    
    
