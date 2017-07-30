#https://fedorahosted.org/suds/wiki/Documentation

import logging
logging.basicConfig(level=logging.INFO)

import suds
from suds.client import Client
logging.getLogger('suds.client').setLevel(logging.DEBUG)

url = 'https://www.HealthEquity.com/Partner/MemberBalanceWebService.asmx?wsdl'

client = Client(url)

'''myheaders = dict(Username='BCBSMA_websvc', Password='MhGn031105K')
client.set_options(soapheaders=myheaders)'''

token = client.factory.create('MemberBalanceServiceAuthHeader')
token.Username = 'BCBSMA_websvc'
token.Password = 'MhGn031105K'
client.set_options(soapheaders=token)

result = client.service.GetMemberBalance('','981522383',4,4)
print(result)

'''' ******************************************* Call Accums test ***************************************************************************'''

#url2 = 'https://tstwas1.bcbsma.com:443/EligibilityComponent/services/eligibility/getBenefitsAndAccums?wsdl'

'''client = Client(url2)'''

'''import base64
username = 'mcentral01'
password = 'member@service'
#base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
base64string = '%s,%s' % (username, password)
authenticationHeader = {
    "SOAPAction" : "EligibilityInquiry",
    "Authorization" : "Basic %s" % base64string
}
client = Client(url=url2, headers=authenticationHeader)'''

'''from suds.wsse import *
security = Security()
token = UsernameToken('mcentral01', 'member@service')
security.tokens.append(token)
client.set_options(wsse=security)'''

'''from suds.transport.http import HttpAuthenticated
def main():
    url = 'https://tstwas1.bcbsma.com:443/EligibilityComponent/services/eligibility/getBenefitsAndAccums?wsdl'
    credentials = dict(username='mcentral01', password='member@service')
    t = HttpAuthenticated(**credentials)
    client = Client(url, location='https://tstwas1.bcbsma.com:443/EligibilityComponent/services/eligibility/getBenefitsAndAccums', transport=t)
    print(client.last_sent())

if __name__=="__main__":
    main()'''
    

#result = client.service.EligibilityInquiry()
#print(result)

'''' ******************************************* Weather App, After Member Logs in: Get Address/Plan Information/Account Information ** Stock price of company is public**************'''
'''' *******************************************White Pages ** If there is no Phone Number from Member Verify with Member *************************************************************'''
'''' ****************************************** Member Enters "Search Word" ** Google Search Results ** To find top 3 Google Search Results on Key word used *************************'''
''' ****** Get Relevant Benefit Lines *************************'''
''' ****** Get Relevant MCPS data *************************'''
''' ****** Get Relevant Providers *************************'''
''' ****** Get Relevant NCCT Data *************************'''
''' ****** Get Relevant Claims *************************'''
''' ****** Get HealthEquity *************************'''
'''' ******************************************* Google Geo Coding ** to find how far Provider is from me *******************************************************************'''
'''' ******************************************* Yelp ** To find if Provider Exists in Yelp and if so get Rating/Comments *****************************************************'''
'''' ******************************************* Healthgrades **To find if Provider Exists in Healthgrades and if so get Rating/Comments **********************************************************'''
'''' ******************************************* ZocDoc ** To find if Provider Exists in ZocDoc and if so get Rating/Comments ******************************************'''
