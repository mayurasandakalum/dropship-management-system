from tkinter import *
from tkinter import ttk
from datetime import date
from PIL import ImageTk,Image

from pynput.keyboard import Key, Controller
keyboard = Controller()

# Import manually created classes
from ClassCurrencyCheckbutton import *
from classes8 import *

# Set Up root of app
root = Tk()
root.geometry("1000x592")
#root.overrideredirect(True)
#root.iconbitmap('on.png')
root.title("Fixed Orders")
#root.wm_attributes('-type', 'splash')

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "GUI Icon Checking\dark.tcl")

# Set the theme with the theme_use method
style.theme_use("azure-dark")


# Output canvas frame
canvas_output_frame = Frame(root, bg='#1f1f1f')
canvas_output_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

# Create a frame to put the VerticalScrolledFrame inside
holder_frame = Frame(root)
holder_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

# Create the VerticalScrolledFrame
vs_frame = VerticalScrolledFrame(holder_frame)
vs_frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)


#####Create main frame
main_frame = Frame(vs_frame.interior, bg='#1f1f1f')
main_frame.pack(side=LEFT)

##### Create eBay title
"""ebay_title_label = Label(main_frame, text="eBay Details", font = "Arial 15 bold")
ebay_title_label.grid(row=1, column=1, pady=(15,10), padx=10, sticky="W")
"""
### Create eBay Sub Frames

ebay_date_details_label_frame = Subframe(main_frame, text='Date Details', row=2, padyUp=25, ipady=2)
ebay_listing_details_label_frame = Subframe(main_frame, text='Listing Details', row=5)
ebay_sold_details_label_frame = Subframe(main_frame, text='Sold Details', row=8, ipady=18)
ebay_buyer_details_label_frame = Subframe(main_frame, text='Buyer Details', row=11)
ebay_shipping_details_label_frame = Subframe(main_frame, text='Shipping Details', row=14)
ebay_tracking_details_label_frame = Subframe(main_frame, text='Tracking Details', row=17)
ali_label_frame = Subframe(main_frame, text='Aliexpress Details', row=21, ipady=20)


###### Create Labels

# eBay Date Detail Labels
ebay_data_added_date_sl_label = label_class(ebay_date_details_label_frame.frame, 1, "Data Added Date")
ebay_sold_date_pdt_label = label_class(ebay_date_details_label_frame.frame, 3, "Item Sold Date")
ebay_paid_date_pdt_label = label_class(ebay_date_details_label_frame.frame, 5, "Paid Date")

# eBay Listing Detail Labels
ebay_listingID_label = label_class(ebay_listing_details_label_frame.frame, 1, "Listing ID")
ebay_lising_title_label = label_class(ebay_listing_details_label_frame.frame, 3, "Title")
ebay_listed_price_label = label_class(ebay_listing_details_label_frame.frame, 5, "Listed Price")

# eBay Sold Detail Labels
ebay_sale_record_number_label = label_class(ebay_sold_details_label_frame.frame, 1, "Sale Record Number")
#ebay_sold_price_without_tax_label = label_class(ebay_sold_details_label_frame.frame, 3, "Sold Price (Without Tax)")

######!

ebay_sold_price_without_tax_label = Label(ebay_sold_details_label_frame.frame, text="Sold Price\n(Without Tax)", font = ("Typo Round Bold Demo", 11), bg='#1f1f1f', fg='#626262')
ebay_sold_price_without_tax_label.grid(row=3, column=1, padx=(40,0), pady=(0,10), sticky="W", columnspan=3)

ebay_shipping_cost_label = Label(ebay_sold_details_label_frame.frame, text="Shipping Cost", font = ("Typo Round Bold Demo", 11), bg='#1f1f1f', fg='#626262')
ebay_shipping_cost_label.place(x=187, y=86)

ebay_tax_amount_label = Label(ebay_sold_details_label_frame.frame, text="Tax Amount", font = ("Typo Round Bold Demo", 11), bg='#1f1f1f', fg='#626262')
ebay_tax_amount_label.place(x=336, y=86)

# eBay Buyer Detail Labels
buyer_id_label = label_class(ebay_buyer_details_label_frame.frame, 1, "Buyer ID")
buyer_email_label = label_class(ebay_buyer_details_label_frame.frame, 3, "E-Mail")
buyer_name_label = label_class(ebay_buyer_details_label_frame.frame, 5, "Name")
buyer_phone_number_label = label_class(ebay_buyer_details_label_frame.frame, 7, "Phone Number")

# eBay Shipping Detail Labels
shipping_name_label = label_class(ebay_shipping_details_label_frame.frame, 1, "Name")
shipping_phone_number_label = label_class(ebay_shipping_details_label_frame.frame, 3, "Phone Number")
shipping_country_label = label_class(ebay_shipping_details_label_frame.frame, 5, "Country")
shipping_state_label = label_class(ebay_shipping_details_label_frame.frame, 5, "State", padx=305)
shipping_city_label = label_class(ebay_shipping_details_label_frame.frame, 7, "City", padx=207)
shipping_zipcode_label = label_class(ebay_shipping_details_label_frame.frame, 7, "Zipcode")
shipping_street_label = label_class(ebay_shipping_details_label_frame.frame, 13, "Street")
shipping_apt_label = label_class(ebay_shipping_details_label_frame.frame, 15, "Apt / Other Details")

# eBay Tracking Detail Labels
tracking_added_date_pdt_label = label_class(ebay_tracking_details_label_frame.frame, 1, "Added Date (PDT)")
tracking_number_label = label_class(ebay_tracking_details_label_frame.frame, 3, "Tracking Number")
shipping_carrier_label = label_class(ebay_tracking_details_label_frame.frame, 5, "Shipping Carrier")
estimated_delivery_date_label = label_class(ebay_tracking_details_label_frame.frame, 7, "Estimated Delivery"+"\n"+"Date")

# Aliexpress Detail Labels
ali_order_date_sl_label = label_class(ali_label_frame.frame, 1, "Order Date")
ali_paid_date_label = label_class(ali_label_frame.frame, 3, "Paid Date")
ali_item_price_label = label_class(ali_label_frame.frame, 5, "Item Price")
ali_shipping_cost_label = label_class(ali_label_frame.frame, 5, "Shipping Cost", padx=255)
ali_tax_charged_label = label_class(ali_label_frame.frame, 7, "Tax Amount")
ali_adjust_price_label = label_class(ali_label_frame.frame, 7, "Adjsted Amount", padx=255)
ali_tax_rate_label = label_class(ali_label_frame.frame, 9, "Tax Rate")

withdraw_rate_label = label_class(ali_label_frame.frame, 15, "Estimated\nWithdraw Rate")
total_amount_from_bank_label = label_class(ali_label_frame.frame, 15, "Total Amount\nFrom Bank", padx=255)
#net_profit_label = label_class(ali_label_frame.frame, 9, "Profit")

###### Create Text Boxes

# Create Varibles
ebay_data_added_date_sl_var = StringVar()
ebay_sold_date_pdt_var = StringVar()
ebay_paid_date_pdt_var = StringVar()

ebay_listingID_var = StringVar()
ebay_lising_title_var = StringVar()
ebay_listed_price_var = StringVar()
ebay_listed_price_var.set('')

ebay_sale_record_number_var = StringVar()
ebay_sold_price_without_tax_var = StringVar()
ebay_sold_price_without_tax_var.set('')
ebay_shipping_cost_var = StringVar()
ebay_shipping_cost_var.set('')
ebay_tax_amount_var = StringVar()
ebay_tax_amount_var.set('')

buyer_id_var = StringVar()
buyer_email_var = StringVar()
buyer_name_var = StringVar()
buyer_phone_number_var = StringVar()

shipping_name_var = StringVar()
shipping_apt_var = StringVar()
shipping_phone_number_var = StringVar()
shipping_country_var = StringVar()
shipping_state_var = StringVar()
shipping_city_var = StringVar()
shipping_zipcode_var = StringVar()
shipping_street_var = StringVar()

tracking_added_date_pdt_var = StringVar()
tracking_number_var = StringVar()
shipping_carrier_var = StringVar()
estimated_delivery_date_var = StringVar()

ali_order_date_sl_var = StringVar()
ali_item_price_var = DoubleVar().set('')
ali_shipping_cost_var = DoubleVar().set('')
ali_tax_charged_var = DoubleVar().set('')
ali_adjust_price_var = DoubleVar().set('')
ali_tax_rate_var = DoubleVar().set('')
ali_paid_date_var = StringVar()

withdraw_rate_var = StringVar()
withdraw_rate_var.set('195')
total_amount_from_bank_var = StringVar()
total_amount_from_bank_var.set('')
#net_profit_var = DoubleVar()

# Determining the date the data will be added
today_date = date.today()
ebay_data_added_date_sl_var.set(today_date)

# eBay Detail Text Boxes
ebay_data_added_date_sl_text_box = checkbox_with_entry(frame=ebay_date_details_label_frame.frame, row=2, padx=35, var=ebay_data_added_date_sl_var, entry_state="d", check='Y')
ebay_sold_date_pdt_text_box = entry_box(frame=ebay_date_details_label_frame.frame, row=4, padx=35, var=ebay_sold_date_pdt_var)
ebay_paid_date_pdt_text_box = paid_date_entry_box(frame=ebay_date_details_label_frame.frame, row=6, padx=35, var=ebay_paid_date_pdt_var) ######

