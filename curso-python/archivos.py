
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

# para escribir un archivo podemos usar 'w', para sobreescribir, o 'a' para adicionar al archivo
def write():
    names = ["Carlos", "Vanessa", "Jerónimo", 'Max', 'Lili', "House"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def main():
    write()
if __name__ == "__main__":
    main()