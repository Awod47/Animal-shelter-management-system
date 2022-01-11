import sqlite3

try:
    con = sqlite3.connect("shelter.db")
    cur = con.cursor()
    print("connection successful")
except Exception as e:
    print("error during connection: "+str(e))


def create_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS Animal(an_id TEXT PRIMARY KEY, an_name TEXT, an_age INT, breed TEXT, species TEXT, details TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS Customer(cust_id TEXT PRIMARY KEY, cust_name TEXT, phone INT, DOB TEXT, address TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS foster(an_id TEXT, cust_id TEXT, fost_date TEXT, due_date TEXT, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, FOREIGN KEY(cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS adopt(an_id TEXT, cust_id TEXT, ad_date TEXT, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, FOREIGN KEY(cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS injury(an_id TEXT, in_date TEXT, body_part TEXT, injury_status TEXT, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS donations(donor_id TEXT PRIMARY KEY, resource TEXT, amount INT, don_date TEXT, availability TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS spending(an_id TEXT, donor_id TEXT, resource TEXT, amount INT, time TEXT, sp_date TEXT , FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, FOREIGN KEY(donor_id) REFERENCES Donotions(donor_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer(vol_id TEXT PRIMARY KEY, vol_name TEXT, dob TEXT, vol_phone INT, vol_address TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS takes_care(vol_id TEXT, an_id TEXT, tc_date TEXT, tcStart_time TEXT, tcEnd_time , FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE CASCADE, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer_timings(vol_id TEXT, V_date TEXT, vStart_time TEXT, vEnd_time TEXT,  FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE CASCADE);")
    con.commit()
    cur.close()
    con.close()