ebay_listingID_text_box = listingID_class(frame=ebay_listing_details_label_frame.frame, row=2, padx=35, var=ebay_listingID_var)
ebay_listing_title_text_box = listing_title_class(frame=ebay_listing_details_label_frame.frame, row=4, padx=35, var=ebay_lising_title_var)
ebay_listed_price_text_box = entry_box(frame=ebay_listing_details_label_frame.frame, row=6, padx=35, var=ebay_listed_price_var)

ebay_sale_record_number_text_box = entry_box(frame=ebay_sold_details_label_frame.frame, row=2, padx=35, var=ebay_sale_record_number_var)

#-----------------------------------------------------------------------------
#ebay_sold_price_without_tax_text_box = sold_price_without_tax_class(frame=ebay_sold_details_label_frame.frame, row=2, padx=33, var=ebay_sold_price_without_tax_var)
#ebay_shipping_cost_text_box = entry_box(frame=ebay_sold_details_label_frame.frame, row=3, padx=33, var=ebay_shipping_cost_var)
#ebay_tax_amount_text_box = entry_box(frame=ebay_sold_details_label_frame.frame, row=4, padx=33, var=ebay_tax_amount_var)
#-----------------------------------------------------------------------------

#ebay_total_without_tax_text_box = entry_box(frame=ebay_sold_details_label_frame.frame, row=5, padx=33)
#ebay_tax_rate_text_box = entry_box(frame=ebay_sold_details_label_frame.frame, row=6, padx=33)
#ebay_final_value_fee_text_box = entry_box(frame=ebay_sold_details_label_frame.frame, row=7, padx=33)
#paypal_fee_text_box = entry_box(frame=ebay_sold_details_label_frame.frame, row=8, padx=33)

buyer_id_text_box = entry_box(frame=ebay_buyer_details_label_frame.frame, row=2, padx=35, var=buyer_id_var)
buyer_email_text_box = entry_box(frame=ebay_buyer_details_label_frame.frame, row=4, padx=35, var=buyer_email_var)
buyer_name_text_box = entry_box(frame=ebay_buyer_details_label_frame.frame, row=6, padx=35, var=buyer_name_var)
buyer_phone_number_text_box = entry_box(frame=ebay_buyer_details_label_frame.frame, row=8, padx=35, var=buyer_phone_number_var)

shipping_name_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=2, padx=35, var=shipping_name_var)
shipping_phone_number_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=4, padx=35, var=shipping_phone_number_var)


########################################!




states = ( 'AL - Alabama', 'AK - Alaska', 'AZ - Arizona', 'AR - Arkansas', 'CA - California', 'CO - Colorado', 'CT - Connecticut', 'DE - Delaware', 'FL - Florida', 'GA - Georgia', 'HI - Hawaii', 'ID - Idaho', 'IL - Illinois', 'IN - Indiana', 'IA - Iowa', 'KS - Kansas', 'KY - Kentucky', 'LA - Louisiana', 'ME - Maine', 'MD - Maryland', 'MA - Massachusetts', 'MI - Michigan', 'MN - Minnesota', 'MS - Mississippi', 'MO - Missouri', 'MT - Montana', 'NE - Nebraska', 'NV - Nevada', 'NH - New Hampshire', 'NJ - New Jersey', 'NM - New Mexico', 'NY - New York', 'NC - North Carolina', 'ND - North Dakota', 'OH - Ohio', 'OK - Oklahoma', 'OR - Oregon', 'PA - Pennsylvania', 'RI - Rhode Island', 'SC - South Carolina', 'SD - South Dakota', 'TN - Tennessee', 'TX - Texas', 'UT - Utah', 'VT - Vermont', 'VA - Virginia', 'WA - Washington', 'WV - West Virginia', 'WI - Wisconsin', 'WY - Wyoming' )

countries = ( 'Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'APO/FPO', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan Republic', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde Islands', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia, Republic of', 'Cyprus', 'Czech Republic', "CÃ´te d'Ivoire (Ivory Coast)", 'Democratic Republic of the', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Islas Malvinas)', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon Republic', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of the', 'Reunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Helena', 'Saint Kitts-Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'UAE - United Arab Emirates', 'UK - United Kingdom', 'US - United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City State', 'Venezuela', 'Vietnam', 'Virgin Islands (U.S.)', 'Wallis and Futuna', 'Western Sahara', 'Western Samoa', 'Yemen', 'Zambia', 'Zimbabwe' )


def callback(comboCountryVar):
        if comboCountryVar.get()[:2] == "US":
                shipping_state_text_box.entry.grid_remove()
                comboState.grid(row=6, column=1, pady=(0,20), sticky=E)
        else:
                comboState.grid_remove()
                shipping_state_text_box.entry.grid()


comboCountryVar = StringVar()
comboStateVar = StringVar()
comboCountryVar.trace("w", lambda *args, comboCountryVar=comboCountryVar: callback(comboCountryVar))

comboCountry = AutocompleteCombobox(ebay_shipping_details_label_frame.frame)
comboCountry.set_completion_list(countries, "ComboboxLong2", comboCountryVar)
comboCountry.grid(row=6, column=1, padx=(35,0), pady=(0,20), sticky=W)

comboState = AutocompleteCombobox(ebay_shipping_details_label_frame.frame)
comboState.set_completion_list(states, "ComboboxShort", comboStateVar)


#combo1.focus_set()
shipping_state_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=6, padx=35, var=shipping_state_var, entryStyle="EntryShort1")

#shipping_country_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=6, padx=35, var=shipping_country_var, entryStyle="EntryShort")
#shipping_state_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=8, padx=35, var=shipping_state_var)
shipping_zipcode_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=10, padx=35, var=shipping_zipcode_var, entryStyle="EntryShort1", sticky=W)
shipping_city_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=10, padx=35, var=shipping_city_var, entryStyle="EntryLong2")
shipping_street_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=14, padx=35, var=shipping_street_var)
shipping_apt_text_box = entry_box(frame=ebay_shipping_details_label_frame.frame, row=16, padx=35 ,var=shipping_apt_var)

tracking_added_date_pdt_text_box = entry_box(frame=ebay_tracking_details_label_frame.frame, row=2, padx=35, var=tracking_added_date_pdt_var)
tracking_number_text_box = entry_box(frame=ebay_tracking_details_label_frame.frame, row=4, padx=35, var=tracking_number_var)

#########################################!

#shipping_carrier_text_box = entry_box(frame=ebay_tracking_details_label_frame.frame, row=6, padx=35, var=shipping_carrier_var)

