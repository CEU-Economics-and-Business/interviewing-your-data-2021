all: 2014.csv 2015.csv 2016.csv 2017.csv 2018.csv 2019.csv
%.csv: ../../data/ted/ted-can-%.csv
	cat $< | \
	csvgrep -d, -c ISO_COUNTRY_CODE -r "(EE|LT|LV)" | \
	csvgrep -d, -c CPV -r "(72[0-9]{6}|221[4-5]0000|22462000|79340000|35730000|35811300)"  > \
	$@
