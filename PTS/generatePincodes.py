import random
import csv

num_records = 40000

with open('allPincodesList.csv', 'r') as f:
    reader = csv.reader(f)
    all_pincodes = [row[0] for row in reader]

random.shuffle(all_pincodes)

# Define dictionary mapping source and destination pin codes to delivery days
delivery_days = {
    # beg
    ("56", "11"): 3,
    ("56", "12"): 3,
    ("56", "13"): 3,
    ("56", "14"): 4,
    ("56", "15"): 4,
    ("56", "16"): 4,
    ("56", "17"): 4,
    ("56", "18"): 5,
    ("56", "19"): 5,
    ("56", "20"): 4,
    ("56", "21"): 4,
    ("56", "22"): 4,
    ("56", "23"): 4,
    ("56", "24"): 4,
    ("56", "25"): 4,
    ("56", "26"): 4,
    ("56", "27"): 4,
    ("56", "28"): 4,
    ("56", "30"): 4,
    ("56", "31"): 4,
    ("56", "32"): 4,
    ("56", "33"): 4,
    ("56", "34"): 4,
    ("56", "36"): 4,
    ("56", "37"): 4,
    ("56", "38"): 4,
    ("56", "39"): 4,
    ("56", "40"): 3,
    ("56", "41"): 3,
    ("56", "42"): 3,
    ("56", "43"): 3,
    ("56", "44"): 3,
    ("56", "45"): 3,
    ("56", "46"): 3,
    ("56", "47"): 3,
    ("56", "48"): 3,
    ("56", "49"): 3,
    ("56", "50"): 2,
    ("56", "51"): 2,
    ("56", "52"): 2,
    ("56", "53"): 2,
    ("56", "56"): 1,
    ("56", "57"): 2,
    ("56", "58"): 2,
    ("56", "59"): 2,
    ("56", "60"): 2,
    ("56", "61"): 2,
    ("56", "62"): 2,
    ("56", "63"): 2,
    ("56", "64"): 2,
    ("56", "67"): 3,
    ("56", "68"): 3,
    ("56", "69"): 3,
    ("56", "70"): 4,
    ("56", "71"): 4,
    ("56", "72"): 4,
    ("56", "73"): 4,
    ("56", "74"): 4,
    ("56", "75"): 4,
    ("56", "76"): 4,
    ("56", "77"): 4, 
    ("56", "78"): 5, 
    ("56", "79"): 6, 
    ("56", "80"): 4, 
    ("56", "81"): 4, 
    ("56", "82"): 4, 
    ("56", "83"): 4, 
    ("56", "84"): 4, 
    ("56", "85"): 4, 
}

with open('delivery_dataset.csv', 'a') as f:
    for i in range(num_records):
        source_pincodes = [p for p in all_pincodes]
        source_pincode = random.choice(source_pincodes)
        destination_pincodes = [p for p in all_pincodes]
        dest_pincode = random.choice(destination_pincodes)
        key = (source_pincode[:2], dest_pincode[:2])
        if key in delivery_days:
            num_days = delivery_days[key]
        else:
            num_days = random.randint(2, 6)
        f.write(f'{source_pincode},{dest_pincode},{num_days}\n')

# import csv

# # Open the input CSV file and create a reader object
# with open('sourcePincode.csv', 'r') as infile:
#     reader = csv.reader(infile)

#     # Extract the second column of each row
#     second_col_set = set()
#     for row in reader:
#         second_col_set.add(row[1])

# # Open the output CSV file and create a writer object
# with open('allPincodesList.csv', 'w', newline='') as outfile:
#     writer = csv.writer(outfile)

#     # Write the extracted second columns to the output file
#     for col in second_col_set:
#         writer.writerow([col])