carriers = ("4PX", "4PX CHINA", "4PX Express", "4PX LTD", "7LSP", "A Duie Pyle", "A J Express", "A1 Courier Services", "AAA Cooper", "AB Custom Group", "ABF", "ABX Express", "aCommerce", "ACS Courier", "Adicional Logistics", "AeroPost", "AFL", "AIR21", "Airpak Express", "Airspeed International Corporation", "AIT Worldwide", "ALLIED EXPRESS", "AlphaFAST", "Amazon Logistics", "AMWST", "An Post", "AO", "APC Overnight Reference", "APC Overnight UK", "APC Postal Logistics US", "APG", "APPLE EXPRESS", "Aprisa Express", "Aquiline", "ARAMEX", "Aramex Australia", "Arrow XL", "ARVATO", "Asendia Germany", "Asendia UK", "Asendia USA", "ASM", "Australia Post", "Australian Air Express", "Austrian Post Registered", "AVRT", "AXL Express & Logistics", "B Post", "B2C Europe", "Bartolini", "BELGIAN POST", "Belgium Post", "Belpost", "Bert Transport", "Best Overnite", "Best Way Parcel", "BirdSystem", "BKNS", "Blue Package", "Bluecare Express", "Bluedart", "Bombino Express Pvt Ltd", "Bonds Couriers", "Border Express", "Boxberry", "Boxc", "Brazil Correios", "Brokers World Wide", "BRT Bartolini", "Bulgarian Posts", "BusinessPost", "Buylogic", "Cambodia Post", "Canada Post", "CanPar", "Capital Transport", "Cainiao", "Caribou", "CBL Logistics", "CENF", "Central Arizona Freight", "Central Transport", "Century Express Courier Services", "Ceska Posta", "CEVA", "CH Robinson", "China Post", "Chit Chats Express", "Chronoexpres", "Chronopost", "Chronopost Portugal", "CHUKOU1", "CHUKOU1_EXPRESS", "Chunghwa Post", "CitiPost", "City Link", "City Link Express", "CJ GLS Korea", "CJ Korea Express Thailand", "Click and Quick", "CNWY", "Coles", "Coliposte Domestic", "Coliposte International", "Colis Prive", "Colissimo", "CollectCo", "CollectPlus", "Conway Freight", "Copa Airlines Courier", "Copa Courier", "Correo Argentino", "Correos", "Correos Chile", "Correos de Costa Rica", "Correos de Mexico", "Correos Express", "costmeticsnow", "Courex", "Courier IT", "Courier Plus", "Courier Post", "Couriers Please", "Coyote", "CTT", "Cyprus Post", "DAI Post", "DATS", "Dawn Wing", "Day and Ross", "Daylight Transport", "Dayton Freight Lines", "DB Schenker", "DB Schenker Sweden", "DD Express Courier", "Delcart", "Delhivery", "deliverE", "Deltec Courier", "Demand Ship", "Detrack", "Deutsche Post", "DHE", "DHEKEN", "DHL", "DHL 2 Mann", "DHL Active Tracing", "DHL Benelux", "DHL eCommerce", "DHL Express", "DHL Express PieceID", "DHL Global Forwarding", "DHL Global Mail Americas", "DHL Netherlands", "DHL Parcel NL", "DHL Poland Domestic", "DHL SC AU", "DHL Spain Domestic", "DHLEKB", "DHLG", "Diamond Line", "Die Schweizerische Post", "Direct Couriers", "Direct Freight Express", "Direct Link", "Directlog", "DMM Network", "Dohrn", "Doora Logistics", "Dotzot", "DPD", "DPD Ireland", "DPD Poland", "DPD Romania", "DPE South Africa", "DPEX", "DPX Thailand", "DSV", "DTDC Australia", "DTDC Express Ltd", "DTDC India", "DTS", "Ducros", "DX", "DX Freight", "Dynalogic Benelux BV", "Dynamic Logistics", "E GO", "Easy Mail", "eBay Delivery Services", "eBay Secure Local Pickup", "eBay SendIt", "eBayBopisAU", "eBayBopisCA", "eBayBopisDE", "eBayBopisUK", "eBayBopisUS", "eBayNowAU", "eBayNowDE", "eBayNowUK", "eBayNowUS", "eBayPostageLabels", "Ecargo", "Echo", "ECMS International Logistics", "Ecom Express", "EDI Express", "EFS Fulfillment Service", "Ekart", "ELTA Hellenic Post", "Email Delivery", "EMF", "Emirates Post", "Endeavour Delivery", "Ensenda", "Enterprise des Poste Laos", "Envialia", "eParcel Korea", "Epic Freight", "Estafeta", "Estes", "eTotal Solution Limited", "Eurodis", "Exapaq", "Expeditors", "EZship", "FAR International", "Fastrak Services", "Fastway", "Fastway Australia", "FASTWAY COURIERS", "Fastway Ireland", "Fastway New Zealand", "Fastway South Africa", "FDXCP", "FedEx", "FedEx Poland Domestic", "FedEx Smart Post", "FERCAM Logistics & Transport", "Fiege", "First Flight Couriers", "First Logistics", "FLYT", "FLYT Express", "FlytExpress US Direct line", "Forward Air", "FTFT", "FulfilExpress-AccStation", "FulfilExpress-eForCity", "FulfilExpress-EverydaySource", "FulfilExpress-iTrimming", "Gati KWE", "GDEX", "Gel Express", "General Overnight", "Geniki Taxydromiki", "Geodis Distribution", "Geodis Espace", "Giao Hang Nhanh", "Global Tranz", "Globe Logistics", "Globegistics", "GLS", "GLS Italy", "GLS Netherlands", "Gofly", "GoJavas", "Greyhound", "GSI EXPRESS", "GSO", "Haidaibao", "HDUSA", "Hercules", "Hermes", "Hermes Italy", "Holisol", "Holland", "Home Delivery Network", "Homedirect Logistics", "Hong Kong Post", "Hrvatska Posta", "HUNTER EXPRESS", "i-parcel", "Iceland Post", "iCumulus", "IDS Logistics", "iLoxx", "IMEX Global Solutions", "IML", "IMX Mail", "In Post", "India Post", "India Post Domestic", "India Post International", "Indonesia Post", "Innovel", "InPost", "InPost Paczkomaty", "Instand Tion Nam Express", "Interlink", "Interlink Express", "Interlink Express Reference", "International Seur", "Interparcel Australia", "Interparcel New Zealand", "Interparcel UK", "InterPost", "IoInvio", "Israel Post", "Israel Post Domestic", "Jam Express", "Japan Post", "Jersey Post", "Jet Ship Worldwide", "JEX Jayon Express", "JNE", "Jocom", "JP BH Posta", "JX", "Kangaroo Worldwide Express", "Kerry Express Thailand", "Kerry TTC Express", "KGM Hub", "KIALA", "Korea Post", "Kuehne Nagel", "Kurasi", "KWT Logistics", "LA POSTE", "Landmark", "Landmark Global", "Lao Post", "Lasership", "Latvia Post", "LBC Express", "LDSO", "LexShip", "Liccardi Express Courier", "Lietuvos Pastas", "Line Clear Express & Logistics Sdn Bhd", "Lion Parcel", "Logwin Logistics", "LoneStar Overnight", "LTL", "M Xpress", "Magyar Posta", "MailAmericas", "Main Freight", "MALAYSIA POST", "Malaysia Post EMS", "Malaysia Post Registered", "Manna Freight", "Mara Xpress", "Matdespatch", "Matkahuolto", "Maxcellents Pte Ltd", "MDS Collivery", "Metapack", "Mexico AeroFlash", "Mexico Redpack", "Mexico Senda Express", "Mikropakket", "MNG Turkey", "Mondial Relay", "MRW", "MSI", "MUDITA", "Mypostonline", "NACEX", "Nationwide Express", "NEMF", "New Zealand Post", "Newgistics", "NewPenn", "Nexive", "Nhans Solutions", "Nightline", "Nim Express", "Ninja Van", "Ninja Van Indonesia", "Ninja Van Malaysia", "Ninja Van Philippines", "Ninja Van Thailand", "NiPost", "Norsk Global", "Nova Poshta", "Nova Poshta International", "NuvoEx", "NZ Post", "Oak Harbor", "OCA Argentina", "OCS ANA", "OCS International", "ODFL", "OFFD", "Old Dominion Freight Line", "Omni Logistics", "omniparcel", "Omniva", "One World Express", "OnTrac", "Orange Connex", "Other", "OVNT", "Packlink", "PAL Express Limited", "Pandu Logistics", "Panther", "Panther Order Number", "Panther Reference", "Paquetexpress", "Parcel Express", "Parcel One", "Parcel Point", "Parcel Pool", "Parcel Post Singapore", "Parcel2Go", "ParcelForce", "Parcelled In", "PBCB", "PBI_UK", "Peninsula", "PF Logistics", "Philpost", "Pilot", "Pilot Freight Services", "PITD", "Pitt Ohio Trucking", "Poczta Polska", "Pocztex", "Portugal CTT", "Portugal Seur", "Pos Indonesia Domestic", "Post Danmark", "POST ITALIANO", "Post NL", "Post Nord Norway", "Post Serbia", "Posta Romana", "Poste Italiane", "Poste Italiane Paccocelere", "Posten Norge", "Posti", "PostNL Domestic", "PostNL International", "PostNL International 3S", "PostNord Logistics", "Postur Is", "Prestige", "Priority1", "Professional Couriers", "PTT Posta", "Purolator", "Quantium Solutions", "Qxpress", "Raben Group", "RAF Philippines", "RaidereX", "RAM", "Red Carpet Logistics", "Red Express", "Red Express Waybill", "Redur Spain", "RETL", "Rincos", "Rist Transport", "RL Carriers", "Roadbull Logistics", "Rocket Parcel International", "Royal Mail", "Royal Shipments", "RPD2man Deliveries", "RPX Indonesia", "rpxonline", "RR Donnelley", "RRUN", "Russian Post", "RZY Express", "Safexpress", "Sagawa", "SAIA", "SAIA LTL Freight", "SAILPOST", "sapo", "Saudi Post", "Scudex Express", "SDA", "SEKO", "Sending", "Sendit", "Sendle", "Seur", "SF EXPESS", "SFC", "SFC Express", "SFC_EXPRESS", "SGT Corriere Espresso", "Shippit", "Shopfans RU", "SHREE TIRUPATI COURIER SERVICES", "Shunyou Post", "SimplyPost", "SINGAPORE POST", "Singapore Speedpost", "Siodemka", "Sioli and Fontana", "Siódemka", "SKYBOX", "Skynet Malaysia", "SkyNet Worldwide", "SkyNet Worldwide Express", "SkyNet Worldwide Express UAE", "Skynet Worldwide Express UK", "skypostal", "SMART SEND", "SMSA Express", "Sogetras", "SortHub", "South African Post Office", "Southeastern Freight Lines", "Spanish Seur", "Specialised Freight", "Spediamo", "Speed Couriers", "SpeeDee", "Speedex Courier", "SpeedPAK", "SPRING", "SRE Korea", "Star Track Courier", "StarTrack", "Suntek Express LTD", "Sweden Posten", "Swiss Post", "TAQBIN Malaysia", "TAQBIN Singapore", "Taxy Dromiki", "TCS", "TELE", "Teliway SIC Express", "TEMANDO", "THAILAND POST", "The Courier Guy", "The Custom Companies", "Tiki", "TIPSA", "TNT", "TNT Australia", "TNT Click Italy", "TNT EXPRESS", "TNT France", "TNT Italy", "TNT Post", "TNT Post Italy Nexive", "TNT Reference", "TNT UK", "TNT UK Reference", "Toll", "Toll IPEC", "Toll Priority", "Topyou", "TPG", "TrakPak", "TransMission", "Tuffnells Parcels Express", "TWW", "UBI", "UK Mail", "Ukraposhta", "Unishippers", "United Delivery Service", "UPS", "UPS Mail Innovations", "UPSC", "USFG", "uShip Freight", "USPS", "USPS CeP", "USPS PMI", "Veritiv", "VicTas Freight Express", "Vietnam Post", "Vietnam Post EMS", "ViettelPost", "Vision Express", "VITR", "Wahana", "Wanb Express", "WanSe", "Ward", "WATKINS", "wedo", "WePost Logistics", "Whistl", "Wilson Trucking", "Winit", "WISE", "Wiseloads", "WNdirect", "Worldwide Express", "WPX", "XDP Express", "XDP Express Reference", "Xend Express", "XL Express", "XPO LTL", "Xpost", "XpressBees", "Yakit", "Yamato Japan", "YANWEN", "Yodel", "Yodel International", "YRC", "Yun Express", "Zalora 7 Eleven", "ZeptoExpress", "Zinc", "Zyllem", "Österreichische Post AG")
combocarrierVar = StringVar()

