import locale

# Set the locale to Brazilian Portuguese
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def number_to_reais(number):
    # Format the number as currency
    #return locale.currency(number, grouping=True)

    nnumber = float('{}.{}'.format(int(number / 100), int(number % 100)))
    int_part, dec_part = format(nnumber, ',.2f').split('.')
    return f"R$ {int_part.replace(',', '.')},{dec_part}"


def number_to_words(number):
    # Convert the number to words in Portuguese
    # This functionality is not provided by the locale module
    # You would need to use a library like num2words with Portuguese support
    # Install it using `pip install num2words`
    #return num2words(number, lang='pt_BR')
    return formatar_numero(number)


def main():
    # Read the number from an input file
    with open('input.txt', 'r') as file:
        number = int(file.read().strip())

    # Format the number in reais and convert to words
    formatted_number = number_to_reais(number)
    words = number_to_words(number)

    # Write the formatted number and words to an output file
    with open('output.txt', 'w') as file:
        file.write(f"{formatted_number}\n{words}\n")


def desmembra_centena(numero) -> list:
    numeros = []
    next = numero

    while True:
        conjunto = next % 1000 # conjunto == 444
        next = int(next / 1000) # 1_012_999_123

        if conjunto == 0 and next == 0:
            break

        numeros.append(conjunto)

    return numeros


def parse_centena(valor) -> str:
    extenso = ""

    # unidades
    unidades = [ "", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove" ]

    # dezenas
    dezenas_lt_20 = [ "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove" ]
    dezenas_gt_20 = [ "",  "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa" ]

    # centenas
    centenas = [ "cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinheitos", "seissentos", "setessentos", "oitocentos", "novessentos" ]

    if valor == 100:
        #pos.append(0)
        extenso += centenas[0] + " "
    if 100 < valor < 200:
        #pos.append(1)
        extenso += centenas[1] + " e "
    if valor > 200:
        #pos.append(int(valor/100))
        extenso += centenas[int(valor/100)] + " e "
    if valor % 100 >= 20:
        #pos.append(int((valor % 100) / 10))
        extenso += dezenas_gt_20[int((valor % 100) / 10)] + " e "
    if 9 < valor % 100 < 20:
        #pos.append((valor % 10))
        extenso += dezenas_lt_20[valor % 10] + " "
    elif 0 < valor % 10 < 10:
        #pos.append(valor % 10)
        extenso += unidades[valor % 10] + " "

    return extenso


def parse_valor(valor) -> str:
    # milhares
    milhares = [ "", "mil", "milh", "bilh", "trilh" ]

    ld_valor = desmembra_centena(valor)

    extenso = ""
    count_zero = 0
    for i in range(len(ld_valor), 0, -1):
        if ld_valor[i - 1] == 0:
            count_zero += 1
            continue

        extenso += parse_centena(ld_valor[i - 1])
        extenso += "" if milhares[i - 1] == "" else "mil " if milhares[i - 1] == "mil" else milhares[i - 1] + "ão " if ld_valor[i - 1] == 1 else milhares[i - 1] + "ões "

    # ajuste
    if valor == 1:
        extenso += "real"
    else:
        if count_zero >= 2:
            extenso += "de reais"
        else:
            extenso += "reais"

    return extenso


def parse_centavos(centavos) -> str:
    # milhares
    milhares = [ "", "mil", "milh", "bilh", "trilh" ]

    ld_centavos = desmembra_centena(centavos)

    extenso = ""

    for i in range(len(ld_centavos), 0, -1):
        extenso += parse_centena(ld_centavos[i - 1])
        extenso += "" if milhares[i - 1] == "" else "mil" if milhares[i - 1] == "mil" else milhares[i - 1] + "ão" if \
        ld_centavos[i - 1] == 1 else milhares[i - 1] + "ões"
        if centavos == 1:
            extenso += "centavo" if milhares[i - 1] == "" else " e "
        else:
            extenso += "centavos" if milhares[i - 1] == "" else " e "

    return extenso


def formatar_numero(numero) -> str:
    extenso = ""
    valor = int(numero / 100)
    centavos = numero % 100

    if valor > 0:
        valor_extenso = parse_valor(valor)
        extenso += valor_extenso
    if centavos > 0:
        centavos_extenso = parse_centavos(centavos)
        if valor > 0:
            extenso += " e "
        extenso += centavos_extenso

    return extenso


def teste():
    print(formatar_numero(1_012_999_123_444))
    print(formatar_numero(100000001))
    print(formatar_numero(100))
    print(formatar_numero(101))
    print(formatar_numero(100001))
    print(formatar_numero(100000))
    print(formatar_numero(99900))
    print(formatar_numero(33300))
    print(formatar_numero(21))
    print(formatar_numero(20))
    print(formatar_numero(19))
    print(formatar_numero(11))
    print(formatar_numero(10))
    print(formatar_numero(1))


if __name__ == "__main__":
    #teste()
    main()

