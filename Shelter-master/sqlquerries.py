import sqlite3
try:
    con = sqlite3.connect("shelter.db")
    # the below line enables foreign keys in the database
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    print("connection successful")
except Exception as e:
    print("error during connection: "+str(e))

# 1.
# sqInsertAnimal is used to insert a record of animal in the Animal Table
# this function generates a unique id between a0001 to a9999
# parameter: (String=animal name, Int=Animal Age, Str=Breed, Str=Species, Str=Details)
# returntype: String=The newly generated ID
def sqInsertAnimal(aname,aage,breed,species,details):
    cur.execute("SELECT an_id from Animal")
    anidlist=cur.fetchall()
    idlist=list()
    for i in anidlist :
        num=int(i[0][1:])
        idlist.append(num)
    for newid in range(1,9999) :
        if newid in idlist :
            continue
        else :
            break
    if newid<10 :
        newidstr = "a000" + str(newid)
    elif newid<100 :
        newidstr = "a00" + str(newid)
    elif newid<1000 :
        newidstr = "a0" + str(newid)
    else :
        newidstr = "a" +str(newid)
    cur.execute("INSERT INTO ANIMAL VALUES(?,?,?,?,?,?);",(newidstr,aname,aage,breed,species,details))
    con.commit()
    return newidstr
# 2.
# sqInsertAdopt is used to insert adoption details into Adopt table
# parameter: str=foreign key an_id, str= foreign key cust_id, str= adoption date
# return type: void
def sqInsertAdopt(an_id,cust_id,ad_date):
    cur.execute("INSERT INTO ADOPT VALUES(?,?,?);",(an_id,cust_id,ad_date))
    con.commit()

# 3.
# sqInsertFoster is used to insert fostering details into foster table
# parameter: str=foreign key an_id, str = foreign key cust_id, str=start date of foster, str= due date
# return type: void
def sqInsertFoster(an_id,cust_id,fost_date,due_date):
    cur.execute("INSERT INTO Foster VALUES(?,?,?,?);",(an_id,cust_id,fost_date,due_date))
    con.commit()
# 4.
# sqInsertInjury is used to insert injury records into Injury table
# parameter: str=foreign key an_id, str=injury date, str=body part, str=injury status
# return type: void
def sqInsertInjury(an_id,in_date,body_part,injury_status):
    cur.execute("INSERT INTO Injury VALUES(?,?,?,?);",(an_id,in_date,body_part,injury_status))
    con.commit()
# 5.
# sqInsertCustomer is used to insert customer details into Customer table
# this function also generates a unique id within range c0001 to c9999
# parameter: Str=Customer name, Str=Phone number, Str=Date of birth, Str=address
# return type: str= generated new customer id
def sqInsertCustomer(cname,phone,dob,address):
    cur.execute("SELECT cust_id from Customer")
    anidlist=cur.fetchall()
    idlist=list()
    for i in anidlist :
        num=int(i[0][1:])
        idlist.append(num)
    for newid in range(1,9999) :
        if newid in idlist :
            continue
        else :
            break
    if newid<10 :
        newidstr = "c000" + str(newid)
    elif newid<100 :
        newidstr = "c00" + str(newid)
    elif newid<1000 :
        newidstr = "c0" + str(newid)
    else :
        newidstr = "c" +str(newid)
    cur.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?);",(newidstr,cname,phone,dob,address))
    con.commit()
    return newidstr

# 6.
# sqInsertCustomer is used to insert volunteer details into volunteer table
# this function also generates a unique id within range v0001 to v9999
# parameter: Str=Volunteer name, Str=Date of birth,Str=phonenumber, Str=address
# return type: str=new generated volunteer id
def sqInsertVolunteer(vname,dob,phone,address):
    cur.execute("SELECT vol_id from Volunteer")
    anidlist=cur.fetchall()
    idlist=list()
    for i in anidlist :
        num=int(i[0][1:])
        idlist.append(num)
    for newid in range(1,9999) :
        if newid in idlist :
            continue
        else :
            break
    if newid<10 :
        newidstr = "v000" + str(newid)
    elif newid<100 :
        newidstr = "v00" + str(newid)
    elif newid<1000 :
        newidstr = "v0" + str(newid)
    else :
        newidstr = "v" +str(newid)
    cur.execute("INSERT INTO Volunteer VALUES(?,?,?,?,?);",(newidstr,vname,dob,phone,address))
    con.commit()
    return newidstr

