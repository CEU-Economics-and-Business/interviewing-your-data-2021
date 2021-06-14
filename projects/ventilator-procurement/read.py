from lxml import etree
import csv
import glob

NMSP = {'ted': 'http://publications.europa.eu/resource/schema/ted/R2.0.9/publication'}

fields = {
	'uri': '//ted:URI_DOC',
	'publication_date': '//ted:DATE_PUB',
	'buyer': '//ted:CONTRACTING_BODY//text()',
	'cpv': '//ted:CPV_MAIN/ted:CPV_CODE/@CODE',
	'amount': '//ted:VALUES/ted:VALUE[@TYPE="PROCUREMENT_TOTAL"]',
	'currency': '//ted:VALUES/ted:VALUE[@TYPE="PROCUREMENT_TOTAL"]/@CURRENCY',
	'contractors': '//ted:CONTRACTOR//text()'
	}

def list_of_xmls():
	return glob.glob('*.xml')

def parse(fn):
	output = {}
	with open(fn, 'rt') as f:
		doc = etree.parse(f)
		for key in fields:
			lst = doc.xpath(fields[key], namespaces=NMSP)
			if lst:
				try:
					output[key] = ', '.join([str(item.text) for item in lst])
				except:
					output[key] = ', '.join([str(item) for item in lst])
	return output

if __name__ == '__main__':
	writer = csv.DictWriter(open('data.csv', 'wt'), fieldnames=list(fields.keys()))
	writer.writeheader()
	for fn in list_of_xmls():
		writer.writerow(parse(fn))