import locale
import re

from num2words import num2words

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
    return ""

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


def teste():
    # unidades
    unidades = [ "", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove" ]

    # dezenas
    dezenas_lt_20 = [ "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove" ]
    dezenas_gt_20 = [ "",  "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa" ]

    # centenas
    centenas = [ "cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinheitos", "seissentos", "setessentos", "oitocentos", "novessentos" ]

    # milhares
    milhares = [ "", "mil", "milhão", "bilhão", "trilhão" ]

    numero = 1_012_999_123_444

    valor = int(numero / 100)
    centavos = numero % 100

    print(valor)
    print(centavos)

    #print(desmembra_centena(valor))
    #print(desmembra_centena(centavos))

    #for centena in desmembra_centena(valor):
    #    print(posicao_centena(centena))

    #for centena in desmembra_centena(centavos):
    #    print(posicao_centena(centena))

    grupo_valor = [posicao_centena(centena) for centena in reversed(desmembra_centena(valor))]
    grupo_centavo = [posicao_centena(centena) for centena in reversed(desmembra_centena(centavos))]

    print(grupo_valor)
    print(grupo_centavo)

    for grupo in grupo_valor:
        for i, g in enumerate(grupo):
            if i == 0:
                print(centenas[g])
            if i == 1 and len(grupo):
                if grupo[i+1] > 0:
                    print(dezenas_gt_20[g])
                else:
                    print(dezenas_lt_20[g])
            if i == 2:
                print(unidades[g])

    for grupo in grupo_centavo:
        for i, g in enumerate(grupo):
            if i == 0 and len(grupo) > 1:
                if grupo[i+1] > 0:
                    print(dezenas_gt_20[g])
                else:
                    print(dezenas_lt_20[g])

            if i == 1:
                print(unidades[g])


def desmembra_centena(numero):
    numeros = []
    next = numero

    while True:
        conjunto = next % 1000 # conjunto == 444
        next = int(next / 1000) # 1_012_999_123

        if conjunto == 0:
            break

        numeros.append(conjunto)

    #numeros = [num for num in reversed(numeros)]
    return numeros


def posicao_centena(valor):
    pos = []
    if valor == 100:
        pos.append(0)
    if 100 < valor < 200:
        pos.append(1)
    if valor > 200:
        pos.append(int(valor/100))
    if valor % 100 >= 20:
        pos.append(int((valor % 100) / 10))

    if 9 < valor % 100 < 20:
        pos.append((valor % 10))
    elif 0 < valor % 10 < 10:
        pos.append(valor % 10)

    return pos


if __name__ == "__main__":
    teste()
    #main()
