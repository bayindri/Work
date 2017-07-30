from pysimplesoap.client import SoapClient
#import logging

#logging.basicConfig(level=logging.DEBUG)


#client = SoapClient(wsdl="https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx?WSDL",soap_ns = 'mem', action ='') # worked!
client = SoapClient(
    wsdl="https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx?wsdl",
    #soap_ns = 'mem',
    action ='MemberBalanceWebService/GetMemberBalance',
    ns = 'mem')

print("Target Namespace", client.namespace)
import pprint
#pprint.pprint(client.services)

for service in client.services.values():
    for port in service['ports'].values():
        #print("PORT")
        #print(port)
        #print
        print(port['location'])
        # fix location (lhttps://www.HealthEquity.com:4000/Partner/MemberBalanceWebService.asmx is erroneous in the WSDL)
        port['location'] = "https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx"
        #print("AFTER PORT")
        #print(port['location'])
        #print
        for op in port['operations'].values():
            print("****************************")
            print(port)
            print(port['location'])
            print(op)
            print('Name:', op['name'])
            print('Docs:', op['documentation'].strip())
            print('Parts:', op['parts'])
            print('Parts:input_header:', op['parts']['input_header'])
            print('Parts:input_header:message:-', op['parts']['input_header']['message'])
            print('Parts:input_header:part:', op['parts']['input_header']['part'])
            print('Parts:input_body:', op['parts']['input_body'])
            print('Parts:output_header:', op['parts']['output_header'])
            print('Parts:output_body:', op['parts']['output_body'])
            print('SOAPAction:', op['action'])
            print('Input:', op['input']['GetMemberBalance']) # args type declaration
            print('SessionId:', op['input']['GetMemberBalance']['SessionId']) # args type declaration
            print('MemberId:', op['input']['GetMemberBalance']['MemberId']) # args type declaration
            print('AccountTypeFlags:', op['input']['GetMemberBalance']['AccountTypeFlags']) # args type declaration
            print('BalanceTypeFlags:', op['input']['GetMemberBalance']['BalanceTypeFlags']) # args type declaration
            print('Output:', op['output']) # returns type declaration
            print ("***************************")
            
# fix location (localhost:9050 is erroneous in the WSDL)
#client.services['IWebServiceService']['ports']['IWebServicePort']['location'] = "https://186.153.145.2:9050/trazamed.WebService"
#print(client.services.ports)
#client.services['MemberBalanceWebService']['ports']['MemberBalanceWebServicePort']['location'] = "https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx"
for service in client.services.values():
    for port in service['ports'].values():
        #print(port)
        print(port['location'])
   
#client = SoapClient(location="https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx", action="MemberBalanceWebService", namespace="", ns="mem")

client['mem:MemberBalanceServiceAuthHeader'] = {'mem:Username': 'BCBSMA_websvc', 'mem:Password': 'MhGn031105K'}
#client['MemberBalanceServiceAuthHeader'] = {'Username': 'BCBSMA_websvc', 'Password': 'MhGn031105K'}
#print(client.GetMemberBalance(SessionId='9999',MemberId='981522383',AccountTypeFlags=4,BalanceTypeFlags=4))
#pprint.pprint(client.GetMemberBalance(SessionId='9999',MemberId='981522383',AccountTypeFlags=4,BalanceTypeFlags=4))
#pprint.pprint(client.GetMemberBalance(MemberId='981522383',AccountTypeFlags=4,BalanceTypeFlags=4))
#pprint.pprint(client.GetMemberBalance(MemberId='981522383'))
#client.xml_request()
print(client.as_xml())
pprint.pprint(client.GetMemberBalance())
pprint.pprint(client.GetMemberBalance.header())
pprint.pprint(client.GetMemberBalance('','981522383',4,4))
pprint.pprint(client.services)
#pprint.pprint(client.GetMemberBalance(SessionId='9999',MemberId='981522383',AccountTypeFlags=4,BalanceTypeFlags=4))

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#response = client.GetMemberBalance(SessionId='9999',MemberId='981522383',AccountTypeFlags='4',BalanceTypeFlags='4')

'''from pysimplesoap.client import SoapClient
from pysimplesoap.simplexml import SimpleXMLElement

from lxml import objectify

client = SoapClient(
    location = "https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx",
    #action = 'MemberBalanceWebService/GetMemberBalance', # SOAPAction
    #ns = 'mem'
    )
params = SimpleXMLElement("""
<?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:mem="MemberBalanceWebService">
    <soapenv:Header>
    <mem:MemberBalanceServiceAuthHeader>
    <!--Optional:-->
    <mem:Username>BCBSMA_websvc</mem:Username>
    <!--Optional:-->
    <mem:Password>MhGn031105K</mem:Password>
    </mem:MemberBalanceServiceAuthHeader>
    </soapenv:Header>
    <soapenv:Body>
    <mem:GetMemberBalance>
    <!--Optional:-->
    <mem:SessionId>?</mem:SessionId>
    <!--Optional:-->
    <mem:MemberId>981522383</mem:MemberId>
    <mem:AccountTypeFlags>4</mem:AccountTypeFlags>
    <mem:BalanceTypeFlags>4</mem:BalanceTypeFlags>
    </mem:GetMemberBalance>
    </soapenv:Body>
    </soapenv:Envelope>""") # manually make request msg
response = client.call('mem:GetMemberBalance',params)
result = response.GetMemberBalanceResult 
print(result) # manully convert returned type'''


