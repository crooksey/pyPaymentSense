# coding: utf-8
import datetime
import pytz
import requests
import paymentsense
from paymentsense import build_hash

# Lets build a POST
# These variables are always required
post_addr = "https://mms.paymentsensegateway.com/Pages/PublicPages/PaymentForm.aspx"
PreSharedKey = "XXX"
MerchantID = "XXX" # replace XXX values with your own
Password = "XXX"
# no decimal point in values, e.g. 34120 is 341.20
Amount = "34120"
CurrencyCode = "826"
EchoAVSCheckResult = False
EchoCardType = False
OrderID = "testOrder416"
TransactionType = "SALE"
CallbackURL = "http://solentwholesale.com"
EmailAddressEditable = True
PhoneNumberEditable = False
CV2Mandatory = True
Address1Mandatory = True
CityMandatory = False
PostCodeMandatory = True
StateMandatory = False
CountryMandatory = False
ResultDeliveryMethod="POST"
PaymentFormDisplaysResult = True
EchoCV2CheckResult = False
EchoThreeDSecureAuthenticationCheckResult = False
# Non required variables, we define these now to enable the full building
# of the URL further down, they cannot be passed as None or they will not
# be built into the request, which will cause a hash digest error
ServerResultURL = ""
AVSOverridePolicy="" 
ThreeDSecureOverridePolicy="" 
CV2OverridePolicy="" 
OrderDescription="" 
CustomerName="" 
Address1=""
Address2="" 
Address3="" 
Address4="" 
City="" 
State="" 
PostCode="" 
CountryCode="" 
EmailAddress="" 
PhoneNumber=""


# datetime check, we set this manually, it is not passed to the function
# TransactionDateTime needs to be in the format of 
# “YYYY-MM-DD HH:MM:SS +00:00”, with the time in 24hr format, 
# where 00:00 is the offset from UTC - e.g. “2013-07-22 13:46 +01:00”

# define the output format
fmt = '%Y-%m-%d %H:%M:%S %z'

# Add your own timezone here
d = datetime.datetime.now(pytz.timezone("Europe/London"))
TransactionDateTime_unclean = d.strftime(fmt)

# Now the python datetime method doesnt include a colon in the UTC offset
# which means we need this lovely messy code below
last_c1 = TransactionDateTime_unclean[-1]
last_c2 = TransactionDateTime_unclean[-2]
end_str = ":" + last_c2 + last_c1
TransactionDateTime_remove = TransactionDateTime_unclean[:-2]
TransactionDateTime = TransactionDateTime_remove + end_str

sha1_hash = build_hash(
	PreSharedKey = PreSharedKey,
	MerchantID = MerchantID,
	Password = Password,
	Amount = Amount,
	CurrencyCode = CurrencyCode,
	EchoAVSCheckResult = EchoAVSCheckResult, 
	EchoCV2CheckResult = EchoCV2CheckResult,
	EchoThreeDSecureAuthenticationCheckResult = EchoThreeDSecureAuthenticationCheckResult,
	EchoCardType = EchoCardType, 
	OrderID = OrderID,
	TransactionType = TransactionType,
	TransactionDateTime=TransactionDateTime,
	CallbackURL = CallbackURL,
	EmailAddressEditable = EmailAddressEditable, 
	PhoneNumberEditable = PhoneNumberEditable,
	CV2Mandatory = CV2Mandatory,
	Address1Mandatory = Address1Mandatory,
	CityMandatory = CityMandatory,
	PostCodeMandatory = PostCodeMandatory,
	StateMandatory = StateMandatory,
	CountryMandatory = CountryMandatory,
	ResultDeliveryMethod=ResultDeliveryMethod,
	PaymentFormDisplaysResult = PaymentFormDisplaysResult)


# now we have the hash, build the request data pairs
data = {
'HashDigest': sha1_hash,
'MerchantID': MerchantID,
'Amount': Amount,
'CurrencyCode': CurrencyCode,
'EchoAVSCheckResult': EchoAVSCheckResult,
'EchoCV2CheckResult': EchoCV2CheckResult,
'EchoThreeDSecureAuthenticationCheckResult': 
	EchoThreeDSecureAuthenticationCheckResult,
'EchoCardType': EchoCardType,
'AVSOverridePolicy': AVSOverridePolicy,
'CV2OverridePolicy': CV2OverridePolicy,
'ThreeDSecureOverridePolicy': ThreeDSecureOverridePolicy,
'OrderID': OrderID,
'TransactionType': TransactionType,
'TransactionDateTime': TransactionDateTime,
'CallbackURL': CallbackURL,
'OrderDescription': OrderDescription,
'CustomerName': CustomerName,
'Address1': Address1,
'Address2': Address2,
'Address3': Address3,
'Address4': Address4,
'City': City,
'State': State,
'PostCode': PostCode,
'CountryCode': CountryCode,
'EmailAddress': EmailAddress,
'PhoneNumber': PhoneNumber,
'EmailAddressEditable': EmailAddressEditable,
'PhoneNumberEditable': PhoneNumberEditable,
'CV2Mandatory': CV2Mandatory,
'Address1Mandatory': Address1Mandatory,
'CityMandatory': CityMandatory,
'PostCodeMandatory': PostCodeMandatory,
'StateMandatory': StateMandatory,
'CountryMandatory': CountryMandatory,
'ResultDeliveryMethod': ResultDeliveryMethod,
'ServerResultURL': ServerResultURL,
'PaymentFormDisplaysResult': PaymentFormDisplaysResult
}

r = requests.post(post_addr, params=data)

url = r.url
url_clean =  url.replace("None","")
print ''
print 'Clean URL: ' + r.url