combocarrier = AutocompleteCombobox(ebay_tracking_details_label_frame.frame)
combocarrier.set_completion_list(carriers, "ComboboxLong1", combocarrierVar)
combocarrier.grid(row=6, column=1, padx=(35,0), pady=(0,20), sticky=W)

estimated_delivery_date_text_box = entry_box(frame=ebay_tracking_details_label_frame.frame, row=8, padx=35, var=estimated_delivery_date_var)

# Aliexpress Detals Text Boxes
ali_order_date_sl_text_box = entry_box(frame=ali_label_frame.frame, row=2, padx=35, var=ali_order_date_sl_var)
ali_paid_date_text_box = entry_box(frame=ali_label_frame.frame, row=4, padx=35, var=ali_paid_date_var)
ali_item_price_text_box = entry_box(frame=ali_label_frame.frame, row=6, padx=35, var=ali_item_price_var, entryStyle="EntryMiddle", sticky=W)
ali_shipping_cost_text_box = entry_box(frame=ali_label_frame.frame, row=6, padx=35, var=ali_shipping_cost_var, entryStyle="EntryMiddle")
ali_tax_charged_text_box = entry_box(frame=ali_label_frame.frame, row=8, padx=35, var=ali_tax_charged_var, entryStyle="EntryMiddle", sticky=W)
ali_adjust_price_text_box = entry_box(frame=ali_label_frame.frame, row=8, padx=35, var=ali_adjust_price_var, entryStyle="EntryMiddle")
ali_tax_rate_text_box = entry_box(frame=ali_label_frame.frame, row=10, padx=35, var=ali_tax_rate_var, entryStyle="EntryMiddle", sticky=W)

withdraw_rate_text_box = checkbox_with_entry(frame=ali_label_frame.frame, row=16, padx=35, var=withdraw_rate_var, entry_state="d", check='Y', entryStyle="EntryMiddle", sticky=W)
total_amount_from_bank_text_box = entry_box(frame=ali_label_frame.frame, row=16, padx=35, var=total_amount_from_bank_var, entryStyle="EntryMiddle")
#net_profit_text_box = entry_box(frame=ali_label_frame.frame, row=9, padx=1, var=)

# Grid first time label
currency = "USD"
currencyLabel = Label(ali_label_frame.frame, text=currency, font=('Typo Round Edited', 11), bg='#262626')
currencyLabel.place(x=400, y=482)

# Create CheckButton using class
currencyCheck = currencyCheckbuttonClass(ali_label_frame.frame)
currencyCheck.currencyCheckbutton(ali_label_frame.frame, labelX=400, labelY=482, firstLabel=currencyLabel)
currencyCheck.place(x=400, y=437)

ebay_sold_price_without_tax_text_box = ttk.Entry(ebay_sold_details_label_frame.frame, textvariable=ebay_sold_price_without_tax_var, justify='center', font=('Typo Round Edited', 11), style="EntryShort2", width=5)
ebay_sold_price_without_tax_text_box.place(x=35, y=129)

ebay_shipping_cost_text_box = ttk.Entry(ebay_sold_details_label_frame.frame, textvariable=ebay_shipping_cost_var, justify='center', font=('Typo Round Edited', 11), style="EntryShort2", width=5)
ebay_shipping_cost_text_box.place(x=178, y=129)

ebay_tax_amount_text_box = ttk.Entry(ebay_sold_details_label_frame.frame, textvariable=ebay_tax_amount_var, justify='center', font=('Typo Round Edited', 11), style="EntryShort2", width=5)
ebay_tax_amount_text_box.place(x=322, y=129)



#####################################!



#### Create Output Canvases

### Tatal(without tax) canvas
total_canvas = Canvas(canvas_output_frame, width = 205, height = 144, bg='#1f1f1f', highlightthickness=0)
total_canvas.grid(row=1, column=1, padx=(42,0), pady=(60,0))
total_image = Image.open('Canvas Shapes/1.1.png')
total_image = total_image.resize((184, 120), Image.ANTIALIAS)
total_image_img = ImageTk.PhotoImage(total_image)
total_canvas.create_image(96,75, image=total_image_img)

# Create a before text
total_text = total_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))

#Blank Label
total_sold_price_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def total_callback1(total_sold_price_var):
    global total_text
    total_canvas.delete(total_text)

    global total_sold_price_error_label
    total_sold_price_error_label.destroy()

    # Check received text int or str
    try:
        if total_sold_price_var.get() == '' or type(float(total_sold_price_var.get())) == float:
            # Check total_sold_price_var
            if total_sold_price_var.get() == '':
                total_sold_price_value = 0
            else:
                total_sold_price_value = float(total_sold_price_var.get())
            
            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                total_shipping_value = 0
            else:
                total_shipping_value = float(ebay_shipping_cost_var.get())
            
            total_text = total_sold_price_value + total_shipping_value
            
            # If both values are 0 then maintain the value at 0
            if total_sold_price_value == 0 and total_shipping_value == 0:
                total_text = total_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                total_text = total_canvas.create_text(35,86 ,text='$'+str("%.2f" % total_text), anchor=W, fill='white', font=('Gelion Black', 21))
   
    except Exception:
        # Maintaining the total value at '0'
        total_text = total_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        total_sold_price_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        total_sold_price_error_label.place(x=365, y=26)

ebay_sold_price_without_tax_var.trace('w', lambda *args, ebay_sold_price_without_tax_var=ebay_sold_price_without_tax_var: total_callback1(ebay_sold_price_without_tax_var))

# Blank Label
total_shipping_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for total_shipping variable
def total_callback2(total_shipping_var):
    global total_text
    total_canvas.delete(total_text)

    global total_shipping_error_label
    total_shipping_error_label.destroy()

    try:
        if total_shipping_var.get() == '' or type(float(total_shipping_var.get())) == float:
            # Check total_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                total_sold_price_value = 0
            else:
                total_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if total_shipping_var.get() == '':
                total_shipping_value = 0
            else:
                total_shipping_value = float(total_shipping_var.get())
            
            total_text = total_sold_price_value + total_shipping_value

            # If both values are 0 then maintain the value at 0
            if total_sold_price_value == 0 and total_shipping_value == 0:
                total_text = total_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                total_text = total_canvas.create_text(35,86 ,text='$'+str("%.2f" % total_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the total value at '0'
        total_text = total_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        total_shipping_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        total_shipping_error_label.place(x=365, y=61)

ebay_shipping_cost_var.trace('w', lambda *args, ebay_shipping_cost_var=ebay_shipping_cost_var: total_callback2(ebay_shipping_cost_var))

### Profit canvas
profit_value_canvas = Canvas(canvas_output_frame, width = 205, height = 144, bg='#1f1f1f', highlightthickness=0)
profit_value_canvas.grid(row=1, column=2, padx=(20,0), pady=(60,0))
profit_value_image = Image.open('Canvas Shapes/1.2.png')
profit_value_image = profit_value_image.resize((184, 120), Image.ANTIALIAS)
profit_value_image_img = ImageTk.PhotoImage(profit_value_image)
profit_value_canvas.create_image(96,75, image=profit_value_image_img)

# Create a before text
profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))


