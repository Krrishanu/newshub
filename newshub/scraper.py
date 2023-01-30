import requests
import xmltodict
from models import db, Daily, News
'''
sources = [{'name':"BD24Live.com",
            'url':"https://www.bd24live.com/feed"},
           {'name':"Bangla News",
            'url':"https://www.banglanews24.com/rss/rss.xml"},
            {'name':"JUGANTOR",
            'url':"https://www.jugantor.com/feed/rss.xml"},
           {'name':"jagonews24.com",
            'url':"https://www.jagonews24.com/rss/rss.xml"},
           {'name':"Prothom Alo",
            'url':"https://www.prothomalo.com/feed/"}]

obs = []
for i in sources:
    obj = Daily(**i)
    obs.append(obj)

for i in obs:
    db.session.add(i)

db.session.commit()

'''





def get_1():

    daily = Daily.query.get(1)

    r = requests.get(daily.url)

#    print(r.status_code)

    meta = xmltodict.parse(r.content)
    channel = meta['rss'][ 'channel']
    item = meta['rss']['channel']['item']

# Add data to db
    
    nws_obj = []
    for i in item:
        nws = News(date=i['pubDate'],
            title=i['title'],
            link=i['link'],
            content=i['content:encoded'],
            description=i['description'],
            daily_id= daily.id) 
        
        nws_obj.append(nws)

    for i in nws_obj:
        db.session.add(i)

    db.session.commit()

def get_2():

    daily = Daily.query.get(2)

    r = requests.get(daily.url)

#    print(r.status_code)

    meta = xmltodict.parse(r.content)
    channel = meta['rss'][ 'channel']
    item = meta['rss']['channel']['item'] 


    # add to db
    nws_obj = []


    for i in item:
        nws = News(date=i['pubDate'],
            title=i['title'],
            link=i['link'],
            description=i['description'],
            daily_id= daily.id) 
        
        nws_obj.append(nws)

    for i in nws_obj:
        db.session.add(i)

    db.session.commit()

def get_3():

    daily = Daily.query.get(3)

    r = requests.get(daily.url)

    meta = xmltodict.parse(r.content)
    channel = meta['rss'][ 'channel']
    item = meta['rss']['channel']['item']


    nws_obj = []
    for i in item:
        nws = News(date=i['pubDate'],
            title=i['title'],
            link=i['link'],
            content=i['content:encoded'],
            description=i['description'],
            daily_id= daily.id) 
        
        nws_obj.append(nws)

    for i in nws_obj:
        db.session.add(i)

    db.session.commit()


def get_4():

    daily = Daily.query.get(4)

    r = requests.get(daily.url)

    try:
        print(r.status_code)
        r = requests.get(daily.url)
    except:
        print(r.status_code)
    
    try:
        meta = xmltodict.parse(r.content)
    except:
        print("ERROR!")
        return

    item = meta['rss']['channel']['item']


    nws_obj = []
    for i in item:
        nws = News(date=i['pubDate'],
            title=i['title'],
            link=i['link'],
            content=i['content:encoded'],
            description=i['description'],
            daily_id= daily.id) 
        
        nws_obj.append(nws)

    for i in nws_obj:
        db.session.add(i)

    db.session.commit()




def get_5():

    daily = Daily.query.get(5)

    r = requests.get(daily.url)

    meta = xmltodict.parse(r.content)
 #   channel = meta['rss'][ 'channel']
 #   item = meta['rss']['channel']['item']
    item = meta['feed'] ['entry']

 
    nws_obj = []
    for i in item:
        nws = News(date=i['published'],
            title=i['title'],
            link=i['link']['@href'],
            description=i['summary'],
            daily_id= daily.id) 
     
        nws_obj.append(nws)

    for i in nws_obj:
        db.session.add(i)

    db.session.commit()

def get_all():
    # Delete all Data
    News.query.delete()

    
    get_1()
    get_2()
    get_3()
    get_4()
    get_5()

"""
    print(data['title'])
    print(data['date'])
    print(data['link'])
    print(data['description'])
    print(data['image'])
    print(data['item'][0].keys())
"""


    #item_keys(['title', 'link', 'dc:creator', 'pubDate', 'category', 'guid', 'description', 'content:encoded'])

#url = sources[0]

if __name__ == "__main__":
    bd24live()