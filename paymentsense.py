# coding: utf-8
# send payments and information to payment sense API
import re
import hashlib

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def build_hash(PreSharedKey, MerchantID, Password, Amount,
	CurrencyCode, EchoAVSCheckResult, EchoCV2CheckResult, 
	EchoThreeDSecureAuthenticationCheckResult, EchoCardType, 
	OrderID, TransactionType, CallbackURL, EmailAddressEditable, 
	PhoneNumberEditable, CV2Mandatory, Address1Mandatory, CityMandatory, 
	PostCodeMandatory, StateMandatory, CountryMandatory, ResultDeliveryMethod,
	PaymentFormDisplaysResult, TransactionDateTime,	AVSOverridePolicy=None, 
	ThreeDSecureOverridePolicy=None, CV2OverridePolicy=None, 
	OrderDescription=None, CustomerName=None, Address1=None, Address2=None, 
	Address3=None, Address4=None, City=None, State=None, PostCode=None, 
	CountryCode=None, EmailAddress=None, PhoneNumber=None,
	ServerResultURL=None):

	# This is the order the variables must be passed to payment sense,
	# where None has been defined, these are the non required variables

	# PreSharedKey needs to validation

	if len(MerchantID) > 15:
		raise Exception("MerchantID must be no more than 15 characters")

	# Password needs to validation

	amount_test = is_number(Amount)
	if amount_test == False:
		raise Exception("Amount need to be a numerical value")

	# We hard code CurrencyCode to 826/GBP
	CurrencyCode = 826

	echo_avs_check = isinstance(EchoAVSCheckResult, bool)
	if echo_avs_check == False:
		raise Exception("EchoAVSCheckResult accepts True or False")

	echo_cv2_check = isinstance(EchoCV2CheckResult, bool)
	if echo_cv2_check == False:
		raise Exception("EchoCV2CheckResult accepts True or False")

	echo_3dcheck = isinstance(EchoThreeDSecureAuthenticationCheckResult, bool)
	if echo_3dcheck == False:
		raise Exception(
			"EchoThreeDSecureAuthenticationCheckResult accepts True or False")

	echo_card_type_check = isinstance(EchoCardType, bool)
	if echo_card_type_check == False:
		raise Exception("EchoCardType accepts True or False")

	if AVSOverridePolicy == None:
		# do nothing, variable not required
		pass
	else:
		# variable has been passed, needs validation
		if len(AVSOverridePolicy) > 4:
			raise Exception(
				"AVSOverridePolicy must be no more than 4 characters")

	if CV2OverridePolicy == None:
		# do nothing, variable not required
		pass
	else:
		# variable has been passed, needs validation
		if len(CV2OverridePolicy) > 2:
			raise Exception(
				"AVSOverridePolicy must be no more than 2 characters")

	if ThreeDSecureOverridePolicy == None:
		# do nothing, variable not required
		pass
	else:
		# variable has been passed, needs validation
		threeds_or_check = isinstance(ThreeDSecureOverridePolicy, bool)
		if threeds_or_check == False:
			raise Exception(
				"ThreeDSecureOverridePolicy accepts True or False")

	if len(OrderID) > 50:
		raise Exception("OrderID must be no more than 15 characters")
	

	if TransactionType == "SALE" or "PREAUTH":
		pass
	else:
		raise Exception("TransactionType accepts 'SALE' or 'PREAUTH'")	

	# CallbackURL doesn't really need any validation

	if OrderDescription == None:
		# do nothing, variable not required
		pass
	elif len(OrderDescription) > 256:
		raise Exception(
			"OrderDescription must be no more than 256 characters")

	if CustomerName == None:
		# do nothing, variable not required
		pass
	elif len(CustomerName) > 100:
		raise Exception(
			"CustomerName must be no more than 100 characters")

	if Address1 == None:
		# do nothing, variable not required
		pass
	elif len(Address1) > 100:
		raise Exception(
			"Address1 must be no more than 100 characters")

	if Address2 == None:
		# do nothing, variable not required
		pass
	elif len(Address2) > 50:
		raise Exception(
			"Address1 must be no more than 50 characters")

	if Address3 == None:
		# do nothing, variable not required
		pass
	elif len(Address3) > 50:
		raise Exception(
			"Address3 must be no more than 50 characters")

	if Address4 == None:
		# do nothing, variable not required
		pass
	elif len(Address4) > 50:
		raise Exception(
			"Address4 must be no more than 50 characters")

	if City == None:
		# do nothing, variable not required
		pass
	elif len(City) > 50:
		raise Exception(
			"City must be no more than 50 characters")

	if State == None:
		# do nothing, variable not required
		pass
	elif len(State) > 50:
		raise Exception(
			"State must be no more than 50 characters")

	if PostCode == None:
		# do nothing, variable not required
		pass
	elif len(PostCode) > 50:
		raise Exception(
			"PostCode must be no more than 50 characters")

	if CountryCode == None:
		# do nothing, variable not required
		pass
	elif len(CountryCode) > 3:
		raise Exception(
			"CountryCode must be no more than 50 characters")
	else:
		cc_test = is_number(CountryCode)
		if cc_test == False:
			raise Exception("CountryCode need to be a numerical value")


	if EmailAddress == None:
		# do nothing, variable not required
		pass
	elif len(EmailAddress) > 100:
		raise Exception(
			"EmailAddress must be no more than 100 characters")
	else:
		email_test = re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b',
					 order.email)
		# if email is invalid, send to luke and he can investigate
		if email_test == None:
			raise Exception("EmailAddress is an invalid format")


	if PhoneNumber == None:
		# do nothing, variable not required
		pass
	elif len(PhoneNumber) > 30:
		raise Exception(
			"PostCode must be no more than 30 characters")


	email_edit_check = isinstance(EmailAddressEditable, bool)
	if email_edit_check == False:
		raise Exception("EmailAddressEditable accepts True or False")

	phone_edit_check = isinstance(PhoneNumberEditable, bool)
	if phone_edit_check == False:
		raise Exception("PhoneNumberEditable accepts True or False")


	cv2_man_check = isinstance(CV2Mandatory, bool)
	if cv2_man_check == False:
		raise Exception("CV2Mandatory accepts True or False")

	addr1_man_check = isinstance(Address1Mandatory, bool)
	if addr1_man_check == False:
		raise Exception("Address1Mandatory accepts True or False")

	city_man_check = isinstance(CityMandatory, bool)
	if city_man_check == False:
		raise Exception("CityMandatory accepts True or False")

	postc_man_check = isinstance(PostCodeMandatory, bool)
	if postc_man_check == False:
		raise Exception("PostCodeMandatory accepts True or False")

	state_man_check = isinstance(StateMandatory, bool)
	if state_man_check == False:
		raise Exception("StateMandatory accepts True or False")

	country_man_check = isinstance(CountryMandatory, bool)
	if country_man_check == False:
		raise Exception("CountryMandatory accepts True or False")

	if ResultDeliveryMethod == "POST" or "SERVER" or "SERVER_PULL":
		pass
	else:
		raise Exception(
			"ResultDeliveryMethod accepts 'POST', 'SERVER' or 'SERVER_PULL'")

	# ServerResultURL requires no validation

	pay_form_check = isinstance(PaymentFormDisplaysResult, bool)
	if pay_form_check == False:
		raise Exception("PaymentFormDisplaysResult accepts True or False")

	prehash_skeleton = """PreSharedKey={PreSharedKey}&MerchantID={MerchantID}&Password={Password}&Amount={Amount}&CurrencyCode={CurrencyCode}&EchoAVSCheckResult={EchoAVSCheckResult}&EchoCV2CheckResult={EchoCV2CheckResult}&EchoThreeDSecureAuthenticationCheckResult={EchoThreeDSecureAuthenticationCheckResult}&EchoCardType={EchoCardType}&AVSOverridePolicy={AVSOverridePolicy}&CV2OverridePolicy={CV2OverridePolicy}&ThreeDSecureOverridePolicy={ThreeDSecureOverridePolicy}&OrderID={OrderID}&TransactionType={TransactionType}&TransactionDateTime={TransactionDateTime}&CallbackURL={CallbackURL}&OrderDescription={OrderDescription}&CustomerName={CustomerName}&Address1={Address1}&Address2={Address2}&Address3={Address3}&Address4={Address4}&City={City}&State={State}&PostCode={PostCode}&CountryCode={CountryCode}&EmailAddress={EmailAddress}&PhoneNumber={PhoneNumber}&EmailAddressEditable={EmailAddressEditable}&PhoneNumberEditable={PhoneNumberEditable}&CV2Mandatory={CV2Mandatory}&Address1Mandatory={Address1Mandatory}&CityMandatory={CityMandatory}&PostCodeMandatory={PostCodeMandatory}&StateMandatory={StateMandatory}&CountryMandatory={CountryMandatory}&ResultDeliveryMethod={ResultDeliveryMethod}&ServerResultURL={ServerResultURL}&PaymentFormDisplaysResult={PaymentFormDisplaysResult}"""

	prehash = prehash_skeleton.format(
		PreSharedKey=PreSharedKey,
		MerchantID=MerchantID,
		Password=Password,
		Amount=Amount,
		CurrencyCode=CurrencyCode,
		EchoAVSCheckResult=EchoAVSCheckResult,
		EchoCV2CheckResult=EchoCV2CheckResult,
		EchoThreeDSecureAuthenticationCheckResult=
			EchoThreeDSecureAuthenticationCheckResult,
		EchoCardType=EchoCardType,
		AVSOverridePolicy=AVSOverridePolicy,
		CV2OverridePolicy=CV2OverridePolicy,
		ThreeDSecureOverridePolicy=ThreeDSecureOverridePolicy,
		OrderID=OrderID,
		TransactionType=TransactionType,
		TransactionDateTime=TransactionDateTime,
		CallbackURL=CallbackURL,
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
		EmailAddressEditable=EmailAddressEditable,
		PhoneNumberEditable=PhoneNumberEditable,
		CV2Mandatory=CV2Mandatory,
		Address1Mandatory=Address1Mandatory,
		CityMandatory=CityMandatory,
		PostCodeMandatory=PostCodeMandatory,
		StateMandatory=StateMandatory,
		CountryMandatory=CountryMandatory,
		ResultDeliveryMethod=ResultDeliveryMethod,
		ServerResultURL=ServerResultURL,
		PaymentFormDisplaysResult=PaymentFormDisplaysResult
		)
	
	prehash_remove_none = prehash.replace("None","")
	# Replace None with empty string, then remove any \n instances
	prehash_clean = prehash_remove_none.replace("\n","")
	#prehash_clean = prehash_remove_none.replace(" ","")
	print prehash_clean
	# lastly generate the sha1 string to pass to the URL
	sha1_string = hashlib.sha1(prehash_clean).hexdigest()

	# return sha1 hash of all values
	return sha1_string
