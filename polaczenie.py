##from SOAPpy import WSDL
import zeep

wsdl = 'http://serwis.mobilotto.pl/mapi/index.php?soap=ssv1.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.getSymbianWyniki('2016-07-17'))


# wsdlFile = 'http://serwis.mobilotto.pl/mapi/index.php?soap=ssv1.wsdl'
# server = WSDL.Proxy(wsdlFile)
# #server.soapproxy.config.dumpSOAPIn = 1
# wynik = server.getSymbianWyniki('2016-07-17')
# mini = wynik['wynikiMini']
# for rec in mini['WynikMini']:
#     print (rec['data_losowania'],rec['numerki'])