#Black Label
profit_value_sold_price_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def profit_value_callback1(profit_value_sold_price_var):
    global profit_value_text
    profit_value_canvas.delete(profit_value_text)

    global profit_value_sold_price_error_label
    profit_value_sold_price_error_label.destroy()

    # Check received text int or str
    try:
        if profit_value_sold_price_var.get() == '' or type(float(profit_value_sold_price_var.get())) == float:

            # Check profit_value_sold_price_var
            if profit_value_sold_price_var.get() == '':
                profit_value_sold_price_value = 0
            else:
                profit_value_sold_price_value = float(profit_value_sold_price_var.get())
            
            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                profit_value_shipping_value = 0
            else:
                profit_value_shipping_value = float(ebay_shipping_cost_var.get())

            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                profit_value_tax_value = 0
            else:
                profit_value_tax_value = float(ebay_tax_amount_var.get())

            # Check total_amount_from_bank_var
            if total_amount_from_bank_var.get() == '':
                profit_tot_from_bank_value = 0
            else:
                profit_tot_from_bank_value = float(total_amount_from_bank_var.get())

            # Check withdraw_rate_var
            if withdraw_rate_var.get() == '':
                profit_withdraw_rate_value = 0
            else:
                profit_withdraw_rate_value = float(withdraw_rate_var.get())
            
            profit_total_text = profit_value_sold_price_value + profit_value_shipping_value
            profit_final_value_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(12.55/100)) + 0.30
            profit_international_fee_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(1.3/100))
            profit_payoneer_fee_text = (((profit_value_sold_price_value + profit_value_shipping_value)-(((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(13.85/100))+0.30))*2)/100

            profit_temp = profit_total_text - (profit_final_value_text + profit_international_fee_text + profit_payoneer_fee_text)
            profit_temp = float("{:.2f}".format(profit_temp))

            profit_value_text = (profit_temp * profit_withdraw_rate_value) - profit_tot_from_bank_value
            
            # If 5 values are 0 then maintain the value at 0
            if profit_value_sold_price_value == 0 and profit_value_shipping_value == 0 and profit_value_tax_value == 0 and profit_withdraw_rate_value == 0 and profit_tot_from_bank_value == 0:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.'+str("%.2f" % profit_value_text), anchor=W, fill='white', font=('Gelion Black', 21))
   
    except Exception:
        # Maintaining the profit_value value at '0'
        profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        profit_value_sold_price_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        profit_value_sold_price_error_label.place(x=365, y=26)

ebay_sold_price_without_tax_var.trace('w', lambda *args, ebay_sold_price_without_tax_var=ebay_sold_price_without_tax_var: profit_value_callback1(ebay_sold_price_without_tax_var))

# Blank Label
profit_value_shipping_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def profit_value_callback2(profit_value_shipping_var):
    global profit_value_text
    profit_value_canvas.delete(profit_value_text)

    global profit_value_shipping_error_label
    profit_value_shipping_error_label.destroy()

    try:
        if profit_value_shipping_var.get() == '' or type(float(profit_value_shipping_var.get())) == float:
            # Check profit_value_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                profit_value_sold_price_value = 0
            else:
                profit_value_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if profit_value_shipping_var.get() == '':
                profit_value_shipping_value = 0
            else:
                profit_value_shipping_value = float(profit_value_shipping_var.get())
            
            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                profit_value_tax_value = 0
            else:
                profit_value_tax_value = float(ebay_tax_amount_var.get())

            # Check total_amount_from_bank_var
            if total_amount_from_bank_var.get() == '':
                profit_tot_from_bank_value = 0
            else:
                profit_tot_from_bank_value = float(total_amount_from_bank_var.get())

            # Check withdraw_rate_var
            if withdraw_rate_var.get() == '':
                profit_withdraw_rate_value = 0
            else:
                profit_withdraw_rate_value = float(withdraw_rate_var.get())
            
            #profit_value_text = profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value
            profit_total_text = profit_value_sold_price_value + profit_value_shipping_value
            profit_final_value_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(12.55/100)) + 0.30
            profit_international_fee_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(1.3/100))
            profit_payoneer_fee_text = (((profit_value_sold_price_value + profit_value_shipping_value)-(((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(13.85/100))+0.30))*2)/100
            
            profit_temp = profit_total_text - (profit_final_value_text + profit_international_fee_text + profit_payoneer_fee_text)
            profit_temp = float("{:.2f}".format(profit_temp))

            profit_value_text = (profit_temp * profit_withdraw_rate_value) - profit_tot_from_bank_value

            # If 3 values are 0 then maintain the value at 0
            if profit_value_sold_price_value == 0 and profit_value_shipping_value == 0 and profit_value_tax_value == 0 and profit_withdraw_rate_value == 0 and profit_tot_from_bank_value == 0:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.'+str("%.2f" % profit_value_text), anchor=W, fill='white', font=('Gelion Black', 21))


    except Exception:
        # Maintaining the profit_value value at '0'
        profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        profit_value_shipping_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        profit_value_shipping_error_label.place(x=365, y=61)

ebay_shipping_cost_var.trace('w', lambda *args, ebay_shipping_cost_var=ebay_shipping_cost_var: profit_value_callback2(ebay_shipping_cost_var))

# Blank Label
profit_value_tax_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for tax variable
def profit_value_callback3(profit_value_tax_var):
    global profit_value_text
    profit_value_canvas.delete(profit_value_text)

    global profit_value_tax_error_label
    profit_value_tax_error_label.destroy()

    try:
        if profit_value_tax_var.get() == '' or type(float(profit_value_tax_var.get())) == float:
            # Check profit_value_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                profit_value_sold_price_value = 0
            else:
                profit_value_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                profit_value_shipping_value = 0
            else:
                profit_value_shipping_value = float(ebay_shipping_cost_var.get())
            
            # Check ebay_tax_amount_var
            if profit_value_tax_var.get() == '':
                profit_value_tax_value = 0
            else:
                profit_value_tax_value = float(profit_value_tax_var.get())

            # Check total_amount_from_bank_var
            if total_amount_from_bank_var.get() == '':
                profit_tot_from_bank_value = 0
            else:
                profit_tot_from_bank_value = float(total_amount_from_bank_var.get())

            # Check withdraw_rate_var
            if withdraw_rate_var.get() == '':
                profit_withdraw_rate_value = 0
            else:
                profit_withdraw_rate_value = float(withdraw_rate_var.get())
            
            profit_total_text = profit_value_sold_price_value + profit_value_shipping_value

            profit_final_value_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(12.55/100)) + 0.30
            profit_international_fee_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(1.3/100))
            profit_payoneer_fee_text = (((profit_value_sold_price_value + profit_value_shipping_value)-(((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(13.85/100))+0.30))*2)/100
           
            profit_temp = profit_total_text - (profit_final_value_text + profit_international_fee_text + profit_payoneer_fee_text)
            profit_temp = float("{:.2f}".format(profit_temp))

            profit_value_text = (profit_temp * profit_withdraw_rate_value) - profit_tot_from_bank_value
            
            # If 3 values are 0 then maintain the value at 0
            if profit_value_sold_price_value == 0 and profit_value_shipping_value == 0 and profit_value_tax_value == 0 and profit_withdraw_rate_value == 0 and profit_tot_from_bank_value == 0:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.'+str("%.2f" % profit_value_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the profit_value value at '0'
        profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        profit_value_tax_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        profit_value_tax_error_label.place(x=365, y=96)

ebay_tax_amount_var.trace('w', lambda *args, ebay_tax_amount_var=ebay_tax_amount_var: profit_value_callback3(ebay_tax_amount_var))


# Blank Label
tot_from_bank_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for tax variable
def profit_value_callback4(profit_value_tot_from_bank_var):
    global profit_value_text
    profit_value_canvas.delete(profit_value_text)

    global tot_from_bank_error_label
    tot_from_bank_error_label.destroy()

    try:
        if profit_value_tot_from_bank_var.get() == '' or type(float(profit_value_tot_from_bank_var.get())) == float:
            # Check profit_value_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                profit_value_sold_price_value = 0
            else:
                profit_value_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                profit_value_shipping_value = 0
            else:
                profit_value_shipping_value = float(ebay_shipping_cost_var.get())
            
            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                profit_value_tax_value = 0
            else:
                profit_value_tax_value = float(ebay_tax_amount_var.get())

            # Check profit_value_tot_from_bank_var
            if profit_value_tot_from_bank_var.get() == '':
                profit_tot_from_bank_value = 0
            else:
                profit_tot_from_bank_value = float(profit_value_tot_from_bank_var.get())

            # Check withdraw_rate_var
            if withdraw_rate_var.get() == '':
                profit_withdraw_rate_value = 0
            else:
                profit_withdraw_rate_value = float(withdraw_rate_var.get())
            
            profit_total_text = profit_value_sold_price_value + profit_value_shipping_value
            profit_final_value_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(12.55/100)) + 0.30
            profit_international_fee_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(1.3/100))
            profit_payoneer_fee_text = (((profit_value_sold_price_value + profit_value_shipping_value)-(((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(13.85/100))+0.30))*2)/100

            profit_temp = profit_total_text - (profit_final_value_text + profit_international_fee_text + profit_payoneer_fee_text)
            profit_temp = float("{:.2f}".format(profit_temp))

            profit_value_text = (profit_temp * profit_withdraw_rate_value) - profit_tot_from_bank_value
            
            # If 5 values are 0 then maintain the value at 0
            if profit_value_sold_price_value == 0 and profit_value_shipping_value == 0 and profit_value_tax_value == 0 and profit_withdraw_rate_value == 0 and profit_tot_from_bank_value == 0:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.'+str("%.2f" % profit_value_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the profit_value value at '0'
        profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        tot_from_bank_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        tot_from_bank_error_label.place(x=365, y=96)

total_amount_from_bank_var.trace('w', lambda *args, total_amount_from_bank_var=total_amount_from_bank_var: profit_value_callback4(total_amount_from_bank_var))

# Blank Label
profit_value_withdraw_rate_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for tax variable
def profit_value_callback5(profit_value_withdraw_rate_var):
    global profit_value_text
    profit_value_canvas.delete(profit_value_text)

    global profit_value_withdraw_rate_error_label
    profit_value_withdraw_rate_error_label.destroy()

    try:
        if profit_value_withdraw_rate_var.get() == '' or type(float(profit_value_withdraw_rate_var.get())) == float:
            # Check profit_value_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                profit_value_sold_price_value = 0
            else:
                profit_value_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                profit_value_shipping_value = 0
            else:
                profit_value_shipping_value = float(ebay_shipping_cost_var.get())
            
            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                profit_value_tax_value = 0
            else:
                profit_value_tax_value = float(ebay_tax_amount_var.get())

            # Check total_amount_from_bank_var
            if total_amount_from_bank_var.get() == '':
                profit_tot_from_bank_value = 0
            else:
                profit_tot_from_bank_value = float(total_amount_from_bank_var.get())

            # Check withdraw_rate_var
            if profit_value_withdraw_rate_var.get() == '':
                profit_withdraw_rate_value = 0
            else:
                profit_withdraw_rate_value = float(profit_value_withdraw_rate_var.get())
            
            profit_total_text = profit_value_sold_price_value + profit_value_shipping_value
            profit_final_value_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(12.55/100)) + 0.30
            profit_international_fee_text = ((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(1.3/100))
            profit_payoneer_fee_text = (((profit_value_sold_price_value + profit_value_shipping_value)-(((profit_value_sold_price_value + profit_value_shipping_value + profit_value_tax_value)*(13.85/100))+0.30))*2)/100

            profit_temp = profit_total_text - (profit_final_value_text + profit_international_fee_text + profit_payoneer_fee_text)
            profit_temp = float("{:.2f}".format(profit_temp))

            profit_value_text = (profit_temp * profit_withdraw_rate_value) - profit_tot_from_bank_value
            
            # If 3 values are 0 then maintain the value at 0
            if profit_value_sold_price_value == 0 and profit_value_shipping_value == 0 and profit_value_tax_value == 0 and profit_withdraw_rate_value == 0 and profit_tot_from_bank_value == 0:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.'+str("%.2f" % profit_value_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the profit_value value at '0'
        profit_value_text = profit_value_canvas.create_text(35,86 ,text='Rs.0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        profit_value_withdraw_rate_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        profit_value_withdraw_rate_error_label.place(x=365, y=96)

withdraw_rate_var.trace('w', lambda *args, withdraw_rate_var=withdraw_rate_var: profit_value_callback5(withdraw_rate_var))

### Final Value canvas
final_value_canvas = Canvas(canvas_output_frame, width = 205, height = 144, bg='#1f1f1f', highlightthickness=0)
final_value_canvas.grid(row=2, column=1, padx=(42,0), pady=(20,0))
final_value_image = Image.open('Canvas Shapes/2.1.png')
final_value_image = final_value_image.resize((184, 120), Image.ANTIALIAS)
final_value_image_img = ImageTk.PhotoImage(final_value_image)
final_value_canvas.create_image(96,75, image=final_value_image_img)

# Create a before text
final_value_text = final_value_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))

