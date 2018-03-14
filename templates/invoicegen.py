import numpy as np
from sklearn.utils import resample
from datetime import datetime
import random
import string

def create_invoice(content):

    items = ['Water','Tea','Coffee',
         'Amazon Echo',' Instant Pot 7-in-1 Multi-Functional Pressure Cooker',
         'TechMatte MagGrip Air Vent Magnetic Universal Car Mount','SanDisk 32GB Ultra Class Memory Card',
        'Sony XB950B1 Extra Bass Wireless Headphones','iRobot Roomba 652 Robotic Vacuum Cleaner',
        'Anker Bluetooth SoundBuds Headphones','Kindle Paperwhite','Fire TV Stick with Alexa Voice Remote',
         'Oral-B Pro 7000 SmartSeries Electric Toothbrush',
         'TaoTronics Dimmable LED Desk Lamp with USB Charging Port','23andMe DNA Test','NVIDIA Tesla K80 GPU',
         'NVIDIA TITAN V VOLTA 12GB HBM2 VIDEO CARD','Equinox Down Alternative Comforter',
         'Anker Super Bright Tactical Flashlight, Rechargeable', 'Cucisina Lemon Squeezer',
         'Fengbao 2PCS Kitchen Sink Strainer - Stainless Steel','ZIONOR Lagopus Ski Snowboard Goggles',
         'BIC Marking Permanent Marker, Metallic','2-in-1 Pet Glove: Grooming Tool + Furniture Pet Hair Remover',
         'Criacr Bluetooth FM Transmitter, Wireless In-Car FM Transmitter','Get Out [Blu-ray]',
         'Car Charger for Nintendo Switch','JETech 2-Pack iPhone 8/7 Screen Protector']

    companies = []

    co = {'NAME':'Ortec Finance Big Data Analytics B.V.',
          'STREET':'Boompjes 40',
          'POST':'3011XB',
          'CITY':'Rotterdam',
          'KVKNR':'70498032',
          'VATNR':'000038761017',
          'BANK':'RABOBANK',
          'BIC':'RABONL2U',
          'IBAN':'NL97RABO0167773583',
          'PHONE':'06-98486335',
          'EMAIL':'info@ofdataanalytics.com',
          'WEB':'http://ofdataanalytics.com/'}

    companies.append(co)

    co = {'NAME':'ORTEC Finance B.V.',
          'STREET':'Boompjes 40',
          'POST':'3011XB',
          'CITY':'Rotterdam',
          'KVKNR':'24421148',
          'VATNR':'000019986750',
          'BANK':'RABOBANK',
          'BIC':'RABONL2U',
          'IBAN':'NL35RABO0386025669',
          'PHONE':'06-90366060',
          'EMAIL':'info@ortec-finance.com',
          'WEB':'http://www.ortec-finance.com/nl-nl'}

    companies.append(co)

    co = {'NAME':'ING Bank N.V.',
          'STREET':'Bijlmerplein 888',
          'POST':'1102MG',
          'CITY':'Amsterdam',
          'KVKNR':'33031431',
          'VATNR':'000019531656',
          'BANK':'ING NETHERLANDS',
          'BIC':'INGBNL2A',
          'IBAN':'NL12INGB0758162765',
          'PHONE':'06-90366060',
          'EMAIL':'info@ing.nl',
          'WEB':'https://www.ing.nl'}

    companies.append(co)

    co = {'NAME':'Amazon NL International Holdings B.V.',
          'STREET':'Johanna Westerdijkplein 1',
          'POST':'2521EN',
          'CITY':'s-Gravenhage',
          'KVKNR':'69988978',
          'VATNR':'000038299550',
          'BANK':'RABOBANK',
          'BIC':'RABONL2U',
          'IBAN':'NL41RABO0150437878',
          'PHONE':'06-35829070',
          'EMAIL':'info@amazon.com',
          'WEB':'https://www.amazon.com'}

    companies.append(co)

    co = {'NAME':'Unilever Nederland',
          'STREET':'Nassaukade 5',
          'POST':'3071JL',
          'CITY':'Rotterdam',
          'KVKNR':'24269393',
          'VATNR':'000019267231',
          'BANK':'ING NETHERLANDS',
          'BIC':'INGBNL2A',
          'IBAN':'NL02INGB0681309748',
          'PHONE':'06-88163931',
          'EMAIL':'info@unilever.com',
          'WEB':'https://www.unilever.com'}


    companies.append(co)

    conditions = ['Payable within 30 days','Delivery after payment','']

    bill_items = resample(items,n_samples=4,replace=False)
    prices = np.random.rand(4)*1000
    quants = np.random.randint(1,10,size=4)
    totals = prices * quants
    vat_s = totals * 0.12 # 12% vat on everything
    total_vat = np.sum(vat_s)
    total_wo_vat = np.sum(totals)
    total = total_vat + total_wo_vat

    for i in range(4):
        item_name = bill_items[i]
        item_quant = quants[i]
        item_price = prices[i]
        item_vat = vat_s[i]
        item_total = totals[i]
        content = content.replace('<ITEM_{}_NAME>'.format(i+1),item_name)

        content = content.replace('<ITEM_{}_QUANT>'.format(i+1),"{0:.2f}".format(item_quant))

        content = content.replace('<ITEM_{}_PRICE>'.format(i+1),"{0:.2f}".format(item_price))

        content = content.replace('<ITEM_{}_VAT>'.format(i+1),"{0:.2f}".format(item_vat))

        content = content.replace('<ITEM_{}_TOTAL>'.format(i+1),"{0:.2f}".format(item_total))

    content = content.replace('<TOTAL_WO_VAT>',"{0:.2f}".format(total_wo_vat))
    content = content.replace('<TOTAL_VAT>',"{0:.2f}".format(total_vat))
    content = content.replace('<TOTAL>',"{0:.2f}".format(total))
    sender, reciever = resample(companies, n_samples=2,replace=False)

    content = content.replace('<SENDER_NAME>',sender['NAME'])
    content = content.replace('<SENDER_STREET>',sender['STREET'])
    content = content.replace('<SENDER_POST>',sender['POST'])
    content = content.replace('<SENDER_CITY>',sender['POST'])
    content = content.replace('<KVKNR>',sender['KVKNR'])
    content = content.replace('<VATNR>',sender['VATNR'])
    content = content.replace('<BANK_NAME>',sender['BANK'])
    content = content.replace('<IBAN>',sender['IBAN'])
    content = content.replace('<BIC_CODE>',sender['BIC'])
    content = content.replace('<PHONE>',sender['PHONE'])
    content = content.replace('<EMAIL>',sender['EMAIL'])
    content = content.replace('<WEBSITE>',sender['WEB'])
    content = content.replace('<RECIPIENT_NAME>',reciever['NAME'])
    content = content.replace('<RECIPIENT_STREET>',reciever['STREET'])
    content = content.replace('<RECIPIENT_POST>',reciever['POST'])
    content = content.replace('<RECIPIENT_CITY>',reciever['CITY'])

    year = random.randint(2008, 2017)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    date = '{}/{}/{}'.format(day,month,year)

    content = content.replace('<INVOICE_DATE>',date)

    if month < 12:
        month += 1
    else:
        month = 1

    due = '{}/{}/{}'.format(day,month,year)

    content = content.replace('<DUE_DATE>',due)

    reference = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    invoice_no = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

    content = content.replace('<CUSTOMER_REFERENCE>',reference)
    content = content.replace('<INVOICE_NR>',invoice_no)

    condition = resample(conditions, n_samples = 1)[0]
    content = content.replace('<CONDITION>',condition)

    target = [0]* len(content)

    sn_start = content.find(sender['NAME'])
    sn_len = len(sender['NAME'])
    sn_end = sn_start + sn_len

    target[sn_start:sn_end] = [1]*sn_len

    skvk_start = content.find(sender['KVKNR'])
    skvk_len = len(sender['KVKNR'])
    skvk_end = skvk_start + skvk_len

    target[skvk_start:skvk_end] = [2]*skvk_len

    siban_start = content.find(sender['IBAN'])
    siban_len = len(sender['IBAN'])
    siban_end = siban_start + siban_len

    target[siban_start:siban_end] = [3]*siban_len

    ref_start = content.find(reference)
    ref_len = len(reference)
    ref_end = ref_start + ref_len

    target[ref_start:ref_end] = [4]*ref_len

    total_start = content.find("{0:.2f}".format(total))
    total_len = len("{0:.2f}".format(total))
    total_end = total_start + total_len

    target[total_start:total_end] = [5]*total_len

    return content, target
