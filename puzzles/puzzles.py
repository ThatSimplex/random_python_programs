import sys
import re
import time
import requests

def scrape(start, stop, file):
    players = open(file, 'a')

    for i in range(start, stop+1):
        url = 'https://lichess.org/training/%g' % i
    
        result = requests.get(url)
    
        if result.status_code == 200:
            stuff = result.text.find(':[{')
            stuf2 = result.text.find('}],')

            play = []
            pla2 = []

            for m in re.finditer('userId', result.text[stuff:stuf2]):
                play.append(m.start())

            for n in re.finditer('name', result.text[stuff:stuf2]):
                pla2.append(n.start())

            players.write(str(i) + '\t' + result.text[stuff+play[0]+9:stuff+pla2[0]-3] + '\t' + result.text[stuff+play[1]+9:stuff+pla2[1]-3] + '\n')

            print(i)

            time.sleep(3)
        elif result.status_code == 429:
            print('Error: ' + str(result.status_code))
            time.sleep(60)
        else:
            print('Error: ' + str(result.status_code))
            time.sleep(10)
    
    players.close()
    print('Finished!')

scrape(15001, 16000, 'players2.txt')