# 7.
# sqInsertVolunteer_Timings insert volunteer checkin record
# parameter: str=foreign key vol_id, str=date, str=start time, str= end_time
# return type: void
def sqInsertVolunteer_Timings(vol_id,date,vstart_time,vend_time): 
    cur.execute("INSERT INTO VOLUNTEER_TIMINGS VALUES(?,?,?,?);",(vol_id,date,vstart_time,vend_time))  
    con.commit()

# 8.
# sqInsertTakes_Care inserts taking care records
# parameter: str=foreign key vol_id, str=foreign key an_id, str=date, str=start time, str=end time
# return type: void
def sqInsertTakes_Care(vol_id,an_id,vol_date,tstart_time,tend_time):
    cur.execute("INSERT INTO TAKES_CARE VALUES(?,?,?,?,?);",(vol_id,an_id,vol_date,tstart_time,tend_time))
    con.commit()

# 9.
# sqInsertDonations is used to insert donation details into donations
# this function also generates a unique id within range d0001 to d9999
# parameter: Str=Resource, Str=Amount, Str=Donation Date, Str=availability
# return type: str=new generated donation ID
def sqInsertDonations(resource,amount,don_date,availability):
    cur.execute("SELECT DONOR_ID from DONATIONS")
    anidlist=cur.fetchall()
    idlist=list()
    for i in anidlist :
        num=int(i[0][1:])
        idlist.append(num)
    for newid in range(1,9999) :
        if newid in idlist :
            continue
        else :
            break
    if newid<10 :
        newidstr = "d000" + str(newid)
    elif newid<100 :
        newidstr = "d00" + str(newid)
    elif newid<1000 :
        newidstr = "d0" + str(newid)
    else :
        newidstr = "d" +str(newid)
    cur.execute("INSERT INTO DONATIONS VALUES(?,?,?,?,?);",(newidstr,resource,amount,don_date,availability))
    con.commit()
    return newidstr

# 10.
# sqInsertSpending inserts  the spending on animals in SPending table
# parameters: str=an_id, str_donor_id, str+amoun, str=time of spending, str=date
# returntype: void
def sqInsertSpending(an_id,donor_id,amount,time,sp_date):
    cur.execute("INSERT INTO SPENDING VALUES(?,?,?,?,?);",(an_id,donor_id,amount,time,sp_date))
    con.commit()

# 11. 12. 13. 14. 15. 16. 17. 18. 19. 20.
# The following functions searches the respective table for any tuple containing the key and returns all the tuples matched
# parameters: str= the key string to be searched for
# returntype: list of tuples
# ex: list = [tuple1,tuple2,tuple3....]
#     tuple = (an_id,an_name,an_age,breed,species,details)

# 11.
def sqSearchAnimal(key):
    cur.execute("SELECT * FROM ANIMAL WHERE an_id=? or an_name=? or an_age=? or breed=? or species=? or details=?;",(key,key,key,key,key,key))
    anlist=cur.fetchall()
    return anlist

# 12.
def sqSearchAdopt(key):
    cur.execute("SELECT * FROM ADOPT WHERE AN_ID=? OR CUST_ID=? OR AD_DATE=?;",(key,key,key))
    adlist=cur.fetchall()
    return adlist

# 13.
def sqSearchFoster(key):
    cur.execute("SELECT * FROM FOSTER WHERE AN_ID=? OR CUST_ID=? OR FOST_date=? or Due_date=?;",(key,key,key,key))
    foslist=cur.fetchall()
    return foslist

# 14.
def sqSearchInjury(key):
    cur.execute("SELECT * FROM INJURY WHERE AN_ID=? OR IN_dATE=? OR BODY_PART=? OR INJURY_STATUS=?;",(key,key,key,key))
    inlist=cur.fetchall()
    return inlist

