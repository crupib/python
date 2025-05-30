""" Retrieve and print from url """
import sys
from urllib.request import urlopen
def fetch_words(url):
    """ Get words from url text file """
    story = urlopen(url)
    story_words = []
    for line in story:
       line_words = line.decode('utf-8').split()
       for word in line_words:
          story_words.append(word)
    story.close()
    return story_words
def print_items(items):
    """ print items """
    for items in items:
       print(items)

def main(url):
    """ main """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
   main(sys.argv[1])
