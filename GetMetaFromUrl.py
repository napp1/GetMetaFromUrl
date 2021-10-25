from bs4 import BeautifulSoup
import csv
import requests


def GetMetaFromUrl(url):
    '''Get meta data from url and write it in data.tsv.'''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="lxml")
    title = soup.title.string
    meta = soup.find_all('meta')
    description=''
    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description']:
            description=tag.attrs['content']
    f = open('data.tsv', 'a')
    f.write(url+"\t"+title+"\t"+description+"\n")
    f.close()

def file_len(fname):
    '''Just return the number of line for the input file url.tsv.
    It will be used to calculate the overall progress.'''
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



with open("url.tsv", "r") as f:
    all_the_urls = csv.reader(f, dialect="excel-tab")
    progress = 0
        
    for i in all_the_urls:
        print(i)
        if i == []: #searching for empy line
            progress += 1
            print(str(100*progress/(file_len("url.tsv")))+"% - Empty line skipped")
        else:
            try:
                progress += 1
                print(str(100*progress/(file_len("url.tsv")))+"% - Running: "+str(i[0]))
                GetMetaFromUrl(str(i[0]))
            
            except ValueError:
                f = open('error-log.txt', 'a')
                f.write(str(i[0])+",")
                f.close()