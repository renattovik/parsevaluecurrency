import locale

# Set the locale to Brazilian Portuguese
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def desmembra_centena(numero) -> list:
    numeros = []
    next = numero

    while next > 0:
        numeros.append(next % 1000)
        next //= 1000

    return list(reversed(numeros))


def parse_centena(valor) -> str:
    if valor == 0:
        return ""

    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas_lt_20 = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
                     "dezenove"]
    dezenas_gt_20 = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
                "oitocentos", "novecentos"]

    extenso = []

    if valor == 100:
        return centenas[0]

    if valor > 100:
        extenso.append(centenas[valor // 100])
        if valor % 100 > 0:
            extenso.append("e")

    dezena = valor % 100
    unidade = valor % 10

    if 10 <= dezena < 20:
        extenso.append(dezenas_lt_20[dezena - 10])
    else:
        if dezena >= 20:
            extenso.append(dezenas_gt_20[dezena // 10])
            if unidade > 0:
                extenso.append("e")
        if unidade > 0:
            extenso.append(unidades[unidade])

    return " ".join(extenso).strip()


def parse(valor) -> (int, str):
    milhares = ["", "mil", "milhão", "bilhão", "trilhão"]
    extenso = []
    count_zero = 0
    partes = desmembra_centena(valor)

    for i, parte in enumerate(partes):
        if parte == 0:
            count_zero += 1
            continue

        extenso.append(parse_centena(parte))
        if milhares[len(partes) - 1 - i]:
            if parte == 1 and (len(partes) - 1 - i) > 1:
                extenso.append(milhares[len(partes) - 1 - i])
            else:
                if milhares[len(partes) - 1 - i] != "mil":
                    extenso.append(milhares[len(partes) - 1 - i][:-2] + ("ões" if parte > 1 else ""))
                else:
                    extenso.append(milhares[len(partes) - 1 - i])

        if partes[(len(partes) - i) - 1] > 100 and len(partes) > 1 and i + 1 < len(partes):
            extenso[len(extenso) - 1] += ","

    return count_zero, " ".join(extenso).strip()


def parse_valor(valor) -> str:
    extenso = []
    count_zero, txt = parse(valor)
    extenso.append(txt)

    if valor == 1:
        extenso.append("real")
    else:
        if count_zero >= 2:
            extenso.append("de")

        extenso.append("reais")

    return " ".join(extenso).strip()


def parse_centavos(centavos) -> str:
    extenso = []

    _, txt = parse(centavos)
    extenso.append(txt)

    # ajustes
    if centavos == 1:
        extenso.append("centavo")
    else:
        extenso.append("centavos")

    return " ".join(extenso).strip()


def escreve_numero_extenso(numero) -> str:
    valor = numero // 100
    centavos = numero % 100

    extenso = []
    if valor > 0:
        extenso.append(parse_valor(valor))
    if centavos > 0:
        if valor > 0:
            extenso.append("e")
        extenso.append(parse_centavos(centavos))

    return " ".join(extenso).strip()


def number_to_reais(number) -> str:
    # Format the number as currency in Brazilian format
    nnumber = float('{}.{}'.format(int(number / 100), int(number % 100)))
    int_part, dec_part = format(nnumber, ',.2f').split('.')
    return f"R$ {int_part.replace(',', '.')},{dec_part}"


def number_to_words(number) -> str:
    return escreve_numero_extenso(number)


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
    numeros_para_testar = [
        999_666_234_567_890_01,
        999_666_234_567_830_01,
        1_012_999_123_444,
        100000002,
        100000001,
        100,
        101,
        100001,
        100000,
        99900,
        33300,
        10000,
        23,
        21,
        20,
        19,
        11,
        10,
        1
    ]

    for numero in numeros_para_testar:
        print(escreve_numero_extenso(numero))


if __name__ == "__main__":
    teste()
    # main()