# 15.
def sqSearchCustomer(key):
    cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID=? OR CUST_NAME=? OR PHONE =? OR DOB=? OR ADDRESS=?;",(key,key,key,key,key))
    custlist = cur.fetchall()
    return custlist

# 16.
def sqSearchVolunteer(key):
    cur.execute("SELECT * FROM VOLUNTEER WHERE VOL_ID=? OR VOL_NAME=? OR DOB=? OR VOL_PHONE=? OR VOL_ADDRESS=?;",(key,key,key,key,key))
    vollist = cur.fetchall()
    return vollist

# 17.
def sqSearchVolunteer_Timings(key):
    cur.execute("SELECT * FROM VOLUNTEER_TIMINGS WHERE VOL_ID=? OR DATE=? OR VSTART_TIME=? OR VEND_TIME=?;",(key,key,key,key))
    vtlist = cur.fetchall()
    return vtlist

# 18.
def sqSearchTakes_Care(key):
    cur.execute("SELECT * FROM TAKES_CARE WHERE VOL_ID =? OR AN_ID=? OR VOL_DATE=? OR TSTART_TIME=? OR TEND_TIME=?;",(key,key,key,key,key))
    tclist = cur.fetchall()
    return tclist

# 19.
def sqSearchDonations(key):
    cur.execute("SELECT * FROM DONATIOSN WHERE DONOR_ID=? OR RESOURCE=? OR AMOUNT=? OR DON_DATE=? OR AVAILABILITY=?;",(key,key,key,key,key))
    dlist=cur.fetchall()
    return dlist

# 20.
def sqSearchSpending(key):
    cur.execute("SELECT * FROM SPENDING WHERE AN_ID=? OR DONOR_ID=? OR AMOUNT=? OR TIME=? OR SP_DATE=?;",(key,key,key,key,key))
    splist=cur.fetchall()
    return splist

# 21. 22. 24. 25. 26. 29.
# The following functions accept an updated tuple with modified attributes except the key attributes and updates the database
# primary values cannot be updated,
# parameters: tuple=the updated record
# returntype: void
# ex: sqModiftAnimal(newtuple)
#     newtuple = ("a0001","Foxy",5,"Golden","dog","none")
#     where oldtuple(currently in database) was ("a0001","Wolfie",5,"Golden","dog","none")
#     calling sqModifyAnimal(newtuple) updates the databse to change the animal name from "wolfie" to "foxy" whose 
#     an_id was "a0001"
# note: the old tuple can be optained by call sqSearchAnimal("a0001")[0], then this tuple can be converted to list and modified
# after modifications are done convert it backinto tuple and pass it to sqModifyAnimal(newtuple)

# 21. 
# can be modified: an_name, an_Age, breed, species, details
# cannot be modified: an_id      
def sqModifyAnimal(atuple):
    cur.execute("UPDATE ANIMAL SET AN_NAME=?,AN_AGE=?,BREED=?,SPECIES=?,DETAILS=? WHERE AN_ID=?;",(atuple[1],atuple[2],atuple[3],atuple[4],atuple[5],atuple[0]))
    con.commit()

# 22.
# can be modified: ad_Date
# cannot be modified: an_id, cust_id
def sqModifyAdopt(adtuple):
    cur.execute("UPDATE ADOPT SET AD_DATE=? WHERE AN_ID=? AND CUST_ID=?;",(adtuple[2],adtuple[0],adtuple[1]))
    con.commit()

# 24.
# can be modified: Injury Status
# cannot be modified: an_id, injury date, body part
def sqModifyInjury(ituple):
    cur.execute("UPDATE INJURY SET INJURY_STATUS=? WHERE AN_ID=? AND IN_DATE=? AND BODY_PART=?;",(ituple[3],ituple[0],ituple[1],ituple[2]))
    con.commit()

# 25.
# can be modified: cust_name,phone,dob,address
# cannot be modified: cust_id
def sqModifyCustomer(ctuple):
    cur.execute("UPDATE CUSTOMER SET CUST_NAME=?,PHONE=?,DOB=?,ADDRESS=? WHERE CUST_ID=?;",(ctuple[1],ctuple[2],ctuple[3],ctuple[4],ctuple[0]))
    con.commit()

