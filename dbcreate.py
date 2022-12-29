import sqlite3,datetime,time

def load_data():
    global conn
    loanedto = [
(38,"Uffizi",datetime.datetime(2020,12,1),datetime.datetime(2021,12,1)),
(51,"Museo del Prado",datetime.datetime(2022,9,1),datetime.datetime(2023,2,28)),
(52,"Museo del Prado",datetime.datetime(2022,9,1),datetime.datetime(2023,2,28)),
(53,"Uffizi",datetime.datetime(2022,12,1),datetime.datetime(2023,12,1)),
(54,"Louvre",datetime.datetime(2022,10,1),datetime.datetime(2023,2,28)),
(55,"Museo del Prado",datetime.datetime(2022,9,1),datetime.datetime(2023,3,31)),
(56,"Uffizi",datetime.datetime(2022,12,1),datetime.datetime(2023,12,1)),
(8,"British Museum",datetime.datetime(2023,12,1),datetime.datetime(2024,12,1)),
(9,"British Museum",datetime.datetime(2023,12,1),datetime.datetime(2024,12,1))
]
    Idioktitos = [(2,),(3,),(4,),(5,),(6,),(7,),(8,),(9,),(10,),
              (11,),(14,),(15,),(16,),(17,),(18,),(19,),
              (20,),(21,),(22,),(23,),(26,),(28,),(29,),
              (30,),(31,),(37,),(38,),(39,),
              (40,),(41,),(42,),
              (51,),(52,),(53,),(54,),(55,),(56,)]
    loanedpaintings=[(34,datetime.datetime(2022,6,1),datetime.datetime(2023,6,1),"National Gallery (London)"),
                 (36,datetime.datetime(2022,6,1),datetime.datetime(2023,6,1),"Museo Regionale (Messina)"),
                 (25,datetime.datetime(2022,6,1),datetime.datetime(2023,6,1),"Hermitage"),
                 (24,datetime.datetime(2022,6,1),datetime.datetime(2023,6,1),"Rijksmuseum"),
                 (43,datetime.datetime(2022,9,1),datetime.datetime(2023,9,1),"Museo Reina Sofia"),
                 (44,datetime.datetime(2022,9,1),datetime.datetime(2023,9,1),"Museum of Modern Art(New York)"),
                 (45,datetime.datetime(2022,9,1),datetime.datetime(2023,9,1),"Solomon R. Guggenheim Museum"),
                 (35,datetime.datetime(2022,9,1),datetime.datetime(2023,9,1),"Musée Picasso"),
                 (1,datetime.datetime(2022,12,1),datetime.datetime(2023,12,1),"Louvre"),
                 (12,datetime.datetime(2022,12,1),datetime.datetime(2023,12,1),"Uffizi"),
                 (13,datetime.datetime(2022,12,1),datetime.datetime(2023,12,1),"Uffizi"),
                 (27,datetime.datetime(2022,12,1),datetime.datetime(2023,12,1),"Louvre"),
                 (32,datetime.datetime(2022,12,1),datetime.datetime(2023,12,1),"British Museum"),
                 (33,datetime.datetime(2022,12,1),datetime.datetime(2023,12,1),"Uffizi"),
                 (46,datetime.datetime(2023,1,1),datetime.datetime(2024,1,1),"Gemäldegalerie Berlin"),
                 (47,datetime.datetime(2023,1,1),datetime.datetime(2024,1,1),"National Gallery (London)"),
                 (48,datetime.datetime(2023,1,1),datetime.datetime(2024,1,1),"National Gallery (London)"),
                 (49,datetime.datetime(2023,1,1),datetime.datetime(2024,1,1),"Uffizi"),
                 (50,datetime.datetime(2023,1,1),datetime.datetime(2024,1,1),"National Gallery (London)")]
    galleries =[("Uffizi",) , ("Hermitage",), ("Louvre",), ("British Museum",),("Museo del Prado",),
            ("National Gallery (London)",),("Museum of Modern Art(New York)",),("Museo Regionale (Messina)",),("Rijksmuseum",),
            ("Museo Reina Sofia",),("Solomon R. Guggenheim Museum",),("Musée Picasso",),("Gemäldegalerie Berlin",)]

    categories =[("Rennaisance",),
             ("Impressionism",),
             ("Modern",),
             ("Romanticism",),
             ("Surrealism",),
             ("Expressionism",),
             ("Baroque",)]

    positions=[("DISPLAY ROOM 1" , 101, False,True),
           ("DISPLAY ROOM 1" , 102, False,True),
           ("DISPLAY ROOM 1" , 103, False,True),
           ("DISPLAY ROOM 1" , 104, False,True),
           ("DISPLAY ROOM 1" , 105, False,True),
           ("DISPLAY ROOM 1" , 106, False,True),
           ("DISPLAY ROOM 1" , 107, False,True),
           ("DISPLAY ROOM 1" , 108, False,True),
           ("DISPLAY ROOM 1" , 109, False,True),
           ("DISPLAY ROOM 1" , 110, False,True),
           ("DISPLAY ROOM 1" , 111, False,True),
           ("DISPLAY ROOM 1" , 112, False,True),
           ("DISPLAY ROOM 1" , 113, False,True),
           ("DISPLAY ROOM 2" , 201, False,True),
           ("DISPLAY ROOM 2" , 202, False,True),
           ("DISPLAY ROOM 2" , 203, False,True),
           ("DISPLAY ROOM 2" , 204, False,True),
           ("DISPLAY ROOM 2" , 205, False,True),
           ("DISPLAY ROOM 2" , 206, False,True),
           ("DISPLAY ROOM 2" , 207, False,True),
           ("DISPLAY ROOM 2" , 208, False,True),
           ("DISPLAY ROOM 3" , 301, False,True),
           ("DISPLAY ROOM 3" , 302, False,True),
           ("DISPLAY ROOM 3" , 303, False,True),
           ("DISPLAY ROOM 3" , 304, False,True),
           ("DISPLAY ROOM 3" , 305, False,True),
           ("DISPLAY ROOM 3" , 306, False,True),
           ("DISPLAY ROOM 3" , 307, False,True),
           ("DISPLAY ROOM 3" , 308, False,True),
           ("EXHIBITION ROOM",1,False,True),
           ("EXHIBITION ROOM",2,False,True),
           ("EXHIBITION ROOM",3,False,True),
           ("EXHIBITION ROOM",4,False,True),
           ("EXHIBITION ROOM",5,False,True),
           ("EXHIBITION ROOM",6,False,True),
           ("WAREHOUSE 1",1,True,False),
           ("WAREHOUSE 1",2,True,False),
           ("WAREHOUSE 1",3,True,False),
           ("WAREHOUSE 1",4,True,False),
           ("WAREHOUSE 1",5,True,False),
           ("WAREHOUSE 1",6,True,False),
           ("WAREHOUSE 1",7,True,False),
           ("WAREHOUSE 1",8,True,False),
           ("WAREHOUSE 1",9,True,False),
           ("WAREHOUSE 1",10,True,False),
           ("WAREHOUSE 2",1,True,False),
           ("WAREHOUSE 2",2,True,False),
           ("WAREHOUSE 2",3,True,False),
           ("WAREHOUSE 2",4,True,False),
           ("WAREHOUSE 2",5,True,False),
           ("WAREHOUSE 2",6,True,False),
           ("WAREHOUSE 2",7,True,False),
           ("WAREHOUSE 2",8,True,False),
           ("WAREHOUSE 2",9,True,False),
           ("WAREHOUSE 2",10,True,False)]

    artists = [
	(1,"Leonardo","Da Vinci","Italian"),
        (2, "Claude","Monet","French"),
	(3,"Vincent","Van Gogh", "Dutch"),
	(4, "Jackson","Pollock","American"),
	(5,"Sandro","Botticelli","Italian"),
	(6, "Salvador","Dali","Spanish"),
	(7,"Domenikos","Theotokopoulos","Greek"),
	(8,"Andy","Warhol","American"),
        (9,"Jan","van Eyck","Dutch"),
	(10,"Eugene","Delacroix","French"),
	(11,"Michelangelo",None,"Italian"),
        (12,"Caravaggio",None,"Italian"),
        (13,"Raphael",None,"Italian"),
        (14,"Pablo","Picasso","Spanish"),
	(15,"Andrea","del Verrochio","Italian"),
	(16,"Joan","Miro","Spanish"),
	(17,"Rembrandt",None,"Dutch"),
        (18,"Edvard","Munch","Norwegian"),
        (19,"Nikos", "Eggonopoylos","Greek"),
        (20,"Nikiforos","Lytras","Greek")
        ]



    paintings=[
	(1,"Mona Lisa",1503,"Rennaisance",1,"EXHIBITION ROOM",1),
        (2, "Lady with an Ermine",1489,"Rennaisance",1,"DISPLAY ROOM 1",108),
	(3,"Starry Night",1889,"Impressionism",3,"DISPLAY ROOM 2",203),
	(4, "The Potato Eaters",1885,"Impressionism",3,"DISPLAY ROOM 2",204),
	(5,"Van Gogh self-portrait",1889,"Impressionism",3,"DISPLAY ROOM 2",205),
	(6, "Liberty Leading the People",1830,"Romanticism",10,"DISPLAY ROOM 2",201),
	(7,"The Massacre at Chios",1824,"Romanticism",10,"DISPLAY ROOM 2",202),
	(8,"Wild Poppies",1873,"Impressionism",2,"WAREHOUSE 1",1),
	(9,"Impression, Sunrise",1873,"Impressionism",2,"WAREHOUSE 1",2),
	(10,"Convergence",1952,"Modern",4,"DISPLAY ROOM 3" , 301),
	(11,"Mural",1943,"Modern",4,"DISPLAY ROOM 3" , 302),
        (12,"The Birth of Venus",1486,"Rennaisance",5,"EXHIBITION ROOM",2),
        (13,"Primavera",1480,"Rennaisance",5,"EXHIBITION ROOM",3),
        (14,"The Disrobing of Christ",1579,"Rennaisance",7,"DISPLAY ROOM 1",107),
	(15,"The Adoration of the Shepherds",1614,"Rennaisance",7,"DISPLAY ROOM 1",106),
	(16,"Shot Marilyns",1964,"Modern",8,"DISPLAY ROOM 3",303),
	(17,"Campbell's Soup Cans",1962,"Modern",8,"DISPLAY ROOM 3",304),
        (18,"The Persistence of Memory",1931,"Surrealism",6,"DISPLAY ROOM 3",305),
        (19,"The Disintegration of the Persistence of Memory",1954,"Surrealism",6,"DISPLAY ROOM 3",306),
        (20,"Guernica",1937,"Surrealism",14,"DISPLAY ROOM 3",307),
        (21,"The Old Guitarist",1904,"Expressionism",14,"DISPLAY ROOM 3",308),
        (22,"The Scream",1893,"Expressionism",18,"DISPLAY ROOM 2",206),
        (23,"Love and Pain",1895,"Expressionism",18,"DISPLAY ROOM 2",207),
        (24,"The Night Watch",1642,"Baroque",17,"WAREHOUSE 1",3),
        (25,"The Return of the Prodigal Son",1669,"Baroque",17,"WAREHOUSE 1",4),
        (26,"Virgin and Child with Canon van der Paele",1434,"Rennaisance",9,"DISPLAY ROOM 1",109),
        (27,"Madonna of Chancellor Rolin",1435,"Rennaisance",9,"EXHIBITION ROOM",4),
        (28,"Portrait of Jan de Leeuw", 1436, "Rennaisance",9,"WAREHOUSE 1",5),
        (29,"The Taddei Tondo", 1502,"Rennaisance",11,"DISPLAY ROOM 1" , 101),
        (30,"Madonna of Bruges", 1504,"Rennaisance",11,"DISPLAY ROOM 1" , 102),
        (31,"The Doni Tondo", 1504,"Rennaisance",11,"DISPLAY ROOM 1" , 103),
        (32,"Antique warrior in profile",1472,"Rennaisance",1,"EXHIBITION ROOM",5),
        (33,"The Annunciation", 1609,"Rennaisance", 7,"EXHIBITION ROOM",6),
        (34,"The Supper at Emmaus",1601,"Baroque", 12,"WAREHOUSE 1",6),
        (35,"Portrait of Dora Maar",1937,"Surrealism",14,"WAREHOUSE 1",7),
        (36,"The Raising of Lazarus",1609,"Baroque", 12,"WAREHOUSE 1",8),
        (37,"The Seven Works of Mercy",1607,"Baroque", 12,"WAREHOUSE 1",9 ),
        (38,"The Ansidei Madonna",1505,"Rennaisance",13,"DISPLAY ROOM 1" , 104),
        (39,"The Madonna of the Meadow",1506,"Rennaisance",13,"DISPLAY ROOM 1" , 105),
        (40,"Saint Catherine of Alexandria",1507,"Rennaisance",13,"DISPLAY ROOM 1" , 110),
        (41,"Deposition of Christ",1507,"Rennaisance",13,"DISPLAY ROOM 1" , 111),
        (42,"Madonna of the Pinks",1506,"Rennaisance",13,"DISPLAY ROOM 1" , 112),
        (43,"Pastoral",1924,"Surrealism",16,"WAREHOUSE 1",10),
        (44,"Catalan Landscape",1923,"Surrealism",16,"WAREHOUSE 2",1),
        (45,"The Tilled Field",1923,"Surrealism",16,"WAREHOUSE 2",2),
        (46,"Madonna and Child",1488,"Rennaisance",15,"WAREHOUSE 2",3),
        (47,"Virgin and Child with Two Angels",1478,"Rennaisance",15,"WAREHOUSE 2",4),
        (48,"Adoration of the Child",1484,"Rennaisance",15,"WAREHOUSE 2",5),
        (49,"Baptism of Christ",1473,"Rennaisance",15,"WAREHOUSE 2",6),
        (50,"Tobias and the Angel",1480,"Rennaisance",15,"WAREHOUSE 2",7),
        (51,"Gamos",1957,"Modern",19,None,None),
        (52,"Odisseys kai kalypso",1956,"Modern",19,None,None),
        (53,"Arravones",1954,"Modern",19,None,None),
        (54,"O Galatas",1895,"Modern",20,None,None),
        (55,"I Antigoni Empros sto Nekro Polyneiki",1865,"Modern",20,None,None),
        (56,"Kalanta",1872,"Modern",20,None,None),
        
        ]

    exhibitions=[(1,"Baroque Period",datetime.datetime(2022,6,1),datetime.datetime(2022,8,31)),
            (2,"Joan Miro",datetime.datetime(2022,9,1),datetime.datetime(2022,12,1)),
            (3,"Rennaisance Painters",datetime.datetime(2022,12,1),datetime.datetime(2023,2,28)),
            (4,"Andrea del Verocchio",datetime.datetime(2023,3,1),datetime.datetime(2023,5,31)),
            (5,"Surrealist Ideas",datetime.datetime(2023,6,1),datetime.datetime(2023,8,31))]

    onview=[(1,34),(1,36),(1,25),(1,24),
        (2,43),(2,44),(2,45),
        (3,1),(3,12),(3,13),(3,27),(3,32),(3,33),
        (4,46),(4,47),(4,48),(4,49),(4,50),
        (5,43),(5,44),(5,45),(5,35)]
    conn.executemany("INSERT INTO Painting VALUES (?,?,?,?,?,?,?)",paintings)
    conn.executemany("INSERT INTO Artist VALUES (?,?,?,?)",artists)
    conn.executemany("INSERT INTO ArtPeriod VALUES (?)",categories)
    conn.executemany("INSERT INTO Exhibition VALUES (?,?,?,?)",exhibitions)
    conn.executemany("INSERT INTO Associate_Gallery VALUES (?)",galleries)
    conn.executemany("INSERT INTO Owned VALUES (?)",Idioktitos)
    conn.executemany("INSERT INTO Loan VALUES (?,?,?,?)",loanedpaintings)
    conn.executemany("INSERT INTO Position VALUES (?,?,?,?)",positions)
    conn.executemany("INSERT INTO Takes VALUES (?,?,?,?)",loanedto)
    conn.executemany("INSERT INTO IsDisplayed VALUES (?,?)",onview)
    conn.commit()
    conn.close()
    print("Data Inserted Succesfully\n")

