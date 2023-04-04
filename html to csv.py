from bs4 import BeautifulSoup
import csv
import random

# open skills.html
with open('skills.html', 'r') as f:
    # read the file
    html = f.read()
    # parse the html
    soup = BeautifulSoup(html, 'html.parser')
    # get the words list
    list = soup.find('ul', attrs={'class': 'plain list'})
    
    # iterate over the list, divide words to topics
    # use a dictionary to store the words
    
    words = []
    
    for item in list.find_all('li'):
        try:
            # word is the text of the span with "wA" class
            word = item.find('span', attrs={'class': 'wA'}).text
            extra = item.find('small').text
            # meaning is the title of the 4th span
            meaning = item.find_all('span')[3].get('title')
            # topic is the title of the 2nd span
            topic = item.find_all('span')[1].get('title')
            
            # remove extra whitespace and newlines, and · from extra
            extra = extra.replace('·', '').strip().replace('\n', '')
            # remove repeated spaces
            extra = ' '.join(extra.split())
            

            words.append([
                word,
                extra + '<br />' + meaning,
                topic
            ])
        except:
            print('ERROR')
            print(item)
        

    # shuffle the words
    random.shuffle(words)
    
    
    # save the words to csv, one file per topic
    for topic in set([word[2] for word in words]):
        with open('out/' + topic + '.csv', 'w') as f:
            writer = csv.writer(f)
            for word in words:
                if word[2] == topic:
                    writer.writerow(word)
    
    