# -*- coding: utf-8
import os
import requests
from bs4 import BeautifulSoup

def findPicNum():
    url = 'http://wufazhuce.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    num = ''
    url = str(soup.find_all('a')[1]['href'])
    url = url.split('/')
    return url[-1]

def getImgSrc(num):
    url = 'http://wufazhuce.com/one/%d' % num
    r = requests.get(url)
    if r.status_code != 200:
        print r.status_code,
        return 'error'
    else:
        soup = BeautifulSoup(r.text, "html.parser")
        piclist = soup.find_all('img')
        return piclist[1]['src']

def mkdir():
    cwd = os.getcwd()
    dirpath = os.path.join(cwd, 'OneImg')
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    return dirpath

def saveImg(src, img_path):
    r = requests.get(src, stream=True)
    img = r.raw.read()
    f = open(img_path, 'wb')
    f.write(img)
    f.close()

if __name__ == '__main__':
    num = int(findPicNum())
    save_path = mkdir()
    while num > 0:
        imgname = '%d.jpg' % num
        img_path = os.path.join(save_path, imgname)
        if os.path.exists(img_path):
            print imgname, 'already exists'
            num -= 1
            continue

        src = getImgSrc(num)
        if src == 'error':
            print imgname
            num -= 1
            continue

        else:
            saveImg(src, img_path)
            print 'success', imgname
            num -= 1

    print 'Done!'