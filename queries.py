import sqlite3,os,time
def connectdb():
    global conn,cur
    try:
        print("Connecting to db\n")
        conn=sqlite3.connect("ArtMuseum.db")
        cur=conn.cursor()
        print("Success")
        time.sleep(3)
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
Find Number of Paintings given by each gallery(5)
Exit(6)\n""")
        if(x=="1"):
            os.system('cls')
            artperiod=input("Enter desired art period:\n")
            museums=input("Enter desired museum:\n")
            curr.execute("Select artid,Title FROM Painting WHERE ArtPeriod_name='"+artperiod+"' AND artid in (SELECT artid from Loan WHERE OriginName='"+museums+"');")
            data=curr.fetchall()
            print("RESULTS:\n")
            if (len(data)==0):
                print("No results based on given parameters")
            else:
                for i in data:
                    print(i[0],i[1])
            time.sleep(5)
        elif(x=="2"):
            os.system('cls')
            curr.execute("SELECT Room,Pos_no From Position EXCEPT SELECT Room,Pos_no From Painting;")
            data=curr.fetchall()
            print("RESULTS:\n")
            for i in data:
                print(i[0],i[1])
            time.sleep(5)
        elif(x=="3"):
            os.system('cls')
            name=input("Enter Artist Name:\n")
            curr.execute("SELECT Title,Creationyear From Painting join Artist on ArtistID=ID where (Name||' '||COALESCE(Surname,''))='" +Artist_name+"';")
            data=curr.fetchall()
            print("RESULTS:\n")
            if (len(data)==0):
                print("No results based on given parameters")
            else:
                for i in data:
                    print(i[0],i[1])
            time.sleep(5)
        elif(x=="4"):
            os.system('cls')
            curr.execute("SELECT ArtPeriod_name,count(ArtPeriod_name) from Painting GROUP by ArtPeriod_name;")
            data=curr.fetchall()
            print("RESULTS:\n")
            for i in data:
                print(i[0],i[1])
            time.sleep(5)
        elif(x=="5"):
            os.system('cls')
            curr.execute("SELECT OriginName,count(OriginName) as noOfPaintings from Painting NATURAL JOIN Loan GROUP by OriginName ORDER by noOfPaintings DESC;")
            data=curr.fetchall()
            print("RESULTS:\n")
            if (len(data)==0):
                print("No results based on given parameters")
            else:
                for i in data:
                    print(i[0],i[1])
            time.sleep(5)
        elif(x=="6"):
            os.system('cls')
            conn.close()
            print("Have a nice day!")
            time.sleep(3)
            break

            

             
            

        
if __name__=="__main__":
    connectdb()
    queries()
    



    



               

