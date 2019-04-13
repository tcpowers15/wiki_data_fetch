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
    # again trying again if exception is thrown
    text = None
    while text is None:
        try:
            text = wikipedia.page(page_name).summary
        except:
            pass

    text = wikipedia.page(page_name).summary

    # clean text to meet requirements of school project data samples
    text = clean(text)

    return text

def get_random_dutch(pages):
    # TODO:
    return 0


def get_random_english(num_pages):
    sentences = []
    # generate random pages
    pages = []
    # request a random page from wikipedia
    # the package seems to throw a lot of busy
    # exceptions so I am taking the try try again approach
    for i in range(num_pages):
        result = None
        while result is None:
            try:
                # try to get page, and try again if error
                result = wikipedia.random(1)

            except:
                pass
        pages.append(result)

    for page in pages:
        # get text from each page
        sentences.append(get_text(page))
    return sentences


def main():
    english_sentences = get_random_english(1)
    print(english_sentences)
    print("fuck")


if __name__ == "__main__":
    main()
