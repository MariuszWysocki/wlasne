from SOAPpy import WSDL

import zeep

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))


wsdlFile = 'http://serwis.mobilotto.pl/mapi/index.php?soap=ssv1.wsdl'
server = WSDL.Proxy(wsdlFile)
#server.soapproxy.config.dumpSOAPIn = 1
wynik = server.getSymbianWyniki('2016-07-17')
mini = wynik['wynikiMini']
for rec in mini['WynikMini']:
    print (rec['data_losowania'],rec['numerki'])
