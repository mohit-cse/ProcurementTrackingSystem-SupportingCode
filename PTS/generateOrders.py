import random
import csv
from datetime import datetime, timedelta

# Define the range of user IDs
user_ids = range(2, 109)

# Define the range of product IDs
product_ids = range(1, 31)

# Define the range of order times
start_date = datetime(2023, 3, 1)
end_date = datetime(2023, 3, 31)
delta = end_date - start_date

# Define a dictionary of Indian cities and their pin codes
# Define a dictionary of Indian states and cities with pin codes
indian_cities = {
    'Andhra Pradesh': {'Visakhapatnam': 530001, 'Vijayawada': 520001, 'Guntur': 522001},
    'Arunachal Pradesh': {'Itanagar': 791111, 'Naharlagun': 791110, 'Pasighat': 791102},
    'Assam': {'Guwahati': 781001, 'Silchar': 788001, 'Dibrugarh': 786001},
    'Bihar': {'Patna': 800001, 'Gaya': 823001, 'Bhagalpur': 812001},
    'Chhattisgarh': {'Raipur': 492001, 'Bhilai': 490001, 'Durg': 491001},
    'Goa': {'Panaji': 403001, 'Mapusa': 403507, 'Margao': 403601},
    'Gujarat': {'Ahmedabad': 380001, 'Surat': 395001, 'Vadodara': 390001},
    'Haryana': {'Gurgaon': 122001, 'Faridabad': 121001, 'Panipat': 132103},
    'Himachal Pradesh': {'Shimla': 171001, 'Mandi': 175001, 'Dharamshala': 176215},
    'Jharkhand': {'Ranchi': 834001, 'Jamshedpur': 831001, 'Dhanbad': 826001},
    'Karnataka': {'Bengaluru': 560001, 'Mangalore': 575001, 'Hubli': 580020},
    'Kerala': {'Thiruvananthapuram': 695001, 'Kochi': 682001, 'Kozhikode': 673001},
    'Madhya Pradesh': {'Bhopal': 462001, 'Indore': 452001, 'Gwalior': 474001},
    'Maharashtra': {'Mumbai': 400001, 'Pune': 411001, 'Nagpur': 440001},
    'Manipur': {'Imphal': 795001, 'Thoubal': 795138, 'Bishnupur': 795126},
    'Meghalaya': {'Shillong': 793001, 'Jowai': 793150, 'Tura': 794101},
    'Mizoram': {'Aizawl': 796001, 'Lunglei': 796701, 'Champhai': 796321},
    'Nagaland': {'Kohima': 797001, 'Dimapur': 797112, 'Mokokchung': 798601},
    'Odisha': {'Bhubaneswar': 751001, 'Cuttack': 753001, 'Rourkela': 769001},
    'Punjab': {'Ludhiana': 141001, 'Amritsar': 143001, 'Jalandhar': 144001},
    'Rajasthan': {'Jaipur': 302001, 'Jodhpur': 342001, 'Udaipur': 313001},
    'Sikkim': {'Gangtok': 737101, 'Namchi': 737126, 'Mangan': 737116},
    'Tamil Nadu': {'Chennai': 600001, 'Coimbatore': 641001, 'Madurai': 625001},
    'Telangana': {'Hyderabad': 500001, 'Warangal': 506002, 'Nizamabad': 503001},
    'Tripura': {'Agartala': 799001, 'Udaipur': 799105, 'Dharmanagar': 799250},
    'Uttar Pradesh': {'Lucknow': 226001, 'Kanpur': 208001, 'Agra': 282001},
    'Uttarakhand': {'Dehradun': 248001, 'Haridwar': 249401, 'Nainital': 263001},
    'West Bengal': {'Kolkata': 700001, 'Howrah': 711101, 'Asansol': 713301}
}
components = ['Green', 'Red', 'Blue', 'Gold', 'Silver', 'Platinum', 'Sapphire', 'Diamond', 'Ruby', 'Emerald', 'Pearl', 'Topaz', 'Crystal', 'Coral', 'Ocean', 'Sky', 'Star', 'Moon', 'Sun', 'Garden', 'Meadow', 'Park', 'Lake', 'River', 'Hill', 'Valley', 'Tower', 'Castle', 'Mansion', 'Palace', 'Plaza', 'Terrace', 'Grove', 'Oasis', 'Horizon', 'Serenity', 'Harmony', 'Vista', 'Crest', 'Summit', 'Peak', 'Pinnacle', 'Infinity', 'Eternity']

buildings = []

for i in range(1000):
    building_name = random.choice(components) + ' ' + random.choice(components)
    buildings.append(building_name)

streets = ['Main', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth', 'Thirteenth', 'Fourteenth', 'Fifteenth', 'Sixteenth', 'Seventeenth', 'Eighteenth', 'Nineteenth', 'Twentieth', 'Twenty-First', 'Twenty-Second', 'Twenty-Third', 'Twenty-Fourth', 'Twenty-Fifth', 'Twenty-Sixth', 'Twenty-Seventh', 'Twenty-Eighth', 'Twenty-Ninth', 'Thirtieth']


# Generate the dataset
data = []
for i in range(300):
    user_id = random.choice(user_ids)
    num_products = random.randint(1, 6)
    products = random.sample(product_ids, num_products)
    order_time = start_date + timedelta(seconds=random.randint(0, delta.total_seconds()))
    state = random.choice(list(indian_cities.keys()))
    city = random.choice(list(indian_cities[state].keys()))
    pincode = indian_cities[state][city]
    address = f"Flat {random.randint(101, 501)}, {random.choice(buildings)}, " \
                f"{random.choice(streets) + ' Street'}" 
    data.append((user_id, products, order_time.strftime("%Y-%m-%d %H:%M:%S"), address, state, city, pincode))

with open('orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['user_id', 'product_id', 'order_time', 'address', 'state', 'city','pincode'])
    writer.writerows(data)