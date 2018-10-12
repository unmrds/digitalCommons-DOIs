import requests
from xml.etree import ElementTree


def writexml(xmldata, fc):
    with open('output/result_'+str(fc)+'.xml', 'w') as o:
        o.write(xmldata)
        o.close
    return

def oaiharvest(oaiurl, getset='', token='', fc=1):
    ns = {'dc_oai': 'http://www.openarchives.org/OAI/2.0/',
          'dc': 'http://purl.org/dc/elements/1.1/'}
    if getset != '':
        payload = {'verb': 'ListRecords', 'metadataPrefix': 'dcs', 'set': getset}
    elif token != '':
        payload = {'verb': 'ListRecords', 'resumptionToken': token}
    r = requests.get(oaiurl, params=payload)
    r.encoding = 'utf-8'
    root = ElementTree.fromstring(r.content)
    recs = root.find('dc_oai:ListRecords', ns)
    items = recs.findall('dc_oai:record', ns)
    print(str(len(items)) + " items in current set")
    token = recs.find("dc_oai:resumptionToken", ns)
    if token.text is None:
        writexml(r.text, fc)
        print('no more requests')
    else:
        writexml(r.text, fc)
        fc += 1
        oaiharvest(oaiurl, token=token.text, fc=fc)


oaiurl = "http://digitalrepository.unm.edu/do/oai/"

getset = "publication:energizenm"

oaiharvest(oaiurl, getset=getset)