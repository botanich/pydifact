# -*- coding: utf-8 -*-

_composite_structure = {
    "D96A": {
        "C002": [  # DOCUMENT/MESSAGE NAME
            ("1001", "C"),  # Document/message name, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("1000", "C"),  # Document/message name
        ],
        "C040": [  # CARRIER
            ("3127", "C"),  # Carrier identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3128", "C"),  # Carrier name
        ],
        "C042": [  # NATIONALITY DETAILS
            ("3293", "C"),  # Nationality, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3292", "C"),  # Nationality
        ],
        "C045": [  # BILL LEVEL IDENTIFICATION
            ("7436", "C"),  # Level one id.
            ("7438", "C"),  # Level two id.
            ("7440", "C"),  # Level three id.
            ("7442", "C"),  # Level four id.
            ("7444", "C"),  # Level five id.
            ("7446", "C"),  # Level six id.
        ],
        "C049": [  # REMUNERATION TYPE IDENTIFICATION
            ("5315", "C"),  # Remuneration type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("5314", "C"),  # Remuneration type
            ("5314", "C"),  # Remuneration type
        ],
        "C056": [  # DEPARTMENT OR EMPLOYEE DETAILS
            ("3413", "C"),  # Department or employee identification
            ("3412", "C"),  # Department or employee
        ],
        "C058": [  # NAME AND ADDRESS
            ("3124", "M"),  # Name and address line
            ("3124", "C"),  # Name and address line
            ("3124", "C"),  # Name and address line
            ("3124", "C"),  # Name and address line
            ("3124", "C"),  # Name and address line
        ],
        "C059": [  # STREET
            ("3042", "M"),  # Street and number/p.o. box
            ("3042", "C"),  # Street and number/p.o. box
            ("3042", "C"),  # Street and number/p.o. box
            ("3042", "C"),  # Street and number/p.o. box
        ],
        "C076": [  # COMMUNICATION CONTACT
            ("3148", "M"),  # Communication number
            ("3155", "M"),  # Communication channel qualifier
        ],
        "C077": [  # FILE IDENTIFICATION
            ("1508", "C"),  # File name
            ("7008", "C"),  # Item description
        ],
        "C078": [  # ACCOUNT IDENTIFICATION
            ("3194", "C"),  # Account holder number
            ("3192", "C"),  # Account holder name
            ("3192", "C"),  # Account holder name
            ("6345", "C"),  # Currency, coded
        ],
        "C079": [  # COMPUTER ENVIRONMENT IDENTIFICATION
            ("1511", "C"),  # Computer environment, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("1510", "C"),  # Computer environment
            ("1056", "C"),  # Version
            ("1058", "C"),  # Release
            ("7402", "C"),  # Identity number
        ],
        "C080": [  # PARTY NAME
            ("3036", "M"),  # Party name
            ("3036", "C"),  # Party name
            ("3036", "C"),  # Party name
            ("3036", "C"),  # Party name
            ("3036", "C"),  # Party name
            ("3045", "C"),  # Party name format, coded
        ],
        "C082": [  # PARTY IDENTIFICATION DETAILS
            ("3039", "M"),  # Party id. identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C085": [  # MARITAL STATUS DETAILS
            ("3479", "C"),  # Marital status, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3478", "C"),  # Marital status
        ],
        "C088": [  # INSTITUTION IDENTIFICATION
            ("3433", "C"),  # Institution name identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3434", "C"),  # Institution branch number
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3432", "C"),  # Institution name
            ("3436", "C"),  # Institution branch place
        ],
        "C090": [  # ADDRESS DETAILS
            ("3477", "M"),  # Address format, coded
            ("3286", "M"),  # Address component
            ("3286", "C"),  # Address component
            ("3286", "C"),  # Address component
            ("3286", "C"),  # Address component
            ("3286", "C"),  # Address component
        ],
        "C099": [  # FILE DETAILS
            ("1516", "M"),  # File format
            ("1056", "C"),  # Version
            ("1503", "C"),  # Data format, coded
            ("1502", "C"),  # Data format
        ],
        "C100": [  # TERMS OF DELIVERY OR TRANSPORT
            ("4053", "C"),  # Terms of delivery or transport, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4052", "C"),  # Terms of delivery or transport
            ("4052", "C"),  # Terms of delivery or transport
        ],
        "C101": [  # RELIGION DETAILS
            ("3483", "C"),  # Religion, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3482", "C"),  # Religion
        ],
        "C107": [  # TEXT REFERENCE
            ("4441", "M"),  # Free text, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C108": [  # TEXT LITERAL
            ("4440", "M"),  # Free text
            ("4440", "C"),  # Free text
            ("4440", "C"),  # Free text
            ("4440", "C"),  # Free text
            ("4440", "C"),  # Free text
        ],
        "C110": [  # PAYMENT TERMS
            ("4277", "M"),  # Terms of payment identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4276", "C"),  # Terms of payment
            ("4276", "C"),  # Terms of payment
        ],
        "C112": [  # TERMS/TIME INFORMATION
            ("2475", "M"),  # Payment time reference, coded
            ("2009", "C"),  # Time relation, coded
            ("2151", "C"),  # Type of period, coded
            ("2152", "C"),  # Number of periods
        ],
        "C128": [  # RATE DETAILS
            ("5419", "M"),  # Rate type qualifier
            ("5420", "M"),  # Rate per unit
            ("5284", "C"),  # Unit price basis
            ("6411", "C"),  # Measure unit qualifier
        ],
        "C138": [  # PRICE MULTIPLIER INFORMATION
            ("5394", "M"),  # Price multiplier
            ("5393", "C"),  # Price multiplier qualifier
        ],
        "C174": [  # VALUE/RANGE
            ("6411", "M"),  # Measure unit qualifier
            ("6314", "C"),  # Measurement value
            ("6162", "C"),  # Range minimum
            ("6152", "C"),  # Range maximum
            ("6432", "C"),  # Significant digits
        ],
        "C186": [  # QUANTITY DETAILS
            ("6063", "M"),  # Quantity qualifier
            ("6060", "M"),  # Quantity
            ("6411", "C"),  # Measure unit qualifier
        ],
        "C200": [  # CHARGE
            ("8023", "C"),  # Freight and charges identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("8022", "C"),  # Freight and charges
            ("4237", "C"),  # Prepaid/collect indicator, coded
            ("7140", "C"),  # Item number
        ],
        "C202": [  # PACKAGE TYPE
            ("7065", "C"),  # Type of packages identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7064", "C"),  # Type of packages
        ],
        "C203": [  # RATE/TARIFF CLASS
            ("5243", "M"),  # Rate/tariff class identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("5242", "C"),  # Rate/tariff class
            ("5275", "C"),  # Supplementary rate/tariff basis identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("5275", "C"),  # Supplementary rate/tariff basis identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C205": [  # HAZARD CODE
            ("8351", "M"),  # Hazard code identification
            ("8078", "C"),  # Hazard substance/item/page number
            ("8092", "C"),  # Hazard code version number
        ],
        "C206": [  # IDENTIFICATION NUMBER
            ("7402", "M"),  # Identity number
            ("7405", "C"),  # Identity number qualifier
            ("4405", "C"),  # Status, coded
        ],
        "C208": [  # IDENTITY NUMBER RANGE
            ("7402", "M"),  # Identity number
            ("7402", "C"),  # Identity number
        ],
        "C210": [  # MARKS & LABELS
            ("7102", "M"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
            ("7102", "C"),  # Shipping marks
        ],
        "C211": [  # DIMENSIONS
            ("6411", "M"),  # Measure unit qualifier
            ("6168", "C"),  # Length dimension
            ("6140", "C"),  # Width dimension
            ("6008", "C"),  # Height dimension
        ],
        "C212": [  # ITEM NUMBER IDENTIFICATION
            ("7140", "C"),  # Item number
            ("7143", "C"),  # Item number type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C213": [  # NUMBER AND TYPE OF PACKAGES
            ("7224", "C"),  # Number of packages
            ("7065", "C"),  # Type of packages identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7064", "C"),  # Type of packages
        ],
        "C214": [  # SPECIAL SERVICES IDENTIFICATION
            ("7161", "C"),  # Special services, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7160", "C"),  # Special service
            ("7160", "C"),  # Special service
        ],
        "C215": [  # SEAL ISSUER
            ("9303", "C"),  # Sealing party, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9302", "C"),  # Sealing party
        ],
        "C218": [  # HAZARDOUS MATERIAL
            ("7419", "C"),  # Hazardous material class code, identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C219": [  # MOVEMENT TYPE
            ("8335", "C"),  # Movement type, coded
            ("8334", "C"),  # Movement type
        ],
        "C220": [  # MODE OF TRANSPORT
            ("8067", "C"),  # Mode of transport, coded
            ("8066", "C"),  # Mode of transport
        ],
        "C222": [  # TRANSPORT IDENTIFICATION
            ("8213", "C"),  # Id. of means of transport identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("8212", "C"),  # Id. of the means of transport
            ("8453", "C"),  # Nationality of means of transport, coded
        ],
        "C223": [  # DANGEROUS GOODS SHIPMENT FLASHPOINT
            ("7106", "C"),  # Shipment flashpoint
            ("6411", "C"),  # Measure unit qualifier
        ],
        "C224": [  # EQUIPMENT SIZE AND TYPE
            ("8155", "C"),  # Equipment size and type identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("8154", "C"),  # Equipment size and type
        ],
        "C228": [  # TRANSPORT MEANS
            ("8179", "C"),  # Type of means of transport identification
            ("8178", "C"),  # Type of means of transport
        ],
        "C229": [  # CHARGE CATEGORY
            ("5237", "M"),  # Charge category, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C231": [  # METHOD OF PAYMENT
            ("4215", "M"),  # Transport charges method of payment, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C232": [  # GOVERNMENT ACTION
            ("9415", "C"),  # Government agency, coded
            ("9411", "C"),  # Government involvement, coded
            ("9417", "C"),  # Government action, coded
            ("9353", "C"),  # Government procedure, coded
        ],
        "C233": [  # SERVICE
            ("7273", "M"),  # Service requirement, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7273", "C"),  # Service requirement, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C234": [  # UNDG INFORMATION
            ("7124", "C"),  # UNDG number
            ("7088", "C"),  # Dangerous goods flashpoint
        ],
        "C235": [  # HAZARD IDENTIFICATION
            ("8158", "C"),  # Hazard identification number, upper part
            ("8186", "C"),  # Substance identification number, lower part
        ],
        "C236": [  # DANGEROUS GOODS LABEL
            ("8246", "C"),  # Dangerous goods label marking
            ("8246", "C"),  # Dangerous goods label marking
            ("8246", "C"),  # Dangerous goods label marking
        ],
        "C237": [  # EQUIPMENT IDENTIFICATION
            ("8260", "C"),  # Equipment identification number
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3207", "C"),  # Country, coded
        ],
        "C239": [  # TEMPERATURE SETTING
            ("6246", "C"),  # Temperature setting
            ("6411", "C"),  # Measure unit qualifier
        ],
        "C240": [  # PRODUCT CHARACTERISTIC
            ("7037", "M"),  # Characteristic identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7036", "C"),  # Characteristic
            ("7036", "C"),  # Characteristic
        ],
        "C241": [  # DUTY/TAX/FEE TYPE
            ("5153", "C"),  # Duty/tax/fee type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("5152", "C"),  # Duty/tax/fee type
        ],
        "C242": [  # PROCESS TYPE AND DESCRIPTION
            ("7187", "M"),  # Process type identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7186", "C"),  # Process type
            ("7186", "C"),  # Process type
        ],
        "C243": [  # DUTY/TAX/FEE DETAIL
            ("5279", "C"),  # Duty/tax/fee rate identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("5278", "C"),  # Duty/tax/fee rate
            ("5273", "C"),  # Duty/tax/fee rate basis identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C244": [  # TEST METHOD
            ("4415", "C"),  # Test method identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4416", "C"),  # Test description
        ],
        "C246": [  # CUSTOMS IDENTITY CODES
            ("7361", "M"),  # Customs code identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C270": [  # CONTROL
            ("6069", "M"),  # Control qualifier
            ("6066", "M"),  # Control value
            ("6411", "C"),  # Measure unit qualifier
        ],
        "C273": [  # ITEM DESCRIPTION
            ("7009", "C"),  # Item description identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7008", "C"),  # Item description
            ("7008", "C"),  # Item description
            ("3453", "C"),  # Language, coded
        ],
        "C279": [  # QUANTITY DIFFERENCE INFORMATION
            ("6064", "M"),  # Quantity difference
            ("6063", "C"),  # Quantity qualifier
        ],
        "C280": [  # RANGE
            ("6411", "M"),  # Measure unit qualifier
            ("6162", "C"),  # Range minimum
            ("6152", "C"),  # Range maximum
        ],
        "C286": [  # SEQUENCE INFORMATION
            ("1050", "M"),  # Sequence number
            ("1159", "C"),  # Sequence number source, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C288": [  # PRODUCT GROUP
            ("5389", "C"),  # Product group, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("5388", "C"),  # Product group
        ],
        "C292": [  # PRICE CHANGE INFORMATION
            ("5377", "M"),  # Price change indicator, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C329": [  # PATTERN DESCRIPTION
            ("2013", "C"),  # Frequency, coded
            ("2015", "C"),  # Despatch pattern, coded
            ("2017", "C"),  # Despatch pattern timing, coded
        ],
        "C330": [  # INSURANCE COVER TYPE
            ("4497", "M"),  # Insurance cover type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C331": [  # INSURANCE COVER DETAILS
            ("4495", "C"),  # Insurance cover identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4494", "C"),  # Insurance cover
            ("4494", "C"),  # Insurance cover
        ],
        "C332": [  # SALES CHANNEL IDENTIFICATION
            ("3496", "M"),  # Sales channel identifier
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C333": [  # INFORMATION REQUEST
            ("4511", "C"),  # Requested information, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4510", "C"),  # Requested information
        ],
        "C401": [  # EXCESS TRANSPORTATION INFORMATION
            ("8457", "M"),  # Excess transportation reason, coded
            ("8459", "M"),  # Excess transportation responsibility, coded
            ("7130", "C"),  # Customer authorization number
        ],
        "C402": [  # PACKAGE TYPE IDENTIFICATION
            ("7077", "M"),  # Item description type, coded
            ("7064", "M"),  # Type of packages
            ("7143", "C"),  # Item number type, coded
            ("7064", "C"),  # Type of packages
            ("7143", "C"),  # Item number type, coded
        ],
        "C501": [  # PERCENTAGE DETAILS
            ("5245", "M"),  # Percentage qualifier
            ("5482", "C"),  # Percentage
            ("5249", "C"),  # Percentage basis, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C502": [  # MEASUREMENT DETAILS
            ("6313", "C"),  # Measurement dimension, coded
            ("6321", "C"),  # Measurement significance, coded
            ("6155", "C"),  # Measurement attribute, coded
            ("6154", "C"),  # Measurement attribute
        ],
        "C503": [  # DOCUMENT/MESSAGE DETAILS
            ("1004", "C"),  # Document/message number
            ("1373", "C"),  # Document/message status, coded
            ("1366", "C"),  # Document/message source
            ("3453", "C"),  # Language, coded
        ],
        "C504": [  # CURRENCY DETAILS
            ("6347", "M"),  # Currency details qualifier
            ("6345", "C"),  # Currency, coded
            ("6343", "C"),  # Currency qualifier
            ("6348", "C"),  # Currency rate base
        ],
        "C506": [  # REFERENCE
            ("1153", "M"),  # Reference qualifier
            ("1154", "C"),  # Reference number
            ("1156", "C"),  # Line number
            ("4000", "C"),  # Reference version number
        ],
        "C507": [  # DATE/TIME/PERIOD
            ("2005", "M"),  # Date/time/period qualifier
            ("2380", "C"),  # Date/time/period
            ("2379", "C"),  # Date/time/period format qualifier
        ],
        "C508": [  # LANGUAGE DETAILS
            ("3453", "C"),  # Language, coded
            ("3452", "C"),  # Language
        ],
        "C509": [  # PRICE INFORMATION
            ("5125", "M"),  # Price qualifier
            ("5118", "C"),  # Price
            ("5375", "C"),  # Price type, coded
            ("5387", "C"),  # Price type qualifier
            ("5284", "C"),  # Unit price basis
            ("6411", "C"),  # Measure unit qualifier
        ],
        "C512": [  # SIZE DETAILS
            ("6173", "C"),  # Size qualifier
            ("6174", "C"),  # Size
        ],
        "C514": [  # SAMPLE LOCATION DETAILS
            ("3237", "C"),  # Sample location, coded
            ("3236", "C"),  # Sample location
        ],
        "C515": [  # TEST REASON
            ("4425", "C"),  # Test reason identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4424", "C"),  # Test reason
        ],
        "C516": [  # MONETARY AMOUNT
            ("5025", "M"),  # Monetary amount type qualifier
            ("5004", "C"),  # Monetary amount
            ("6345", "C"),  # Currency, coded
            ("6343", "C"),  # Currency qualifier
            ("4405", "C"),  # Status, coded
        ],
        "C517": [  # LOCATION IDENTIFICATION
            ("3225", "C"),  # Place/location identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3224", "C"),  # Place/location
        ],
        "C519": [  # RELATED LOCATION ONE IDENTIFICATION
            ("3223", "C"),  # Related place/location one identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3222", "C"),  # Related place/location one
        ],
        "C521": [  # BUSINESS FUNCTION
            ("4027", "M"),  # Business function qualifier
            ("4025", "M"),  # Business function, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4022", "C"),  # Business description
        ],
        "C522": [  # INSTRUCTION
            ("4403", "M"),  # Instruction qualifier
            ("4401", "C"),  # Instruction, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4400", "C"),  # Instruction
        ],
        "C523": [  # NUMBER OF UNIT DETAILS
            ("6350", "C"),  # Number of units
            ("6353", "C"),  # Number of units qualifier
        ],
        "C524": [  # HANDLING INSTRUCTIONS
            ("4079", "C"),  # Handling instructions, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4078", "C"),  # Handling instructions
        ],
        "C526": [  # FREQUENCY DETAILS
            ("6071", "M"),  # Frequency qualifier
            ("6072", "C"),  # Frequency value
            ("6411", "C"),  # Measure unit qualifier
        ],
        "C527": [  # STATISTICAL DETAILS
            ("6314", "C"),  # Measurement value
            ("6411", "C"),  # Measure unit qualifier
            ("6313", "C"),  # Measurement dimension, coded
            ("6321", "C"),  # Measurement significance, coded
        ],
        "C528": [  # COMMODITY/RATE DETAIL
            ("7357", "C"),  # Commodity/rate identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C529": [  # PROCESSING INDICATOR
            ("7365", "M"),  # Processing indicator, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7187", "C"),  # Process type identification
        ],
        "C531": [  # PACKAGING DETAILS
            ("7075", "C"),  # Packaging level, coded
            ("7233", "C"),  # Packaging related information, coded
            ("7073", "C"),  # Packaging terms and conditions, coded
        ],
        "C532": [  # RETURNABLE PACKAGE DETAILS
            ("8395", "C"),  # Returnable package freight payment responsibility, coded
            ("8393", "C"),  # Returnable package load contents, coded
        ],
        "C533": [  # DUTY/TAX/FEE ACCOUNT DETAIL
            ("5289", "M"),  # Duty/tax/fee account identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C534": [  # PAYMENT INSTRUCTION DETAILS
            ("4439", "C"),  # Payment conditions, coded
            ("4431", "C"),  # Payment guarantee, coded
            ("4461", "C"),  # Payment means, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4435", "C"),  # Payment channel, coded
        ],
        "C536": [  # CONTRACT AND CARRIAGE CONDITION
            ("4065", "M"),  # Contract and carriage condition, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C537": [  # TRANSPORT PRIORITY
            ("4219", "M"),  # Transport priority, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C543": [  # AGREEMENT TYPE IDENTIFICATION
            ("7431", "M"),  # Agreement type qualifier
            ("7433", "C"),  # Agreement type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7434", "C"),  # Agreement type description
        ],
        "C545": [  # INDEX IDENTIFICATION
            ("5013", "M"),  # Index qualifier
            ("5027", "C"),  # Index type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C546": [  # INDEX VALUE
            ("5030", "M"),  # Index value
            ("5039", "C"),  # Index value representation, coded
        ],
        "C549": [  # MONETARY FUNCTION
            ("5007", "M"),  # Monetary function, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C550": [  # REQUIREMENT/CONDITION IDENTIFICATION
            ("7295", "M"),  # Requirement/condition identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7294", "C"),  # Requirement or condition
        ],
        "C551": [  # BANK OPERATION
            ("4383", "M"),  # Bank operation, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C552": [  # ALLOWANCE/CHARGE INFORMATION
            ("1230", "C"),  # Allowance or charge number
            ("5189", "C"),  # Charge/allowance description, coded
        ],
        "C553": [  # RELATED LOCATION TWO IDENTIFICATION
            ("3233", "C"),  # Related place/location two identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3232", "C"),  # Related place/location two
        ],
        "C554": [  # RATE/TARIFF CLASS DETAIL
            ("5243", "C"),  # Rate/tariff class identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C555": [  # STATUS EVENT
            ("9011", "M"),  # Status event, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9010", "C"),  # Status event
        ],
        "C556": [  # STATUS REASON
            ("9013", "M"),  # Status reason, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9012", "C"),  # Status reason
        ],
        "C564": [  # PHYSICAL OR LOGICAL STATE INFORMATION
            ("7007", "C"),  # Physical or logical state, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7006", "C"),  # Physical or logical state
        ],
        "C585": [  # PRIORITY DETAILS
            ("4037", "C"),  # Priority, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4036", "C"),  # Priority
        ],
        "C601": [  # STATUS TYPE
            ("9015", "M"),  # Status type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C701": [  # ERROR POINT DETAILS
            ("1049", "M"),  # Message section, coded
            ("1052", "C"),  # Message item number
            ("1054", "C"),  # Message sub-item number
        ],
        "C702": [  # CODE SET IDENTIFICATION
            ("9150", "C"),  # Simple data element tag
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C703": [  # NATURE OF CARGO
            ("7085", "M"),  # Nature of cargo, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C709": [  # MESSAGE IDENTIFIER
            ("1475", "M"),  # Message type identifier
            ("1056", "M"),  # Version
            ("1058", "M"),  # Release
            ("1476", "M"),  # Control agency
            ("1523", "C"),  # Association assigned identification
            ("1060", "C"),  # Revision number
        ],
        "C770": [  # ARRAY CELL DETAILS
            ("9424", "C"),  # Array cell information
        ],
        "C778": [  # POSITION IDENTIFICATION
            ("7164", "C"),  # Hierarchical id. number
            ("1050", "C"),  # Sequence number
        ],
        "C779": [  # ARRAY STRUCTURE IDENTIFICATION
            ("9428", "M"),  # Array structure identifier
            ("7405", "C"),  # Identity number qualifier
        ],
        "C780": [  # VALUE LIST IDENTIFICATION
            ("1518", "M"),  # Value list identifier
            ("7405", "C"),  # Identity number qualifier
        ],
        "C782": [  # DATA SET IDENTIFICATION
            ("1520", "M"),  # Data set identifier
            ("7405", "C"),  # Identity number qualifier
        ],
        "C783": [  # FOOTNOTE SET IDENTIFICATION
            ("9430", "M"),  # Footnote set identifier
            ("7405", "C"),  # Identity number qualifier
        ],
        "C784": [  # FOOTNOTE IDENTIFICATION
            ("9432", "M"),  # Footnote identifier
            ("7405", "C"),  # Identity number qualifier
        ],
        "C785": [  # STATISTICAL CONCEPT IDENTIFICATION
            ("6434", "M"),  # Statistical concept identifier
            ("7405", "C"),  # Identity number qualifier
        ],
        "C786": [  # STRUCTURE COMPONENT IDENTIFICATION
            ("7512", "M"),  # Structure component identifier
            ("7405", "C"),  # Identity number qualifier
        ],
        "C814": [  # SAFETY SECTION
            ("4046", "M"),  # Safety section
            ("4044", "C"),  # Safety section name
        ],
        "C815": [  # ADDITIONAL SAFETY INFORMATION
            ("4039", "M"),  # Additional safety information, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4038", "C"),  # Additional safety information
        ],
        "C816": [  # NAME COMPONENT DETAILS
            ("3405", "M"),  # Name component qualifier
            ("3398", "C"),  # Name component
            ("3401", "C"),  # Name component status, coded
            ("3295", "C"),  # Name component original representation, coded
        ],
        "C817": [  # ADDRESS USAGE
            ("3299", "C"),  # Address purpose, coded
            ("3131", "C"),  # Address type, coded
            ("3475", "C"),  # Address status, coded
        ],
        "C818": [  # PERSON INHERITED CHARACTERISTIC DETAILS
            ("3311", "C"),  # Person inherited characteristic identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3310", "C"),  # Person inherited characteristic
        ],
        "C819": [  # COUNTRY SUB-ENTITY DETAILS
            ("3229", "C"),  # Country sub-entity identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3228", "C"),  # Country sub-entity
        ],
        "C821": [  # TYPE OF DAMAGE
            ("7501", "C"),  # Type of damage, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7500", "C"),  # Type of damage
        ],
        "C822": [  # DAMAGE AREA
            ("7503", "C"),  # Damage area identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7502", "C"),  # Damage area
        ],
        "C823": [  # TYPE OF UNIT/COMPONENT
            ("7505", "C"),  # Type of unit/component, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7504", "C"),  # Type of unit/component
        ],
        "C824": [  # COMPONENT MATERIAL
            ("7507", "C"),  # Component material, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7506", "C"),  # Component material
        ],
        "C825": [  # DAMAGE SEVERITY
            ("7509", "C"),  # Damage severity, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7508", "C"),  # Damage severity
        ],
        "C826": [  # ACTION
            ("1229", "C"),  # Action request/notification, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("1228", "C"),  # Action request/notification
        ],
        "C827": [  # TYPE OF MARKING
            ("7511", "M"),  # Type of marking, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C829": [  # SUB-LINE INFORMATION
            ("5495", "C"),  # Sub-line indicator, coded
            ("1082", "C"),  # Line item number
        ],
        "C849": [  # PARTIES TO INSTRUCTION
            ("3301", "M"),  # Party enacting instruction identification
            ("3285", "C"),  # Recipient of the instruction identification
        ],
        "C850": [  # STATUS OF INSTRUCTION
            ("4405", "M"),  # Status, coded
            ("3036", "C"),  # Party name
        ],
        "C878": [  # CHARGE/ALLOWANCE ACCOUNT
            ("3434", "M"),  # Institution branch number
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("3194", "C"),  # Account holder number
            ("6345", "C"),  # Currency, coded
        ],
        "C889": [  # CHARACTERISTIC VALUE
            ("7111", "C"),  # Characteristic value, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7110", "C"),  # Characteristic value
            ("7110", "C"),  # Characteristic value
        ],
        "C901": [  # APPLICATION ERROR DETAIL
            ("9321", "M"),  # Application error identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C941": [  # RELATIONSHIP
            ("9143", "C"),  # Relationship, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9142", "C"),  # Relationship
        ],
        "C942": [  # MEMBERSHIP CATEGORY
            ("7451", "M"),  # Membership category identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7450", "C"),  # Membership category
        ],
        "C944": [  # MEMBERSHIP STATUS
            ("7453", "C"),  # Membership status, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7452", "C"),  # Membership status
        ],
        "C945": [  # MEMBERSHIP LEVEL
            ("7455", "M"),  # Membership level qualifier
            ("7457", "C"),  # Membership level identification
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("7456", "C"),  # Membership level
        ],
        "C948": [  # EMPLOYMENT CATEGORY
            ("9005", "C"),  # Employment category, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9004", "C"),  # Employment category
        ],
        "C950": [  # QUALIFICATION CLASSIFICATION
            ("9007", "C"),  # Qualification classification, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9006", "C"),  # Qualification classification
            ("9006", "C"),  # Qualification classification
        ],
        "C951": [  # OCCUPATION
            ("9009", "C"),  # Occupation, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9008", "C"),  # Occupation
            ("9008", "C"),  # Occupation
        ],
        "C953": [  # CONTRIBUTION TYPE
            ("5049", "M"),  # Contribution type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("5048", "C"),  # Contribution type
        ],
        "C955": [  # ATTRIBUTE TYPE
            ("9021", "M"),  # Attribute type, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
        ],
        "C956": [  # ATTRIBUTE DETAILS
            ("9019", "C"),  # Attribute, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("9018", "C"),  # Attribute
        ],
        "C960": [  # REASON FOR CHANGE
            ("4295", "C"),  # Change reason, coded
            ("1131", "C"),  # Code list qualifier
            ("3055", "C"),  # Code list responsible agency, coded
            ("4294", "C"),  # Change reason
        ],
    }
}
