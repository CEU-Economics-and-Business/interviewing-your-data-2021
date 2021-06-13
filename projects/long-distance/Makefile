data.csv: ../../data/ted/ted-can-2019.csv
	cat $< | \
	csvgrep -d, -c ISO_COUNTRY_CODE -r ".*---.*" -i | \
	csvgrep -d, -c WIN_COUNTRY_CODE -r ".*---.*" -i | \
	csvsql --query "select * from STDIN where not ISO_COUNTRY_CODE = WIN_COUNTRY_CODE" > \
	$@