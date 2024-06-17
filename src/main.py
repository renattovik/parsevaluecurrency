import locale
from num2words import num2words

# Set the locale to Brazilian Portuguese
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def number_to_reais(number):
    # Format the number as currency
    return locale.currency(number, grouping=True)

def number_to_words(number):
    # Convert the number to words in Portuguese
    # This functionality is not provided by the locale module
    # You would need to use a library like num2words with Portuguese support
    # Install it using `pip install num2words`
    return num2words(number, lang='pt_BR')

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


if __name__ == "__main__":
    main()
