pyPaymentSense
==============

Python code to interact with the Payment Sense API, including full validation
for all variables.

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
ResultDeliveryMethod="POST"
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