# 26.
# can be modified: vol_name, dob, phone, address
# cannot be modified: vol_id
def sqModifyVolunteer(vtuple):
    cur.execute("UPDATE VOLUNTEER SET VOL_NAME=?,DOB=?,VOL_PHONE=?,VOL_ADDRESS=? WHERE VOL_ID=?;",(vtuple[1],vtuple[2],vtuple[3],vtuple[4],vtuple[0]))
    con.commit()

# 29.
# can be modified:
# cannot be modified:
def sqModifyDonations(dtuple):
    cur.execute("UPDATE DONATIONS SET RESOURCE=?, AMOUNT=?, DON_DATE=?, AVAILABILITY=? WHERE DONOR_ID=?;",(dtuple[1],dtuple[2],dtuple[3],dtuple[4],dtuple[0]))
    con.commit()


# 31. 41. 42.
# sqDeleteAnimal() accepts a key attribute (an_id=a0001,a1200...) and deletes the respective records
# it also deletes corresponding records from spending and takes_care if needed
# parameters: str=an_id(a1000,a1202....)
# return type: void
def sqDeleteAnimal(aid):
    cur.execute("DELETE FROM SPENDING WHERE DONOR_ID IS NULL AND AN_ID=?;",(aid,))
    cur.execute("DELETE FROM TAKES_CARE WHERE VOL_ID IS NULL AND AN_ID=?;",(aid,))
    cur.execute("DELETE FROM ANIMAL WHERE AN_ID=?;",(aid,))
    con.commit()

# 32.
# sqDeleteCustomer() accepts a key attribute (cust_id=c1002,c8910....) and deletes the respective record
# Parameters: str= cust_id("c1020","c5601"...)
# return type: void
def sqDeleteCustomer(cid):
    cur.execute("DELETE FROM CUSTOMER WHERE CUST_ID=?;",(cid,))
    con.commit()

# 33. 42.
# sqDeleteVolunteer() accepts a key attribute and deletes the respective record
# it also deletes corresponding takes_care records if needed
# Parameters: str=vol_id
# return typle: void
def sqDeleteVolunteer(vid):
    cur.execute("DELETE FROM TAKES_cARE WHERE AN_ID IS NULL AND VOL_ID=?;",(vid,))
    cur.execute("DELETE FROM VOLUNTEER WHERE VOL_ID=?;",(vid,))
    con.commit()

# 34. 41.
# sqDeleteDonations() accepts a key attribute and deletes the respective Donations record
# it also deletes corresponding spending records if needed
# Parameters: str=donor_id
# Return type: void
def sqDeleteDonations(did):
    cur.execute("DELETE FROM SPENDING WHERE AN_ID IS NULL AND DONOR_ID=?;",(did,))
    cur.execute("DELETE FROM DONATIONS WHERE DONOR_ID=?;",(did,))
    con.commit()

# 35. 36. 37. 38. 39. 40.
# Since some tables dont have a well defined key attribute we delete the record by
# passing the whole tuple to the respective functions

# 35.
# sqDeleteSpending() accepts a tuple of Spending table and deletes it
# parameters: tuple=(an_id,donor_id,amount,time,sp_date)
# return type: void
def sqDeleteSpending(sptuple):
    cur.execute("DELETE FROM SPENDING WHERE AN_ID =? AND DONOR_ID=? AND AMOUNT=? AND TIME=? AND SP_DATE=?;",sptuple)
    con.commit()

# 36.
# sqDeleteTakes_Care() accepts a tuple of Takes_Care table and deletes it
# parameters: tuple=(vol_id,an_id,vol_Date,tstart_time,tend_time)
# returntype: void
def sqDeleteTakes_Care(tctuple):
    cur.execute("DELETE FROM TAKES_CARE WHERE VOL_ID=? AND AN_ID=? AND VOL_DATE=? AND TSTART_TIME=? AND TEND_TIME=?;",tctuple)
    con.commit()

