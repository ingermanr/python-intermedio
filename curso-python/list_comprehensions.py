def main():
    
    # list_comp = []
    # for i in range(0,101):
    #     if i % 3 !=0:
    #         list_comp.append(i**2)
    
    # list_comp = [i**2 for i in range(1,101) if i %3 !=0]

    list_comp2 = [i for i in range(1,100000) if i % 36 ==0]

    print(list_comp2)

if __name__ == '__main__':
    main()