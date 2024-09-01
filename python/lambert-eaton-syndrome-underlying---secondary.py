# phekb, 2024.

import sys, csv, re

codes = [{"code":"43530726","system":"ICD10CM"},{"code":"43531175","system":"ICD10CM"},{"code":"43531175","system":"ICD10CM"},{"code":"43530726","system":"ICD10CM"},{"code":"43530726","system":"ICD10CM"},{"code":"43531175","system":"ICD10CM"},{"code":"43531175","system":"ICD10CM"},{"code":"43530726","system":"ICD10CM"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lambert-eaton-syndrome-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lambert-eaton-syndrome-underlying---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lambert-eaton-syndrome-underlying---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lambert-eaton-syndrome-underlying---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
