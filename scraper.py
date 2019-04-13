import json
import requests
import csv


wiki_random_url_en = 'http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exintro&explaintext&exchars=500&format=json'
wiki_random_url_nl = 'http://nl.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exintro&explaintext&exchars=500&format=json'


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
    url = ''
    if lang_code == 'nl':
        url = wiki_random_url_nl
    else:
        url = wiki_random_url_en

    for i in range(num_data):
        request = requests.get(url)
        json_data = json.loads(request)
        text = json_data['query']\
            ['pages']\
            [list(json_data['query']['pages'].keys())[0]]\
            ['extract']

        text = clean_text(text)
        sentences.append(text)

    return sentences





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
