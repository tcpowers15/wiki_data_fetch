import wikipediaapi as wiki
import csv


def clean_text(text):
    # Todo:
    return 0


def get_random_sentences(num_data, lang_code):
    """
    Makes calls using wikipedia api and returns a list
    of sentences already cleaned and ready to be used in the intelligent
    systems project

    :param num_data: the number of sentences to produce
    :param lang_code: which language to get sentences in, accepts any
                        that is accepted by wikipedia
    :return: list of strings
    """
    # create Wikipedia api object



def main():
    # number of sentences to get
    num_data = 10

    # get the data
    english_sentences = get_random_sentences(num_data, 'en')
    dutch_sentences = get_random_sentences(num_data, 'nl')

    # write the lists to csv
    # todo


if __name__ == "__main__":
    main()