# 37.
# sqDeleteInjury accepts a tuple of Injury table and deletes it
# parameters: tuple=(an_id,in_date,body_part,injury_status)
# returntype: void
def sqDeleteInjury(ituple):
    cur.execute("DELETE FROM INJURY WHERE AN_ID=? AND IN_DATE=? AND BODY_PART=? AND INJURY_STATUS=?",ituple)
    con.commit()

# 38.
# sqDeleteAdopt accpets a tuple of Adopt table and deletes it
# parameters: tuple=(an_id,cust_id,ad_date)
# return type: void
def sqDeleteAdopt(atuple):
    cur.execute("DELETE FROM ADOPT WHERE AN_ID=? AND CUST_ID=? AND AD_DATE=?;",atuple)
    con.commit()

# 39.
# sqDeleteFoster() accepts a tuple of Foster table and deletes it
# parameters: tuple=(an_id,cust_id,fost_date,due_date)
# return type: void
def sqDeleteFoster(ftuple):
    cur.execute("DELETE FROM FOSTER WHERE AN_ID=? AND CUST_ID=? AND FOST_DATE=? AND DUE_DATE=?;",ftuple)
    con.commit()

# 40.
# sqDeleteVolunteer_Timings() accepts a tuple from volunteertimings table and deletes it
# parameters: tuple=(vol_id,date,vstart_time,vend_time)
# returntype: void
def sqDeleteVolunteer_Timings(vttuple):
    cur.execute("DELETE FROM VOLUNTEER_TIMINGS WHERE VOL_ID=? AND DATE=? AND VSTART_TIME=? AND VEND_TIME=?;",vttuple)
    con.commit()

# 43. 44. 45. 46.
# the following fetchs all records from a particular table
# parameter: none
# returntyple: list= list of tuples containing all records

# 43.
# returns all records in Animal table
def sqListAnimal():
    cur.execute("SELECT * FROM ANIMAL;")
    anlist=cur.fetchall()
    return anlist

# 44.
# returns all records in Customer table
def sqListCustomer():
    cur.execute("SELECT * FROM CUSTOMER;")
    custlist=cur.fetchall()
    return custlist

# 45.
# returns all records in Volunteer table
def sqListVolunteer():
    cur.execute("SELECT * FROM VOLUNTEER;")
    vollist=cur.fetchall()
    return vollist

# 46.
# returns all records in Donations table
def sqListDonations():
    cur.execute("SELECT * FROM DONATIONS;")
    donlist=cur.fetchall()
    return donlist

# 47.
# this function fetches all information related to an animal(an_id)
# this function gives: animal details, adoption detail, list of fostering, list of injury,list of spending, list of takescare
# and the total time it was cared for
# parameter: str=animal id
# return type: list = [0:tuple=animalinfo, 
#                      1:tuple=adoptioninfo, 
#                      2:list=[(foster1),(foster2)...], list of tuples
#                      3:list=[(injury1),(injury2)...], list of tuples
#                      4:list=[(spending1),(spending2)..], list of tuples
#                      5:list=[(takescare1),(takescare2)...], list of tuples
#                      6:int=total time taken care of
#                     ]
# Examples: to print list of injuries of animal a0101
#           >>>L1=sqViewAnimal("a0101")
#           >>>print(L1[3])
#           to print total time animal a2000 was taken care of
#           >>>L1=sqViewAnimal("a2000")
#           >>>print(L1[6])
def sqViewAnimal(an_id):
    cur.execute("SELECT * FROM ANIMAL WHERE AN_ID=?;",(an_id,))
    antuple=cur.fetchone()
    cur.execute("SELECT * FROM ADOPT WHERE AN_ID=?;",(an_id,))
    adtuple=cur.fetchone()
    cur.execute("SELECT * FROM FOSTER WHERE AN_ID=?",(an_id,))
    fostlist=cur.fetchall()
    cur.execute("SELECT * FROM INJURY WHERE AN_ID=?",(an_id,))
    injlist=cur.fetchall()
    cur.execute("SELECT * FROM SPENDING WHERE AN_ID=?;",(an_id,))
    splist=cur.fetchall()
    cur.execute("SELECT * FROM TAKES_CARE WHERE AN_ID=?;",(an_id,))
    tclist=cur.fetchall()
    sumhrs=0
    for i in tclist:
        timehrs=int(i[4][0:2])*60-int(i[3][0:2])*60 +int(i[4][3:5])-int(i[3][3:5])
        sumhrs=sumhrs+timehrs
    sumhrs=sumhrs/60
    finallist=[antuple,adtuple,fostlist,injlist,splist,tclist,int(sumhrs)]
    return finallist

