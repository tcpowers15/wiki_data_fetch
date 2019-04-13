import json
import requests


wiki_random_url_en = 'http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exintro&explaintext&exchars=500&format=json'
wiki_random_url_nl = 'http://nl.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exintro&explaintext&exchars=500&format=json'


def clean_text(text):
    """
    sanitizes the input text to fall within the confines of the text to be used in the project
    this function became pretty uneeded but its still here

    :param text: string of text
    :return: data
    """
    text = ' '.join(text.split()[:15])
    return text


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
    if lang_code == 'nl':
        url = wiki_random_url_nl
    else:
        url = wiki_random_url_en

    for i in range(num_data):
        request = requests.get(url)
        json_data = json.loads(request.content)
        text = json_data['query']['pages'][list(json_data['query']['pages'].keys())[0]]['extract']
        text = clean_text(text)
        sentences.append(text)

    return sentences


def main():
    # number of sentences to get
    num_data = 1

    # get the data
    english_sentences = get_random_sentences(num_data, 'en')
    dutch_sentences = get_random_sentences(num_data, 'nl')

    # write the lists to .dat because csv is too mainstream or something
    output_file = 'training_data_' + str(num_data) + '.dat'
    file = open(output_file, 'w')

    for sample in english_sentences:
        file.write('en|'+sample+'\n')

    for sample in dutch_sentences:
        file.write('nl|'+sample)

    # close file
    file.close()


if __name__ == "__main__":
    main()
