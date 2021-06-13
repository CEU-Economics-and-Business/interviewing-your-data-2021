all: ted-can-2019.csv TED_data_information_v3.3.pdf
ted-can-2019.csv: 
	curl -sLo $@ "https://data.europa.eu/euodp/repository/ec/dg-grow/mapps/TED%202020/TED%20-%20Contract%20award%20notices%202019.csv"
TED_data_information_v3.3.pdf: TED_data_information_v3.3.pdf.gz
	gunzip $<
TED_data_information_v3.3.pdf.gz:
	curl -sLo $@ "https://data.europa.eu/euodp/repository/ec/dg-grow/mapps/TED%202020/TED(csv)_data_information_v3.3.pdf.gz"