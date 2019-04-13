import wikipedia
import csv


def clean(text):
    # remove punctuation
    text.strip('.,;:/?][{}(!@#$%^&*+=-_)')
    # extract first 15 words
    text = ' '.join(text.split()[:15])
    return text


def get_text(page_name):
    # fetch summary
    text = wikipedia.page(page_name).summary()

    # clean text to meet requirements of school project data samples
    text = clean(text)

    return text

def get_random_dutch(pages):
    # TODO:
    return 0


def get_random_english(num_pages):
    sentences = []
    # generate random pages
    pages = [wikipedia.random(1) for i in range(num_pages)]
    for page in pages:
        # get text from each page
        for text in get_text(page):
            # append to sentences
            sentences.append(text)
    return sentences


def main():
    english_sentences = get_random_english(10)
    print(english_sentences)


if __name__ == "__main__":
    main()
