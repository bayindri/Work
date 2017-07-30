from pysimplesoap.client import SoapClient
#import logging

#logging.basicConfig(level=logging.DEBUG)


#client = SoapClient(wsdl="https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx?WSDL",soap_ns = 'mem', action ='') # worked!
client = SoapClient(
    wsdl="https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx?wsdl",
    #soap_ns = 'mem',
    action ='MemberBalanceWebService/GetMemberBalance')

print("Target Namespace", client.namespace)
'''import pprint
pprint.pprint(client.services)'''

for service in client.services.values():
    for port in service['ports'].values():
        print(port['location'])
        for op in port['operations'].values():
            print('Name:', op['name'])
            print('Docs:', op['documentation'].strip())
            print('SOAPAction:', op['action'])
            print('Input', op['input']) # args type declaration
            print('Output', op['output']) # returns type declaration
            print

#client = SoapClient(location="https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx", action="MemberBalanceWebService", namespace="", ns="mem")

#client['mem:MemberBalanceServiceAuthHeader'] = {'mem:Username': 'BCBSMA_websvc', 'mem:Password': 'MhGn031105K'}
client['MemberBalanceServiceAuthHeader'] = {'Username': 'BCBSMA_websvc', 'Password': 'MhGn031105K'}
response = client.GetMemberBalance(SessionId='9999',MemberId='981522383',AccountTypeFlags=4,BalanceTypeFlags=4)