def createdatabase():
    global conn
    conn=sqlite3.connect("ArtMuseum.db")
    table1="""CREATE TABLE Painting (
	artid integer,
	Title varchar NOT NULL,
	Creationyear INTEGER,
	ArtPeriod_name varchar,
	ArtistID integer,
	Room varchar,
	Pos_no integer,
	PRIMARY KEY (artid),
	FOREIGN KEY (ArtPeriod_name) REFERENCES ArtPeriod(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (ArtistID) REFERENCES Artist(ID)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (Room,Pos_no) REFERENCES Position(Room,Pos_no)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
        UNIQUE(Room, Pos_no)
);"""
    table2="""CREATE TABLE Artist (
	ID integer,
	Name varchar NOT NULL,
	Surname varchar,
	Nationality varchar,
	PRIMARY KEY (ID)
);"""
    table3="""CREATE TABLE ArtPeriod (
	Name varchar,
	PRIMARY KEY (Name)
);"""
    table4="""CREATE TABLE Exhibition (
	ID integer,
	Subject varchar NOT NULL,
	StartDate date NOT NULL,
	EndDate date NOT NULL,
	PRIMARY KEY (ID),
	CONSTRAINT dates CHECK (StartDate<EndDate)
);"""
    table5="""CREATE TABLE Associate_Gallery (
	Name varchar, 
	PRIMARY KEY (Name)
);"""
    table6="""CREATE TABLE Owned (
	artid integer,
	PRIMARY KEY (artid)
);
"""
    table7="""CREATE TABLE Loan (
	artid integer,
	LoanStart date NOT NULL,
	LoanEnd date NOT NULL,
	OriginName varchar NOT NULL,
	PRIMARY KEY (artid),
	FOREIGN KEY (OriginName) REFERENCES Associate_Gallery(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	CONSTRAINT dates CHECK (LoanStart<LoanEnd)
	
);"""
    table8="""CREATE TABLE Position (
	Room varchar,
	Pos_no integer,
	Storage boolean,
	In_Display boolean,
	PRIMARY KEY (Room,Pos_no),
	CONSTRAINT TWOPLACE CHECK (Storage <> In_Display)
);"""
    table9="""CREATE TABLE Takes (
	artid integer ,
	BorrowerName VARCHAR,
	LoanStart date NOT NULL,
	LoanEnd date NOT NULL,
	PRIMARY KEY (artid, BorrowerName),
	FOREIGN KEY (artid) REFERENCES Owned(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (BorrowerName) REFERENCES Associate_Gallery(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	CONSTRAINT dates CHECK (LoanStart<LoanEnd)
);"""
    table10="""CREATE TABLE IsDisplayed (
	artid integer,
	ExhibitionId integer,
	PRIMARY KEY (artid, ExhibitionId),
	FOREIGN KEY (artid) REFERENCES Loan(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (ExhibitionId) REFERENCES Exhibition(ID)
	ON	DELETE CASCADE		ON	UPDATE		CASCADE
);"""
    conn.execute(table1)
    conn.execute(table2)
    conn.execute(table3)
    conn.execute(table4)
    conn.execute(table5)
    conn.execute(table6)
    conn.execute(table7)
    conn.execute(table8)
    conn.execute(table9)
    conn.execute(table10)
    print("Art Museum DataBase Succesfully Created")
    


if __name__=="__main__":
    createdatabase()
    load_data()
    time.sleep(4)
