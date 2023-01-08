import sqlite3,os,time
def connectdb():
    global conn,cur
    try:
        print("Connecting to db\n")
        conn=sqlite3.connect("ArtMuseum.db")
        cur=conn.cursor()
        print("Success")
        input("\nPress Enter to continue:")
    except:
        print("Error connecting")
        exit()    
def queries():
    global conn,curr
    curr=conn.cursor()
    while True:
        os.system('cls')
        x=input("""Find Which Loaned Painting from a certain Art Period Comes From a certain Museum (1)
Find Empty Positions (2)
Find Paintings of a certain Artist (3)
Find Number of Paintings in each Period (4)
Find Number of Paintings given and taken by each gallery(5)
Show List Of Paintings In Display (Permanent And Loaned)(6)
Exit(7)\n""")
        if(x=="1"):
            os.system('cls')
            artperiod=input("Enter desired art period:\n")
            museums=input("Enter desired museum:\n")
            style="{:<5}{:<2}"
            curr.execute("Select artid,Title FROM Painting WHERE ArtPeriod_name='"+artperiod+"' AND artid in (SELECT artid from Loan WHERE OriginName='"+museums+"');")
            data=curr.fetchall()
            print("RESULTS:\n")
            print(style.format("ID","Title"))
            if (data==None):
                print("No results based on given parameters")
            else:
                for i in data:
                    print(style.format(i[0],i[1]))
            input("\nPress Enter to continue:")
        elif(x=="2"):
            os.system('cls')
            style="{:20}{:<2}"
            curr.execute("SELECT Room,Pos_no From Position EXCEPT SELECT Room,Pos_no From Painting;")
            data=curr.fetchall()
            print("RESULTS:\n")
            print(style.format("Room","Number of Position"))
            for i in data:
                print(style.format(i[0],i[1]))
            input("\nPress Enter to continue:")
        elif(x=="3"):
            os.system('cls')
            style="{:30}{:<2}"
            name=input("Enter Artist Name:\n")
            curr.execute("SELECT Title,Creationyear From Painting join Artist on ArtistID=ID where (Name||' '||COALESCE(Surname,''))='" +name+"'ORDER BY Creationyear ASC;")
            data=curr.fetchall()
            print("RESULTS:\n")
            print("Paintings of "+name+"\n")
            print(style.format("Title","Year Of Creation"))
            if (data==None):
                print("No results based on given parameters")
            else:
                for i in data:
                    print(style.format(i[0],i[1]))
            input("\nPress Enter to continue:")
        elif(x=="4"):
            os.system('cls')
            style="{:20}{:<2}"
            curr.execute("SELECT ArtPeriod_name,count(ArtPeriod_name) as c from Painting GROUP by ArtPeriod_name ORDER BY c DESC;")
            data=curr.fetchall()
            print("RESULTS:\n")
            print(style.format("Art Period","Number of Paintings"))
            for i in data:
                print(style.format(i[0],i[1]))
            input("\nPress Enter to continue:")
        elif(x=="5"):
            os.system('cls')
            curr.execute("""SELECT Gallery, sum(noOfPaintings) as transactions from
(SELECT OriginName as Gallery ,count(OriginName) as noOfPaintings from Painting NATURAL JOIN Loan GROUP by OriginName
UNION
select BorrowerName as Gallery, count(BorrowerName) as noOfPaintings from Painting NATURAL JOIN Owned NATURAL JOIN Takes GROUP by BorrowerName)
group by Gallery ORDER by transactions DESC""")
            data=curr.fetchall()
            style="{:34}{:<2}"
            print("RESULTS:\n")
            print(style.format("Gallery","Number of Recorded Transactions"))
            if (data==None):
                print("No results based on given parameters")
            else:
                for i in data:
                    print(style.format(i[0],i[1]))
            input("\nPress Enter to continue:")
        elif(x=="6"):
            os.system('cls')
            curr.execute("""SELECT Title,CreatorName FROM(
SELECT Title,Name||' '||coalesce(Surname,'') as CreatorName FROM Painting JOIN Artist on ArtistID=ID natural JOIN Loan  where julianday('now') BETWEEN julianday(LoanStart) AND julianday(LoanEnd) AND Room not like '%WAREHOUSE%' AND Room is not NULL
UNION
SELECT Title,Name||' '||coalesce(Surname,'')  as CreatorName FROM Painting JOIN Artist on ArtistID=ID NATURAL JOIN Owned where Room not like '%WAREHOUSE%' AND Room is not NULL)
ORDER by Title ASC;""")
            data=curr.fetchall()
            style="{:<50}{:<10}"	
            print("RESULTS:\n")
            print(style.format("Title","Creator"))
            if (data==None):
                print("No results based on given parameters")
            else:
                for i in data:
                    print(style.format(i[0],i[1]))
            input("\nPress Enter to continue:")

        elif(x=="7"):
            os.system('cls')
            conn.close()
            print("Have a nice day!")
            time.sleep(3)
            break

            

             
            

        
if __name__=="__main__":
    connectdb()
    queries()
    



    



               