#Black Label
final_value_sold_price_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def final_value_callback1(final_value_sold_price_var):
    global final_value_text
    final_value_canvas.delete(final_value_text)

    global final_value_sold_price_error_label
    final_value_sold_price_error_label.destroy()

    # Check received text int or str
    try:
        if final_value_sold_price_var.get() == '' or type(float(final_value_sold_price_var.get())) == float:

            # Check final_value_sold_price_var
            if final_value_sold_price_var.get() == '':
                final_value_sold_price_value = 0
            else:
                final_value_sold_price_value = float(final_value_sold_price_var.get())
            
            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                final_value_shipping_value = 0
            else:
                final_value_shipping_value = float(ebay_shipping_cost_var.get())

            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                final_value_tax_value = 0
            else:
                final_value_tax_value = float(ebay_tax_amount_var.get())
            
            final_value_text = ((final_value_sold_price_value + final_value_shipping_value + final_value_tax_value)*(12.55/100)) + 0.30
            
            # If 3 values are 0 then maintain the value at 0
            if final_value_sold_price_value == 0 and final_value_shipping_value == 0 and final_value_tax_value == 0:
                final_value_text = final_value_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                final_value_text = final_value_canvas.create_text(35,86 ,text='$'+str("%.2f" % final_value_text), anchor=W, fill='white', font=('Gelion Black', 21))
   
    except Exception:
        # Maintaining the final_value value at '0'
        final_value_text = final_value_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        final_value_sold_price_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        final_value_sold_price_error_label.place(x=365, y=26)

ebay_sold_price_without_tax_var.trace('w', lambda *args, ebay_sold_price_without_tax_var=ebay_sold_price_without_tax_var: final_value_callback1(ebay_sold_price_without_tax_var))

# Blank Label
final_value_shipping_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def final_value_callback2(final_value_shipping_var):
    global final_value_text
    final_value_canvas.delete(final_value_text)

    global final_value_shipping_error_label
    final_value_shipping_error_label.destroy()

    try:
        if final_value_shipping_var.get() == '' or type(float(final_value_shipping_var.get())) == float:
            # Check final_value_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                final_value_sold_price_value = 0
            else:
                final_value_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if final_value_shipping_var.get() == '':
                final_value_shipping_value = 0
            else:
                final_value_shipping_value = float(final_value_shipping_var.get())
            
            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                final_value_tax_value = 0
            else:
                final_value_tax_value = float(ebay_tax_amount_var.get())
            
            #final_value_text = final_value_sold_price_value + final_value_shipping_value + final_value_tax_value
            final_value_text = ((final_value_sold_price_value + final_value_shipping_value + final_value_tax_value)*(12.55/100)) + 0.30

            # If 3 values are 0 then maintain the value at 0
            if final_value_sold_price_value == 0 and final_value_shipping_value == 0 and final_value_tax_value == 0:
                final_value_text = final_value_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                final_value_text = final_value_canvas.create_text(35,86 ,text='$'+str("%.2f" % final_value_text), anchor=W, fill='white', font=('Gelion Black', 21))


    except Exception:
        # Maintaining the final_value value at '0'
        final_value_text = final_value_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        final_value_shipping_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        final_value_shipping_error_label.place(x=365, y=61)

ebay_shipping_cost_var.trace('w', lambda *args, ebay_shipping_cost_var=ebay_shipping_cost_var: final_value_callback2(ebay_shipping_cost_var))

# Blank Label
final_value_tax_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for tax variable
def final_value_callback3(final_value_tax_var):
    global final_value_text
    final_value_canvas.delete(final_value_text)

    global final_value_tax_error_label
    final_value_tax_error_label.destroy()

    try:
        if final_value_tax_var.get() == '' or type(float(final_value_tax_var.get())) == float:
            # Check final_value_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                final_value_sold_price_value = 0
            else:
                final_value_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                final_value_shipping_value = 0
            else:
                final_value_shipping_value = float(ebay_shipping_cost_var.get())
            
            # Check ebay_tax_amount_var
            if final_value_tax_var.get() == '':
                final_value_tax_value = 0
            else:
                final_value_tax_value = float(final_value_tax_var.get())
            
            final_value_text = ((final_value_sold_price_value + final_value_shipping_value + final_value_tax_value)*(12.55/100)) + 0.30
            
            # If 3 values are 0 then maintain the value at 0
            if final_value_sold_price_value == 0 and final_value_shipping_value == 0 and final_value_tax_value == 0:
                final_value_text = final_value_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                final_value_text = final_value_canvas.create_text(35,86 ,text='$'+str("%.2f" % final_value_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the final_value value at '0'
        final_value_text = final_value_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        final_value_tax_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        final_value_tax_error_label.place(x=365, y=96)

ebay_tax_amount_var.trace('w', lambda *args, ebay_tax_amount_var=ebay_tax_amount_var: final_value_callback3(ebay_tax_amount_var))


##################################################################################################################################################

### International Fee canvas
international_fee_canvas = Canvas(canvas_output_frame, width = 205, height = 144, bg='#1f1f1f', highlightthickness=0)
international_fee_canvas.grid(row=2, column=2, padx=(20,0), pady=(20,0))
international_fee_image = Image.open('Canvas Shapes/2.2.png')
international_fee_image = international_fee_image.resize((184, 120), Image.ANTIALIAS)
international_fee_image_img = ImageTk.PhotoImage(international_fee_image)
international_fee_canvas.create_image(96,75, image=international_fee_image_img)

# Create a before text
international_fee_text = international_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))