# 48.
# this function fetches all information related to a customer
# this function gives: customerdetails, list of customer adoptions, list of fosters
# parameter: str=customer id
# return type: list=[0:tuple=customer details
#                    1:list=[(adopt1),(adopt2)...] list of tuples
#                    2:list=[(foster1),(foster2)...] list of tuples
#                   ]
def sqViewCustomer(cust_id):
    cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID=?;",(cust_id,))
    custtuple=cur.fetchone()
    cur.execute("SELECT * FROM ADOPT WHERE CUST_ID=?;",(cust_id,))
    adlist=cur.fetchall()
    cur.execute("SELECT * FROM FOSTER WHERE CUST_ID=?;",(cust_id,))
    fostlist=cur.fetchall()
    finallist=[custtuple,adlist,fostlist]
    return finallist

# 49.
# this functin fetches all information related to a volunteer
# this function gives: volunteer details, list of vtimings, list of takes_Care, 
#                      total time volunteered, total time taken care for each animal
# parameter: str=volunteer id
# return typle: List=[0: tuple=volunteerdetails
#                     1: list=[(vtimings1),(vtimings2),...] list of tuples
#                     2: list=[(takes_Care1),(takes_Care2),....] list of tuples
#                     3: int=total hrs volunteered
#                     4: list=[(an_id,hrs),(an_id,hrs),("a2001",31)....]
#                        4:this is a list of tuples, each tuple represents the 
#                        total hours spent on that particular an_id 
#                    ] 
def sqViewVolunteer(vol_id):
    cur.execute("SELECT * FROM VOLUNTEER WHERE VOL_ID=?;",(vol_id,))
    voltuple=cur.fetchone()
    cur.execute("SELECT * FROM VOLUNTEER_TIMINGS WHERE VOL_ID=?;",(vol_id,))
    vtlist=cur.fetchall()
    cur.execute("SELECT * FROM TAKES_CARE WHERE VOL_ID=?;",(vol_id,))
    tclist=cur.fetchall()
    totalhr=0
    #summin=0
    for i in vtlist:
        timehr=int(i[3][0:2])*60+int(i[3][3:5])-int(i[2][0:2])*60-int(i[2][3:5])
        #timehr=int(i[3][0:2])-int(i[2][0:2])
        #timmin=int(i[3][3:5])-int(i[2][3:5])
        totalhr=totalhr+timehr
    totalhr=totalhr/60
    cur.execute("SELECT DISTINCT an_id from TAKES_CARE WHERE VOL_ID=?;",(vol_id,))
    anlist=cur.fetchall()
    anidlist=list()
    for i in anlist:
        cur.execute("SELECT AN_NAME FROM ANIMAL WHERE an_id=?;",(i[0],))
        anname=cur.fetchone()
        newtuple=(i[0],anname[0])
        anidlist.append(newtuple)
    finalindlist=list()
    for i in anidlist:
        sumhr=0
        summin=0
        for j in tclist:
            if j[1]==i[0] :
                timehr=int(j[4][0:2])*60-int(j[3][0:2])*60 + int(j[4][3:5])-int(j[3][3:5])
                #timmin=int(j[4][3:5])-int(j[3][3:5])
                sumhr=sumhr+timehr
                #summin=summin+timmin
        sumhr=sumhr/60
        itctuple=(i[0],i[1],int(sumhr))
        finalindlist.append(itctuple)
    finallist=[voltuple,vtlist,tclist,int(totalhr),finalindlist]
    return finallist

