import os
import csv
import nltk

FIXTURES = os.path.join(os.path.dirname(__file__), "..", "fixtures")
PRODUCTS = os.path.join(FIXTURES, "products")

def load_data(name):
    with open(os.path.join(PRODUCTS, name), 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

if __name__ == '__main__':
    amazon  = list(load_data('amazon.csv'))
    google  = list(load_data('google.csv'))
    mapping = list(load_data('perfect_mapping.csv'))

    print len(amazon)
    print len(google)
    print len(mapping)

    print amazon[0].keys()
    print google[0].keys()
    print mapping[0].keys()
