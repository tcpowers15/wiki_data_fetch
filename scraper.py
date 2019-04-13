import json
import requests
import csv


wiki_random_url = 'http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exintro&explaintext&exchars=500&format=json'


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
    sentences = []
    pages = []

    request = requests.get(wiki_random_url)
    json_data = json.loads(request.content)
    text = json_data['query']\
                    ['pages']\
                    [list(json_data['query']['pages'].keys())[0]]\
                    ['extract']




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
