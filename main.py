import macguffin as algo
from numpy import random
import os
clear = lambda: os.system('cls')

encrypt_data = None
decrypt_data = None
base_key = None
key = None

def hello():
    print()
    print("Menu: ")
    print("    0 - Input key")
    print("    1 - Input data to encrypt")
    print("    2 - Input data to decrypt")
    print("    3 - Status")
    print("    4 - Encrypt")
    print("    5 - Decrypt")
    print("    6 - Example")
    print("    7 - About")
    print("    8 - Author")
    print("    9 - Exit")

def input_key():
    global base_key, key
    print("waiting for key...")
    tmp_key = int(input())
    print("Your key is : ", tmp_key)
    print("Accept - 1")
    if input() == "1":
        base_key = tmp_key
        key = algo.make_key(base_key)


def input_encrypt_data():
    global encrypt_data
    print("waiting for data...")
    tmp_data = int(input())
    print("Your data is : ", tmp_data)
    print("Accept - 1")
    if input() == "1":
        encrypt_data = tmp_data


def input_decrypt_data():
    global decrypt_data
    print("waiting for data...")
    tmp_data = int(input())
    print("Your data is : ", tmp_data)
    print("Accept - 1")
    if input() == "1":
        decrypt_data = tmp_data


def about():
    print("В криптографии, MacGuffin — симметричный блочный шифр, построенный на основе сети Фейстеля.")
    print("Алгоритм придуман Брюсом Шнайером и Мэттом Блэйзом в 1994 году в рамках Fast Software Encryption.")
    print("Ключевым элементом в структуре шифра является несбалансированная сеть Фейстеля. Входные блоки поделены на четыре регистра, ")
    print("по два байта каждый. В новом раунде три последних правых блока объединяются в контрольный блок и складываются по модулю 2 с ")
    print("раундовым ключом, созданным из основного при помощи алгоритма ключевого расписания. Полученные 48 бит разбиваются на 8 частей и ")
    print("становятся входными параметрами шести S-блоков. В свою очередь, каждый S-блок преобразует 6 входных битов в 2 выходных. 16-битный результат ")
    print("S-блоков складывается по модулю 2 с крайним слева входным блоком, и результат становится крайним справа регистром входного блока следующего раунда.")
    print("Три крайних справа регистра текущего раунда смещаются без изменений на одну позицию влево. Таким образом формируется входной блок для следующего раунда.")


def author():
    print("Программная реализация алгоритма MacGuffin")
    print("выполнил студент группы БИСТ-18-1")
    print("Портнов Роман Владимирович")
    print("ИТКН НИТУ МИСиС")
    print("МОСКВА 2020")

def status():
    global base_key, encrypt_data, decrypt_data
    print()
    print("Ключ шифрования: ", base_key)
    print("Данные для шифрования: ", encrypt_data)
    print("Данные для расшифровки: ", decrypt_data)

def encrypt():
    global base_key, encrypt_data, decrypt_data
    if base_key is None:
        print("Введите ключ")
        return
    if encrypt_data is None:
        print("Введите данные для шифрования")
        return
    decrypt_data = algo.encrypt(encrypt_data, key)
    print("Результат шифрования: ", decrypt_data)

def decrypt():
    global base_key, encrypt_data, decrypt_data
    if base_key is None:
        print("Введите ключ")
        return
    if decrypt_data is None:
        print("Введите данные для шифрования")
        return
    encrypt_data = algo.decrypt(decrypt_data, key)
    print("Результат расшифровки: ", encrypt_data)

def example():
    rnd1 = random.randint(0, (1<<31) - 1)
    rnd2 = random.randint(0, (1<<31) - 1)
    rnd3 = random.randint(0, (1 << 31) - 1)
    rnd4 = random.randint(0, (1 << 31) - 1)
    rnd5 = random.randint(0, (1 << 31) - 1)
    rnd6 = random.randint(0, (1 << 31) - 1)
    tmpkey = (rnd1<<96) + (rnd2<<64)+(rnd3<<32)+rnd4

    print("Ключ шифрования ", tmpkey)
    temp_key = algo.make_key(tmpkey)
    tmpdata = (rnd5<<32) + rnd6
    print("Данные до шифрования: ", tmpdata)
    tmp_data = algo.encrypt(tmpdata, temp_key)
    print("Данные после шифрования: ", tmp_data)
    tmpdata = algo.decrypt(tmp_data, temp_key)
    print("Расшифрование результата: ", tmpdata)


def main():
    END = True
    while END:
        hello()
        print("")
        command = input()

        if command == "0":
            input_key()
        if command == "1":
            input_encrypt_data()
        if command == "2":
            input_decrypt_data()
        if command == "3":
            status()
        if command == "4":
            encrypt()
        if command == "5":
            decrypt()
        if command == "6":
            example()
        if command == "7":
            about()
        if command == "8":
            author()
        if command == "9":
            END = False
        if command == "":
            continue


if __name__ == '__main__':
    main()

