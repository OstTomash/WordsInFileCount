import os


def get_number_of_words(phrases):
    """
    Function that receives a phrase from the user,
    writes it to a new file and counts the number of words in it

    :param phrases: string
    :return: number
    """
    file_path = os.path.join(os.getcwd(), 'files', 'example.txt')

    with open(file_path, 'w') as file:
        file.write(phrases)

    with open(file_path, 'r') as file:
        counter = len(file.read().strip().split(' '))
        return counter


custom_input = input("Enter whatever you want: ")
print(get_number_of_words(custom_input))
