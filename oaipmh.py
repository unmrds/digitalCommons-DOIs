import requests
from xml.etree import ElementTree


def oairesume(oaiurl, token):
    ns = {'dc_oai': 'http://www.openarchives.org/OAI/2.0/',
          'dc': 'http://purl.org/dc/elements/1.1/'}
    payload = {'verb': 'ListRecords', 'resumptionToken' : token}
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
        oairesume(oaiurl, token.text)


def oaiharvest(oaiurl, getset):
    ns = {'dc_oai': 'http://www.openarchives.org/OAI/2.0/',
          'dc': 'http://purl.org/dc/elements/1.1/'}
    payload = {'verb': 'ListRecords', 'metadataPrefix': 'dcs', 'set': getset}
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
        oairesume(oaiurl, token.text)


oaiurl = "http://digitalrepository.unm.edu/do/oai/"

getset = "publication:nawrs"

oaiharvest(oaiurl, getset)