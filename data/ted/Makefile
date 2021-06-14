YEARS = 2014 2015 2016 2017 2018 2019
all: $(foreach year,$(YEARS),ted-can-$(year).csv) TED_data_information_v3.3.pdf
ted-can-%.csv: 
	curl -sLo $@ "https://data.europa.eu/euodp/repository/ec/dg-grow/mapps/TED%202020/TED%20-%20Contract%20award%20notices%20$*.csv"
TED_data_information_v3.3.pdf: TED_data_information_v3.3.pdf.gz
	gunzip $<
TED_data_information_v3.3.pdf.gz:
	curl -sLo $@ "https://data.europa.eu/euodp/repository/ec/dg-grow/mapps/TED%202020/TED(csv)_data_information_v3.3.pdf.gz"