#Black Label
international_fee_sold_price_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def international_fee_callback1(international_fee_sold_price_var):
    global international_fee_text
    international_fee_canvas.delete(international_fee_text)

    global international_fee_sold_price_error_label
    international_fee_sold_price_error_label.destroy()

    # Check received text int or str
    try:
        if international_fee_sold_price_var.get() == '' or type(float(international_fee_sold_price_var.get())) == float:

            # Check international_fee_var
            if international_fee_sold_price_var.get() == '':
                international_fee_sold_price_value = 0
            else:
                international_fee_sold_price_value = float(international_fee_sold_price_var.get())
            
            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                international_fee_shipping_value = 0
            else:
                international_fee_shipping_value = float(ebay_shipping_cost_var.get())

            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                international_fee_tax_value = 0
            else:
                international_fee_tax_value = float(ebay_tax_amount_var.get())
            
            international_fee_text = ((international_fee_sold_price_value + international_fee_shipping_value + international_fee_tax_value)*(1.3/100))
            
            # If 3 values are 0 then maintain the value at 0
            if international_fee_sold_price_value == 0 and international_fee_shipping_value == 0 and international_fee_tax_value == 0:
                international_fee_text = international_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                international_fee_text = international_fee_canvas.create_text(35,86 ,text='$'+str("%.2f" % international_fee_text), anchor=W, fill='white', font=('Gelion Black', 21))
   
    except Exception:
        # Maintaining the international_fee value at '0'
        international_fee_text = international_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        international_fee_sold_price_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        international_fee_sold_price_error_label.place(x=365, y=26)

ebay_sold_price_without_tax_var.trace('w', lambda *args, ebay_sold_price_without_tax_var=ebay_sold_price_without_tax_var: international_fee_callback1(ebay_sold_price_without_tax_var))

