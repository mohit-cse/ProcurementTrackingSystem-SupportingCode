import csv,datetime
import os
from sqlalchemy import create_engine,text
from test_model import getNumberOfDays

db_connection_string=os.environ['DB_CONN_STR']

engine = create_engine(db_connection_string,connect_args={
    "ssl":{
        "ssl_ca":"/etc/ssl/cert.pem"
    }
})

conn=engine.connect()
def add_data():
    # get the full path to the CSV file
    with open("E:\Final year project\Procurement Tracking System\orders.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip the header row
        for row in reader:
            # insert the row into the orders_1 table
            result=conn.execute(text("insert into orders(user_id, product_id, order_time, address, state, city, pincode) values(:user_id,:product_id,:order_time,:address,:state,:city,:pincode)").bindparams(user_id=int(row[0]),product_id=row[1],order_time=row[2],address=row[3],state=row[4],city=row[5],pincode=int(row[6])))
            number_of_days=getNumberOfDays(row[6])
            date_obj = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            new_date_obj = date_obj + datetime.timedelta(days=number_of_days)
            expected_delivery = new_date_obj.strftime('%Y-%m-%d')
            order_status_result=conn.execute(text("insert into order_status(order_id,status,expected_delivery,delivered_on) values (:order_id,:status,:date,:date2)").bindparams(order_id=result.lastrowid,status="Delivered",date=expected_delivery,date2=expected_delivery))
    print("Done")       


add_data()
    