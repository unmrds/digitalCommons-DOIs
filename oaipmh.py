import requests
from xml.etree import ElementTree


def oaiharvest(oaiurl, getset='', token=''):
    ns = {'dc_oai': 'http://www.openarchives.org/OAI/2.0/',
          'dc': 'http://purl.org/dc/elements/1.1/'}
    if getset != '':
        payload = {'verb': 'ListRecords', 'metadataPrefix': 'dcs', 'set': getset}
    elif token != '':
        payload = {'verb': 'ListRecords', 'resumptionToken': token}
    r = requests.get(oaiurl, params=payload)
    #print(r.url)
    tree = ElementTree.fromstring(r.content)
    recs = tree.find('dc_oai:ListRecords', ns)
    items = recs.findall('dc_oai:record', ns)
    print(len(items))
    token = recs.find('dc_oai:resumptionToken', ns)
    if token.text is None:
        print('no more requests')
    else:
        print(token.text)
        oaiharvest(oaiurl, token=token.text)


oaiurl = "http://digitalrepository.unm.edu/do/oai/"

getset = "publication:nawrs"

oaiharvest(oaiurl, getset=getset)