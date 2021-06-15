from lxml import etree
import csv
import glob

NMSP = {'ted': 'http://publications.europa.eu/resource/schema/ted/R2.0.9/publication'}

fields = {
	'uri': '//ted:URI_DOC',
	'publication_date': '//ted:DATE_PUB',
	'buyer_name': '//ted:CONTRACTING_BODY//ted:OFFICIALNAME//text()',
	'buyer_address': '//ted:CONTRACTING_BODY//ted:ADDRESS//text()',
	'buyer_town': '//ted:CONTRACTING_BODY//ted:TOWN//text()',
	'buyer_country': '//ted:CONTRACTING_BODY//ted:COUNTRY//text()',
	'cpv': '//ted:CPV_MAIN/ted:CPV_CODE/@CODE',
	'amount': '//ted:VALUES/ted:VALUE[@TYPE="PROCUREMENT_TOTAL"]',
	'currency': '//ted:VALUES/ted:VALUE[@TYPE="PROCUREMENT_TOTAL"]/@CURRENCY',
	'contractor_name': '//ted:CONTRACTOR//ted:OFFICIALNAME//text()',
	'contractor_address': '//ted:CONTRACTOR//ted:ADDRESS//text()',
	'contractor_town': '//ted:CONTRACTOR//ted:TOWN//text()',
	'contractor_country': '//ted:CONTRACTOR//ted:COUNTRY//text()',
}

def list_of_xmls():
	return glob.glob('xml/*.xml')

def parse(fn):
	output = {}
	with open(fn, 'rt') as f:
		doc = etree.parse(f)
		for key in fields:
			lst = doc.xpath(fields[key], namespaces=NMSP)
			if lst:
				try:
					output[key] = '|'.join([str(item.text) for item in lst])
				except:
					output[key] = '|'.join([str(item) for item in lst])
	return output

if __name__ == '__main__':
	writer = csv.DictWriter(open('data.csv', 'wt'), fieldnames=list(fields.keys()))
	writer.writeheader()
	for fn in list_of_xmls():
		writer.writerow(parse(fn))