# Blank Label
international_fee_shipping_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def international_fee_callback2(international_fee_shipping_var):
    global international_fee_text
    international_fee_canvas.delete(international_fee_text)

    global international_fee_shipping_error_label
    international_fee_shipping_error_label.destroy()

    try:
        if international_fee_shipping_var.get() == '' or type(float(international_fee_shipping_var.get())) == float:
            # Check international_fee_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                international_fee_sold_price_value = 0
            else:
                international_fee_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if international_fee_shipping_var.get() == '':
                international_fee_shipping_value = 0
            else:
                international_fee_shipping_value = float(international_fee_shipping_var.get())
            
            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                international_fee_tax_value = 0
            else:
                international_fee_tax_value = float(ebay_tax_amount_var.get())
            
            #international_fee_text = international_fee_sold_price_value + international_fee_shipping_value + international_fee_tax_value
            international_fee_text = ((international_fee_sold_price_value + international_fee_shipping_value + international_fee_tax_value)*(1.3/100))

            # If 3 values are 0 then maintain the value at 0
            if international_fee_sold_price_value == 0 and international_fee_shipping_value == 0 and international_fee_tax_value == 0:
                international_fee_text = international_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                international_fee_text = international_fee_canvas.create_text(35,86 ,text='$'+str("%.2f" % international_fee_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the international_fee value at '0'
        international_fee_text = international_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        international_fee_shipping_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        international_fee_shipping_error_label.place(x=365, y=61)

ebay_shipping_cost_var.trace('w', lambda *args, ebay_shipping_cost_var=ebay_shipping_cost_var: international_fee_callback2(ebay_shipping_cost_var))

# Blank Label
international_fee_tax_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for tax variable
def international_fee_callback3(international_fee_tax_var):
    global international_fee_text
    international_fee_canvas.delete(international_fee_text)

    global international_fee_tax_error_label
    international_fee_tax_error_label.destroy()

    try:
        if international_fee_tax_var.get() == '' or type(float(international_fee_tax_var.get())) == float:
            # Check international_fee_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                international_fee_sold_price_value = 0
            else:
                international_fee_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                international_fee_shipping_value = 0
            else:
                international_fee_shipping_value = float(ebay_shipping_cost_var.get())
            
            # Check ebay_tax_amount_var
            if international_fee_tax_var.get() == '':
                international_fee_tax_value = 0
            else:
                international_fee_tax_value = float(international_fee_tax_var.get())
            
            international_fee_text = ((international_fee_sold_price_value + international_fee_shipping_value + international_fee_tax_value)*(1.3/100))
            
            # If 3 values are 0 then maintain the value at 0
            if international_fee_sold_price_value == 0 and international_fee_shipping_value == 0 and international_fee_tax_value == 0:
                international_fee_text = international_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                international_fee_text = international_fee_canvas.create_text(35,86 ,text='$'+str("%.2f" % international_fee_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the international_fee value at '0'
        international_fee_text = international_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        international_fee_tax_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        international_fee_tax_error_label.place(x=365, y=96)

ebay_tax_amount_var.trace('w', lambda *args, ebay_tax_amount_var=ebay_tax_amount_var: international_fee_callback3(ebay_tax_amount_var))

### Paynoeer Withdrawal Fee canvas
payoneer_fee_canvas = Canvas(canvas_output_frame, width = 205, height = 144, bg='#1f1f1f', highlightthickness=0)
payoneer_fee_canvas.grid(row=3, column=1, padx=(42,0), pady=(20,0))
payoneer_fee_image = Image.open('Canvas Shapes/3.1.png')
payoneer_fee_image = payoneer_fee_image.resize((184, 120), Image.ANTIALIAS)
payoneer_fee_image_img = ImageTk.PhotoImage(payoneer_fee_image)
payoneer_fee_canvas.create_image(96,75, image=payoneer_fee_image_img)

# Create a before text
payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))

#Black Label
payoneer_fee_sold_price_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def payoneer_fee_callback1(payoneer_fee_sold_price_var):
    global payoneer_fee_text
    payoneer_fee_canvas.delete(payoneer_fee_text)

    global payoneer_fee_sold_price_error_label
    payoneer_fee_sold_price_error_label.destroy()

    # Check received text int or str
    try:
        if payoneer_fee_sold_price_var.get() == '' or type(float(payoneer_fee_sold_price_var.get())) == float:

            # Check payoneer_fee_var
            if payoneer_fee_sold_price_var.get() == '':
                payoneer_fee_sold_price_value = 0
            else:
                payoneer_fee_sold_price_value = float(payoneer_fee_sold_price_var.get())
            
            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                payoneer_fee_shipping_value = 0
            else:
                payoneer_fee_shipping_value = float(ebay_shipping_cost_var.get())

            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                payoneer_fee_tax_value = 0
            else:
                payoneer_fee_tax_value = float(ebay_tax_amount_var.get())
            
            payoneer_fee_text = (((payoneer_fee_sold_price_value + payoneer_fee_shipping_value)-(((payoneer_fee_sold_price_value + payoneer_fee_shipping_value + payoneer_fee_tax_value)*(13.85/100))+0.30))*2)/100
            
            # If 3 values are 0 then maintain the value at 0
            if payoneer_fee_sold_price_value == 0 and payoneer_fee_shipping_value == 0 and payoneer_fee_tax_value == 0:
                payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$'+str("%.2f" % payoneer_fee_text), anchor=W, fill='white', font=('Gelion Black', 21))
   
    except Exception:
        # Maintaining the payoneer_fee value at '0'
        payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        payoneer_fee_sold_price_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        payoneer_fee_sold_price_error_label.place(x=365, y=26)

ebay_sold_price_without_tax_var.trace('w', lambda *args, ebay_sold_price_without_tax_var=ebay_sold_price_without_tax_var: payoneer_fee_callback1(ebay_sold_price_without_tax_var))

# Blank Label
payoneer_fee_shipping_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def payoneer_fee_callback2(payoneer_fee_shipping_var):
    global payoneer_fee_text
    payoneer_fee_canvas.delete(payoneer_fee_text)

    global payoneer_fee_shipping_error_label
    payoneer_fee_shipping_error_label.destroy()

    try:
        if payoneer_fee_shipping_var.get() == '' or type(float(payoneer_fee_shipping_var.get())) == float:
            # Check payoneer_fee_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                payoneer_fee_sold_price_value = 0
            else:
                payoneer_fee_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if payoneer_fee_shipping_var.get() == '':
                payoneer_fee_shipping_value = 0
            else:
                payoneer_fee_shipping_value = float(payoneer_fee_shipping_var.get())
            
            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                payoneer_fee_tax_value = 0
            else:
                payoneer_fee_tax_value = float(ebay_tax_amount_var.get())
            
            #payoneer_fee_text = payoneer_fee_sold_price_value + payoneer_fee_shipping_value + payoneer_fee_tax_value
            payoneer_fee_text = (((payoneer_fee_sold_price_value + payoneer_fee_shipping_value)-(((payoneer_fee_sold_price_value + payoneer_fee_shipping_value + payoneer_fee_tax_value)*(13.85/100))+0.30))*2)/100

            # If 3 values are 0 then maintain the value at 0
            if payoneer_fee_sold_price_value == 0 and payoneer_fee_shipping_value == 0 and payoneer_fee_tax_value == 0:
                payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$'+str("%.2f" % payoneer_fee_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the payoneer_fee value at '0'
        payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        payoneer_fee_shipping_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        payoneer_fee_shipping_error_label.place(x=365, y=61)

ebay_shipping_cost_var.trace('w', lambda *args, ebay_shipping_cost_var=ebay_shipping_cost_var: payoneer_fee_callback2(ebay_shipping_cost_var))

# Blank Label
payoneer_fee_tax_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for tax variable
def payoneer_fee_callback3(payoneer_fee_tax_var):
    global payoneer_fee_text
    payoneer_fee_canvas.delete(payoneer_fee_text)

    global payoneer_fee_tax_error_label
    payoneer_fee_tax_error_label.destroy()

    try:
        if payoneer_fee_tax_var.get() == '' or type(float(payoneer_fee_tax_var.get())) == float:
            # Check payoneer_fee_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                payoneer_fee_sold_price_value = 0
            else:
                payoneer_fee_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                payoneer_fee_shipping_value = 0
            else:
                payoneer_fee_shipping_value = float(ebay_shipping_cost_var.get())
            
            # Check ebay_tax_amount_var
            if payoneer_fee_tax_var.get() == '':
                payoneer_fee_tax_value = 0
            else:
                payoneer_fee_tax_value = float(payoneer_fee_tax_var.get())
            
            payoneer_fee_text = (((payoneer_fee_sold_price_value + payoneer_fee_shipping_value)-(((payoneer_fee_sold_price_value + payoneer_fee_shipping_value + payoneer_fee_tax_value)*(13.85/100))+0.30))*2)/100
            
            # If 3 values are 0 then maintain the value at 0
            if payoneer_fee_sold_price_value == 0 and payoneer_fee_shipping_value == 0 and payoneer_fee_tax_value == 0:
                payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$'+str("%.2f" % payoneer_fee_text), anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the payoneer_fee value at '0'
        payoneer_fee_text = payoneer_fee_canvas.create_text(35,86 ,text='$0', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        payoneer_fee_tax_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        payoneer_fee_tax_error_label.place(x=365, y=96)

ebay_tax_amount_var.trace('w', lambda *args, ebay_tax_amount_var=ebay_tax_amount_var: payoneer_fee_callback3(ebay_tax_amount_var))



### International Fee canvas
tax_rate_canvas = Canvas(canvas_output_frame, width = 205, height = 144, bg='#1f1f1f', highlightthickness=0)
tax_rate_canvas.grid(row=3, column=2, padx=(20,0), pady=(20,0))
tax_rate_image = Image.open('Canvas Shapes/3.2.png')
tax_rate_image = tax_rate_image.resize((184, 120), Image.ANTIALIAS)
tax_rate_image_img = ImageTk.PhotoImage(tax_rate_image)
tax_rate_canvas.create_image(96,75, image=tax_rate_image_img)

# Create a before text
tax_rate_text = tax_rate_canvas.create_text(35,86 ,text='0 %', anchor=W, fill='white', font=('Gelion Black', 21))

#Black Label
tax_rate_sold_price_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def tax_rate_callback1(tax_rate_sold_price_var):
    global tax_rate_text
    tax_rate_canvas.delete(tax_rate_text)

    global tax_rate_sold_price_error_label
    tax_rate_sold_price_error_label.destroy()

    # Check received text int or str
    try:
        if tax_rate_sold_price_var.get() == '' or type(float(tax_rate_sold_price_var.get())) == float:

            # Check tax_rate_var
            if tax_rate_sold_price_var.get() == '':
                tax_rate_sold_price_value = 1
            else:
                tax_rate_sold_price_value = float(tax_rate_sold_price_var.get())
            
            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                tax_rate_shipping_value = 1
            else:
                tax_rate_shipping_value = float(ebay_shipping_cost_var.get())

            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                tax_rate_tax_value = 0
            else:
                tax_rate_tax_value = float(ebay_tax_amount_var.get())
            
            #tax_rate_text = ((tax_rate_sold_price_value + tax_rate_shipping_value + tax_rate_tax_value)*(1.8/100))
            tax_rate_text = (tax_rate_tax_value/(tax_rate_sold_price_value + tax_rate_shipping_value))*100
            
            # If 'sold_price_value' and 'shipping_value' values are 1 then maintain the value at 0
            if tax_rate_sold_price_value == 1 and tax_rate_shipping_value == 1:
                tax_rate_text = tax_rate_canvas.create_text(35,86 ,text='0 %', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                tax_rate_text = tax_rate_canvas.create_text(35,86 ,text=str("%.2f" % tax_rate_text) + ' %', anchor=W, fill='white', font=('Gelion Black', 21))
   
    except Exception:
        # Maintaining the tax_rate value at '0'
        tax_rate_text = tax_rate_canvas.create_text(35,86 ,text='0 %', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        tax_rate_sold_price_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        tax_rate_sold_price_error_label.place(x=365, y=26)

ebay_sold_price_without_tax_var.trace('w', lambda *args, ebay_sold_price_without_tax_var=ebay_sold_price_without_tax_var: tax_rate_callback1(ebay_sold_price_without_tax_var))

# Blank Label
tax_rate_shipping_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for sold_price variable
def tax_rate_callback2(tax_rate_shipping_var):
    global tax_rate_text
    tax_rate_canvas.delete(tax_rate_text)

    global tax_rate_shipping_error_label
    tax_rate_shipping_error_label.destroy()

    try:
        if tax_rate_shipping_var.get() == '' or type(float(tax_rate_shipping_var.get())) == float:
            # Check tax_rate_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                tax_rate_sold_price_value = 1
            else:
                tax_rate_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if tax_rate_shipping_var.get() == '':
                tax_rate_shipping_value = 1
            else:
                tax_rate_shipping_value = float(tax_rate_shipping_var.get())
            
            # Check ebay_tax_amount_var
            if ebay_tax_amount_var.get() == '':
                tax_rate_tax_value = 0
            else:
                tax_rate_tax_value = float(ebay_tax_amount_var.get())
            
            #tax_rate_text = tax_rate_sold_price_value + tax_rate_shipping_value + tax_rate_tax_value
            tax_rate_text = (tax_rate_tax_value/(tax_rate_sold_price_value + tax_rate_shipping_value))*100

            # If 'sold_price_value' and 'shipping_value' values are 1 then maintain the value at 0
            if tax_rate_sold_price_value == 1 and tax_rate_shipping_value == 1:
                tax_rate_text = tax_rate_canvas.create_text(35,86 ,text='0 %', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                tax_rate_text = tax_rate_canvas.create_text(35,86 ,text=str("%.2f" % tax_rate_text) + ' %', anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the tax_rate value at '0'
        tax_rate_text = tax_rate_canvas.create_text(35,86 ,text='0 %', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        tax_rate_shipping_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        tax_rate_shipping_error_label.place(x=365, y=61)

ebay_shipping_cost_var.trace('w', lambda *args, ebay_shipping_cost_var=ebay_shipping_cost_var: tax_rate_callback2(ebay_shipping_cost_var))

# Blank Label
tax_rate_tax_error_label = Label(ebay_sold_details_label_frame.frame)

# Callback funtion for tax variable
def tax_rate_callback3(tax_rate_tax_var):
    global tax_rate_text
    tax_rate_canvas.delete(tax_rate_text)

    global tax_rate_tax_error_label
    tax_rate_tax_error_label.destroy()

    try:
        if tax_rate_tax_var.get() == '' or type(float(tax_rate_tax_var.get())) == float:
            # Check tax_rate_sold_price_var
            if ebay_sold_price_without_tax_var.get() == '':
                tax_rate_sold_price_value = 1
            else:
                tax_rate_sold_price_value = float(ebay_sold_price_without_tax_var.get())

            # Check ebay_shipping_cost_var
            if ebay_shipping_cost_var.get() == '':
                tax_rate_shipping_value = 1
            else:
                tax_rate_shipping_value = float(ebay_shipping_cost_var.get())
            
            # Check ebay_tax_amount_var
            if tax_rate_tax_var.get() == '':
                tax_rate_tax_value = 0
            else:
                tax_rate_tax_value = float(tax_rate_tax_var.get())
            
            tax_rate_text = (tax_rate_tax_value/(tax_rate_sold_price_value + tax_rate_shipping_value))*100
            
            # If 'sold_price_value' and 'shipping_value' values are 1 then maintain the value at 0
            if tax_rate_sold_price_value == 1 and tax_rate_shipping_value == 1:
                tax_rate_text = tax_rate_canvas.create_text(35,86 ,text='0 %', anchor=W, fill='white', font=('Gelion Black', 21))
            else:
                tax_rate_text = tax_rate_canvas.create_text(35,86 ,text=str("%.2f" % tax_rate_text) + ' %', anchor=W, fill='white', font=('Gelion Black', 21))

    except Exception:
        # Maintaining the tax_rate value at '0'
        tax_rate_text = tax_rate_canvas.create_text(35,86 ,text='0 %', anchor=W, fill='white', font=('Gelion Black', 21))
        # Display error
        tax_rate_tax_error_label = Label(ebay_sold_details_label_frame.frame, text='Please enter\nin correct data type',fg='red', bg='white', justify='left')
        tax_rate_tax_error_label.place(x=365, y=96)

ebay_tax_amount_var.trace('w', lambda *args, ebay_tax_amount_var=ebay_tax_amount_var: tax_rate_callback3(ebay_tax_amount_var))


root.mainloop()