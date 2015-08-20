pyPaymentSense
==============

Python code to interact with the Payment Sense API, including full validation
for all variables. Works with python 2/3 (example shown with print command
from python 2, but all code works with both python2 and python3).

The package can be install with:
```bash
$ pip install pypaymentsense
```


For a usage example see below:

```python
# coding: utf-8
import datetime
import pytz
import requests
import pypaymentsense
from pypaymentsense import build_hash, get_paymenturl

# Lets build a POST request

#######################################
# These variables are always required #
#######################################
post_addr = "https://mms.paymentsensegateway.com/Pages/PublicPages/PaymentForm.aspx"
# Note, the below details are obtained from Payment Snese once you have setup
# an account, and will be sent in TWO seperate emails when you first register
PreSharedKey = "YOUR-PSK-HERE"
MerchantID = "YOUR-MERCHANT-ID"
Password = "YOUR=PASSWORD-HERE"
# no decimal point in values, e.g. 34120 is 341.20
Amount = "34120"
# 826 is GBP
# Full list can be found here:
# http://developers.paymentsense.co.uk/hosted-integration-resources/
CurrencyCode = "826"
# Echo certain information back to the server so you can display on your
# callback page
EchoAVSCheckResult = False
EchoCardType = False
# Anything you want here
OrderID = "test Order416"
# SALE or PREAUTH
TransactionType = "SALE"
# The url the user will be returned to once payment has been made/declined
# It is a good idea to inlcude some JS code on this page to show the 
# user the results of the payment
CallbackURL = "http://example.com/your_callback"
# Self explanitory variables
EmailAddressEditable = True
PhoneNumberEditable = False
CV2Mandatory = True
Address1Mandatory = True
CityMandatory = False
PostCodeMandatory = True
StateMandatory = False
CountryMandatory = False
ResultDeliveryMethod="SERVER_PULL"
PaymentFormDisplaysResult = True
EchoCV2CheckResult = False
EchoThreeDSecureAuthenticationCheckResult = False
# Non required variables, we define these now to enable the full building
# of the URL, they can be passed as NONE if you do not want to include them
# in the post
ServerResultURL = None
OrderDescription= "Example Description"
CustomerName = "John Smith"
Address1 = "15 Faithfull Street"
Address2 = None
Address3 = None
Address4 = None
City = "Chichester"
State = "West Sussex"
PostCode = "XX2 5AW"
# List of country codes can be found here:
# http://developers.paymentsense.co.uk/hosted-integration-resources/
CountryCode = None
EmailAddress = "luke@solentwholesale.com"
PhoneNumber = "01243 774626"

# Now we need to set our timezone
datetime_tz = datetime.datetime.now(pytz.timezone("Europe/London"))

payment_url = get_paymenturl(
			PreSharedKey=PreSharedKey, MerchantID=MerchantID,
			Password=Password, Amount=Amount,
			CurrencyCode=CurrencyCode, 
			EchoAVSCheckResult=EchoAVSCheckResult,
			EchoCardType=EchoCardType, OrderID=OrderID,
			TransactionType=TransactionType, CallbackURL=CallbackURL,
			EmailAddressEditable=EmailAddressEditable,
			PhoneNumberEditable=PhoneNumberEditable,
			CV2Mandatory=CV2Mandatory,
			Address1Mandatory=Address1Mandatory,
			CityMandatory=CityMandatory,
			PostCodeMandatory=PostCodeMandatory,
			StateMandatory=StateMandatory, 
			CountryMandatory=CountryMandatory,
			ResultDeliveryMethod=ResultDeliveryMethod,
			PaymentFormDisplaysResult=PaymentFormDisplaysResult,
			EchoCV2CheckResult= EchoCV2CheckResult,
			EchoThreeDSecureAuthenticationCheckResult=\
				EchoThreeDSecureAuthenticationCheckResult,
			ServerResultURL=ServerResultURL,
			OrderDescription=OrderDescription,
			CustomerName=CustomerName,
			Address1=Address1,
			Address2=Address2,
			Address3=Address3,
			Address4=Address4,
			City=City,
			State=State,
			PostCode=PostCode,
			CountryCode=CountryCode,
			EmailAddress=EmailAddress,
			PhoneNumber=PhoneNumber,
			datetime_tz=datetime_tz,
			post_addr=post_addr
			)
print "Genearated Url: " + payment_url
```

For this example we will use the SERVER_PULL method, what this does is, after a 
successful payment, certain details are passed back to your server, you then 
send these details back to paymentsense as a request. The request response contains
the details of the transaction, for example your callback view would have
the following code:

```python
import urllib
PreSharedKey = "YOUR-PSK-HERE"
Password = "YOUR-PASSWORD-HERE"
'''
This code works in pyramid + django, flask users should use the following
to perform a GET request:
hashdigest = request.args.get('HashDigest')
'''
# Get required variables from the URL string
hashdigest = request.GET['HashDigest']
merchantid = request.GET['MerchantID']
crossreference = request.GET['CrossReference']
orderid = request.GET['OrderID']
post_addr = "https://mms.paymentsensegateway.com/Pages/PublicPages/PaymentFormResultHandler.ashx"
data = {
    'MerchantID': merchantid,
    'Password': Password,
    'CrossReference': crossreference,
    }
# Send request to payment sense 
r = requests.post(post_addr, data=data)
# Result is the .text
url_raw =  r.text
# Decode to a URL string
url_decode = urllib.unquote(url_raw).decode('utf8') 
#You now have a url string E.g. Var1=abc&VAR2=def, pass this to another view
```

Now you have a URL string, you can pass this to the view used to show
the payment, results, in this view you would have code similar to:

```python
'''
This code works in pyramid + django, flask users should use the following
to perform a GET request:
status_code = request.args.get('StatusCode')
'''
# Here we will access the URL string passed from the previous view

if int(request.GET['StatusCode']) == 30:
    result = "Declined"
    result_logo = False
else:
    result = "Approved"
    result_logo = True

amount_raw = Decimal(request.GET['Amount'])
amount = amount_raw / 100

order_desc = request.GET['OrderDescription']

# create a dict with the results in
payment = {}
payment['result'] = result
payment['amount'] = amount
payment['card_type'] = request.GET['CardType']
payment['auth_code'] = request.GET['Message']
payment['order_desc'] = request.GET['OrderDescription']
payment['trade_name_str'] = trade_name_str
payment['trans_ref'] = request.GET['OrderID']
payment['cardholder_name'] = request.GET['CustomerName']

# You can then return the payment dict to the template for rendering
```

