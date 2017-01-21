import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import sqlite3
import downloader

def BVLSMain():
    BVLSaddDir('Update bestand','http://sebn.sc/',80,'http://sebn.sc/images/logo.png')
    listhtml = getHtml('http://www.welkedagishetvandaag.nl/','http://www.welkedagishetvandaag.nl/')
    match = re.compile('<div id="day">.*?h1>(.*?)</h1>.*?h1>(.*?)</h1>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for text1, text2 in match:
        BVLSaddDir('[B]' + text1 + ' [/B]' + text2,'',66,'http://sebn.sc/images/logo.png', Folder=False) 
    BVLSaddDir('Maandag','http://sebn.sc/',67,'http://sebn.sc/images/logo.png')
    BVLSaddDir('Dinsdag','http://sebn.sc/',68,'http://sebn.sc/images/logo.png')
    BVLSaddDir('Woensdag','http://sebn.sc/',69,'http://sebn.sc/images/logo.png')
    BVLSaddDir('Donderdag','http://sebn.sc/',70,'http://sebn.sc/images/logo.png')
    BVLSaddDir('Vrijdag','http://sebn.sc/',71,'http://sebn.sc/images/logo.png')
    BVLSaddDir('Zaterdag','http://sebn.sc/',72,'http://sebn.sc/images/logo.png')
    BVLSaddDir('Zondag','http://sebn.sc/',73,'http://sebn.sc/images/logo.png')
    BVLSaddDir('Losse streams','http://sebn.sc/',54,'http://sebn.sc/images/logo.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def BVLSMaandag(url):
    listhtml = getHtml(url, '')
    matchmaandag = re.compile('<h1 style="color: #000;margin-bottom: 20px;">Maandag(.*?)<h1 style="color: #000;margin-bottom: 20px;">Dinsdag', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    datum = re.compile("(.*?)</h1>", re.IGNORECASE | re.DOTALL).findall(matchmaandag)
    for datum in datum:
        datum = 'Maandag' + datum
        BVLSaddDir('[B]' + datum + '[/B]','','','http://sebn.sc/images/logo.png', Folder=False)
    totaalwedstrijd = re.compile('<div class="match-date">(.*?)<!-- #AFBLIJVEN HIERONDER -->', re.IGNORECASE | re.DOTALL).findall(matchmaandag)
    for wedstrijden in totaalwedstrijd:
        wedstrijd = re.compile('<div class="day">(.*?)</div>.*?<div class="(.*?)".*?">.*?<div class="name">(.*?)</div></div>.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
        for tijd, imgcd, name, url in wedstrijd:
            imgurl = getHtml('http://sebn.sc/schedule/css/images.css', 'http://sebn.sc/schedule/css/images.css')
            img = re.compile(r"\." + imgcd + ":before.*?background: url\('(.*?)'", re.IGNORECASE | re.DOTALL).findall(imgurl)[0]
            if 'sebn.sc' in img:
                img = img
            else:
                img = 'http://sebn.sc' + img
            name = striphtml(name)
            name = name.replace('\n','').replace('\t','').replace('                 ',' ').replace('VS',' VS').replace('  ',' ')
            title = tijd + ': '+ name
            xbmc.log(title)
            url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
            addDir(title,url,59,img , fanart,'','','','')
            
            streams = re.compile('href="(.*?)".*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
            for url, name in streams:
                streams = '[COLOR cornflowerblue]- ' + name + '[/COLOR]'
                url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
                addDir(streams,url,59,'http://sebn.sc/images/logo.png' , fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def BVLSDinsdag(url):
    listhtml = getHtml(url, '')
    matchdinsdag = re.compile('<h1 style="color: #000;margin-bottom: 20px;">Dinsdag(.*?)<h1 style="color: #000;margin-bottom: 20px;">Woensdag', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    datum = re.compile("(.*?)</h1>", re.IGNORECASE | re.DOTALL).findall(matchdinsdag)
    for datum in datum:
        datum = 'Dinsdag' + datum
        BVLSaddDir('[B]' + datum + '[/B]','','','http://sebn.sc/images/logo.png', Folder=False)
    totaalwedstrijd = re.compile('<div class="match-date">(.*?)<!-- #AFBLIJVEN HIERONDER -->', re.IGNORECASE | re.DOTALL).findall(matchdinsdag)
    for wedstrijden in totaalwedstrijd:
        wedstrijd = re.compile('<div class="day">(.*?)</div>.*?<div class="(.*?)".*?">.*?<div class="name">(.*?)</div></div>.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
        for tijd, imgcd, name, url in wedstrijd:
            imgurl = getHtml('http://sebn.sc/schedule/css/images.css', 'http://sebn.sc/schedule/css/images.css')
            img = re.compile(r"\." + imgcd + ":before.*?background: url\('(.*?)'", re.IGNORECASE | re.DOTALL).findall(imgurl)[0]
            if 'sebn.sc' in img:
                img = img
            else:
                img = 'http://sebn.sc' + img
            name = striphtml(name)
            name = name.replace('\n','').replace('\t','').replace('                 ',' ').replace('VS',' VS').replace('  ',' ')
            title = tijd + ': '+ name
            xbmc.log(title)
            url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
            addDir(title,url,59,img , fanart,'','','','')
            
            streams = re.compile('href="(.*?)".*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
            for url, name in streams:
                streams = '[COLOR cornflowerblue]- ' + name + '[/COLOR]'
                url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
                addDir(streams,url,59,'http://sebn.sc/images/logo.png' , fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def BVLSWoensdag(url):
    listhtml = getHtml(url, '')
    matchwoensdag = re.compile('<h1 style="color: #000;margin-bottom: 20px;">Woensdag(.*?)<h1 style="color: #000;margin-bottom: 20px;">Donderdag', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    datum = re.compile("(.*?)</h1>", re.IGNORECASE | re.DOTALL).findall(matchwoensdag)
    for datum in datum:
        datum = 'Woensdag' + datum
        BVLSaddDir('[B]' + datum + '[/B]','','','http://sebn.sc/images/logo.png', Folder=False)
    totaalwedstrijd = re.compile('<div class="match-date">(.*?)<!-- #AFBLIJVEN HIERONDER -->', re.IGNORECASE | re.DOTALL).findall(matchwoensdag)
    for wedstrijden in totaalwedstrijd:
        wedstrijd = re.compile('<div class="day">(.*?)</div>.*?<div class="(.*?)".*?">.*?<div class="name">(.*?)</div></div>.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
        for tijd, imgcd, name, url in wedstrijd:
            imgurl = getHtml('http://sebn.sc/schedule/css/images.css', 'http://sebn.sc/schedule/css/images.css')
            img = re.compile(r"\." + imgcd + ":before.*?background: url\('(.*?)'", re.IGNORECASE | re.DOTALL).findall(imgurl)[0]
            if 'sebn.sc' in img:
                img = img
            else:
                img = 'http://sebn.sc' + img
            name = striphtml(name)
            name = name.replace('\n','').replace('\t','').replace('                 ',' ').replace('VS',' VS').replace('  ',' ')
            title = tijd + ': '+ name
            xbmc.log(title)
            url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
            addDir(title,url,59,img , fanart,'','','','')
            
            streams = re.compile('href="(.*?)".*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
            for url, name in streams:
                streams = '[COLOR cornflowerblue]- ' + name + '[/COLOR]'
                url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
                addDir(streams,url,59,'http://sebn.sc/images/logo.png' , fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def BVLSDonderdag(url):
    listhtml = getHtml(url, '')
    matchdonderdag = re.compile('<h1 style="color: #000;margin-bottom: 20px;">Donderdag(.*?)<h1 style="color: #000;margin-bottom: 20px;">Vrijdag', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    datum = re.compile("(.*?)</h1>", re.IGNORECASE | re.DOTALL).findall(matchdonderdag)
    for datum in datum:
        datum = 'Donderdag' + datum
        BVLSaddDir('[B]' + datum + '[/B]','','','http://sebn.sc/images/logo.png', Folder=False)
    totaalwedstrijd = re.compile('<div class="match-date">(.*?)<!-- #AFBLIJVEN HIERONDER -->', re.IGNORECASE | re.DOTALL).findall(matchdonderdag)
    for wedstrijden in totaalwedstrijd:
        wedstrijd = re.compile('<div class="day">(.*?)</div>.*?<div class="(.*?)".*?">.*?<div class="name">(.*?)</div></div>.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
        for tijd, imgcd, name, url in wedstrijd:
            imgurl = getHtml('http://sebn.sc/schedule/css/images.css', 'http://sebn.sc/schedule/css/images.css')
            img = re.compile(r"\." + imgcd + ":before.*?background: url\('(.*?)'", re.IGNORECASE | re.DOTALL).findall(imgurl)[0]
            if 'sebn.sc' in img:
                img = img
            else:
                img = 'http://sebn.sc' + img
            name = striphtml(name)
            name = name.replace('\n','').replace('\t','').replace('                 ',' ').replace('VS',' VS').replace('  ',' ')
            title = tijd + ': '+ name
            xbmc.log(title)
            url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
            addDir(title,url,59,img , fanart,'','','','')
            
            streams = re.compile('href="(.*?)".*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
            for url, name in streams:
                streams = '[COLOR cornflowerblue]- ' + name + '[/COLOR]'
                url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
                addDir(streams,url,59,'http://sebn.sc/images/logo.png' , fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def BVLSVrijdag(url):
    listhtml = getHtml(url, '')
    matchvrijdag = re.compile('<h1 style="color: #000;margin-bottom: 20px;">Vrijdag(.*?)<h1 style="color: #000;margin-bottom: 20px;">Zaterdag', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    datum = re.compile("(.*?)</h1>", re.IGNORECASE | re.DOTALL).findall(matchvrijdag)
    for datum in datum:
        datum = 'Vrijdag' + datum
        BVLSaddDir('[B]' + datum + '[/B]','','','http://sebn.sc/images/logo.png', Folder=False)
    totaalwedstrijd = re.compile('<div class="match-date">(.*?)<!-- #AFBLIJVEN HIERONDER -->', re.IGNORECASE | re.DOTALL).findall(matchvrijdag)
    for wedstrijden in totaalwedstrijd:
        wedstrijd = re.compile('<div class="day">(.*?)</div>.*?<div class="(.*?)".*?">.*?<div class="name">(.*?)</div></div>.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
        for tijd, imgcd, name, url in wedstrijd:
            imgurl = getHtml('http://sebn.sc/schedule/css/images.css', 'http://sebn.sc/schedule/css/images.css')
            img = re.compile(r"\." + imgcd + ":before.*?background: url\('(.*?)'", re.IGNORECASE | re.DOTALL).findall(imgurl)[0]
            if 'sebn.sc' in img:
                img = img
            else:
                img = 'http://sebn.sc' + img
            name = striphtml(name)
            name = name.replace('\n','').replace('\t','').replace('                 ',' ').replace('VS',' VS').replace('  ',' ')
            title = tijd + ': '+ name
            xbmc.log(title)
            url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
            addDir(title,url,59,img , fanart,'','','','')
            
            streams = re.compile('href="(.*?)".*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
            for url, name in streams:
                streams = '[COLOR cornflowerblue]- ' + name + '[/COLOR]'
                url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
                xbmc.log(url)
                addDir(streams,url,59,'http://sebn.sc/images/logo.png' , fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def BVLSZaterdag(url):
    listhtml = getHtml(url, '')
    matchzaterdag = re.compile('<h1 style="color: #000;margin-bottom: 20px;">Zaterdag(.*?)<h1 style="color: #000;margin-bottom: 20px;">Zondag', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    datum = re.compile("(.*?)</h1>", re.IGNORECASE | re.DOTALL).findall(matchzaterdag)
    for datum in datum:
        datum = 'Zaterdag' + datum
        BVLSaddDir('[B]' + datum + '[/B]','','','http://sebn.sc/images/logo.png', Folder=False)
    totaalwedstrijd = re.compile('<div class="match-date">(.*?)<!-- #AFBLIJVEN HIERONDER -->', re.IGNORECASE | re.DOTALL).findall(matchzaterdag)
    for wedstrijden in totaalwedstrijd:
        wedstrijd = re.compile('<div class="day">(.*?)</div>.*?<div class="(.*?)".*?">.*?<div class="name">(.*?)</div></div>.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
        for tijd, imgcd, name, url in wedstrijd:
            imgurl = getHtml('http://sebn.sc/schedule/css/images.css', 'http://sebn.sc/schedule/css/images.css')
            img = re.compile(r"\." + imgcd + ":before.*?background: url\('(.*?)'", re.IGNORECASE | re.DOTALL).findall(imgurl)[0]
            if 'sebn.sc' in img:
                img = img
            else:
                img = 'http://sebn.sc' + img
            name = striphtml(name)
            name = name.replace('\n','').replace('\t','').replace('                 ',' ').replace('VS',' VS').replace('  ',' ')
            title = tijd + ': '+ name
            xbmc.log(title)
            url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
            addDir(title,url,59,img , fanart,'','','','')
            
            streams = re.compile('href="(.*?)".*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
            for url, name in streams:
                streams = '[COLOR cornflowerblue]- ' + name + '[/COLOR]'
                url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
                addDir(streams,url,59,'http://sebn.sc/images/logo.png' , fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def BVLSZondag(url):
    listhtml = getHtml(url, '')
    matchzondag = re.compile('<h1 style="color: #000;margin-bottom: 20px;">Zondag(.*?)<div class="sidebarbox-title">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    datum = re.compile("(.*?)</h1>", re.IGNORECASE | re.DOTALL).findall(matchzondag)
    for datum in datum:
        datum = 'Zondag' + datum
        BVLSaddDir('[B]' + datum + '[/B]','','','http://sebn.sc/images/logo.png', Folder=False)
    totaalwedstrijd = re.compile('<div class="match-date">(.*?)<!-- #AFBLIJVEN HIERONDER -->', re.IGNORECASE | re.DOTALL).findall(matchzondag)
    for wedstrijden in totaalwedstrijd:
        wedstrijd = re.compile('<div class="day">(.*?)</div>.*?<div class="(.*?)".*?">.*?<div class="name">(.*?)</div></div>.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
        for tijd, imgcd, name, url in wedstrijd:
            imgurl = getHtml('http://sebn.sc/schedule/css/images.css', 'http://sebn.sc/schedule/css/images.css')
            img = re.compile(r"\." + imgcd + ":before.*?background: url\('(.*?)'", re.IGNORECASE | re.DOTALL).findall(imgurl)[0]
            if 'sebn.sc' in img:
                img = img
            else:
                img = 'http://sebn.sc' + img
            name = striphtml(name)
            name = name.replace('\n','').replace('\t','').replace('                 ',' ').replace('VS',' VS').replace('  ',' ')
            title = tijd + ': '+ name
            xbmc.log(title)
            url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
            addDir(title,url,59,img , fanart,'','','','')
            
            streams = re.compile('href="(.*?)".*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(wedstrijden)
            for url, name in streams:
                streams = '[COLOR cornflowerblue]- ' + name + '[/COLOR]'
                url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sebn.sc/' + url
                addDir(streams,url,59,'http://sebn.sc/images/logo.png' , fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
    
def downloaden():
    path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.TVEE','temp'))
    url = ''
    name = 'SEBN'
    lib=os.path.join(path, name)
    downloader.download(url, lib)
    if os.path.exists(lib):
        addonfolder = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.TVEE','home'))
        time.sleep(2)
        dp = xbmcgui.DialogProgress()
        dp.create("TVEE","Downloaden gereed",'', '...')    
        dp.close()
        
def BVLSaddDir(name, url, mode, iconimage, page=None, channel=None, section=None, keyword='', Folder=True, fanart=None):
    if url.startswith("plugin://"):
        u = url
    else:
        u = (sys.argv[0] +
             "?url=" + urllib.quote_plus(url) +
             "&mode=" + str(mode) +
             "&page=" + str(page) +
             "&channel=" + str(channel) +
             "&section=" + str(section) +
             "&keyword=" + urllib.quote_plus(keyword) +
             "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    if not fanart:
        fanart = FANART
    liz.setArt({'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=Folder)
    return ok

def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)

def getHtml(url, referer=None, hdr=None, data=None):
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
    if not hdr:
        req = urllib2.Request(url, data, headers)
    else:
        req = urllib2.Request(url, data, hdr)
    if referer:
        req.add_header('Referer', referer)
    response = urllib2.urlopen(req, timeout=60)
    data = response.read()    
    response.close()
    return data