# 50.
# this function fetches all information related to a particular donation
# this function retrieves: donation info, list of spending on that dono
# parameter: str=donoation id
# return type: list=[0:tuple=donation details
#                    1:list=[(spending1),(spending2)...] list of tuples
#                   ]
def sqViewDonations(donor_id):
    cur.execute("SELECT * FROM DONATIONS WHERE DONOR_ID=?;",(donor_id,))
    donotuple=cur.fetchone()
    cur.execute("SELECT * FROM SPENDING WHERE DONOR_ID=?;",(donor_id,))
    splist=cur.fetchall()
    finallist=[donotuple,splist]
    return finallist

# 51. 52. functions which creates all the nescessary tables and handles password
# sqCreateTables() Creates the nescessary tables if it doesnt exists
# if the tables exist then nothing is changed
# parameters: none
# return type: void
def sqCreateTables():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Animal(
        an_id TEXT PRIMARY KEY, 
        an_name TEXT, 
        an_age INT, 
        breed TEXT, 
        species TEXT, 
        details TEXT ); 
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Customer(
        cust_id TEXT PRIMARY KEY, 
        cust_name TEXT, 
        phone TEXT, 
        DOB TEXT, 
        address TEXT ); 
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS foster(
        an_id TEXT, 
        cust_id TEXT, 
        fost_date TEXT, 
        due_date TEXT, 
        FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, 
        FOREIGN KEY(cust_id) REFERENCES Customer(cust_id) ON DELETE SET NULL ); 
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS adopt(
        an_id TEXT, 
        cust_id TEXT, 
        ad_date TEXT, 
        FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, 
        FOREIGN KEY(cust_id) REFERENCES Customer(cust_id) ON DELETE SET NULL
        PRIMARY KEY(AN_ID) ); 
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS injury(
        an_id TEXT, 
        in_date TEXT, 
        body_part TEXT, 
        injury_status TEXT, 
        FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE
        PRIMARY KEY(AN_ID,in_DATE,BODY_PART) ); 
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS donations(
        donor_id TEXT PRIMARY KEY, 
        resource TEXT, 
        amount TEXT, 
        don_date TEXT, 
        availability TEXT );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS spending(
        an_id TEXT, 
        donor_id TEXT, 
        amount TEXT, 
        time TEXT, 
        sp_date TEXT, 
        FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE SET NULL, 
        FOREIGN KEY(donor_id) REFERENCES Donations(donor_id) ON DELETE SET NULL );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS volunteer(
        vol_id TEXT PRIMARY KEY, 
        vol_name TEXT, 
        dob TEXT, 
        vol_phone TEXT, 
        vol_address TEXT); 
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS takes_care(
        vol_id TEXT, 
        an_id TEXT, 
        tc_date TEXT, 
        tcStart_time TEXT, 
        tcEnd_time, 
        FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE SET NULL , 
        FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE SET NULL );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS volunteer_timings(
        vol_id TEXT, 
        V_date TEXT, 
        vStart_time TEXT, 
        vEnd_time TEXT,  
        FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE CASCADE );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Password(
        pass TEXT );
        """)
    con.commit()

# 51. 52.
# sqIsPassCreated() is used to check if the password is created
# password is stored as a tuple in the Password table
# parameter: None
# return type: BOOL 
#              True: If password is already created
#              Flase: If password was not created
def sqIsPassCreated():
    cur.execute("SELECT COUNT(*) from Password")
    L=cur.fetchall()
    if L[0][0]==1 :
        return True
    else :
        return False

# 51. 52.
# sqSetPassword() inserts the password into Password table
# parameter: string=The password which is to be inserted
# returntype: void
def sqSetPassword(psw):
    if sqIsPassCreated() == False :
        cur.execute("INSERT INTO Password VALUES(?); ",(psw,))
        con.commit()  

# 51. 52.
# sqGetPassword() fetches the password from the table password
# parameter: none
# returntype: String=the password 
def sqGetPassword():
    cur.execute("SELECT * FROM PASSWORD")
    L=cur.fetchall()
    return L[0][0]
