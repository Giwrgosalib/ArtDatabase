CREATE TABLE Painting (
	artid INTEGER ,
	Title varchar NOT NULL,
	Creationyear INTEGER,
	ArtPeriod_name varchar,
	ArtistID integer,
	Room varchar,
	Pos_no integer,
	PRIMARY KEY (artid) ,
	FOREIGN KEY (ArtPeriod_name) REFERENCES ArtPeriod(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (ArtistID) REFERENCES Artist(ID)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (Room,Pos_no) REFERENCES Position(Room,Pos_no)
	ON	DELETE	SET NULL	ON	UPDATE		CASCADE,
        UNIQUE(Room, Pos_no)
);

CREATE TABLE Artist (
	ID integer,
	Name varchar NOT NULL,
	Surname varchar,
	Nationality varchar,
	PRIMARY KEY (ID)
);

CREATE TABLE ArtPeriod (
	Name varchar,
	PRIMARY KEY (Name)
);

CREATE TABLE Exhibition (
	ID integer,
	Subject varchar NOT NULL,
	StartDate date NOT NULL,
	EndDate date NOT NULL,
	PRIMARY KEY (ID)
	CONSTRAINT dates CHECK (StartDate<EndDate)
);

CREATE TABLE Associate_Gallery (
	Name varchar, 
	PRIMARY KEY (Name)
);

CREATE TABLE Owned (
	artid integer,
	PRIMARY KEY (artid),
	FOREIGN KEY (artid) REFERENCES Painting(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE
);

CREATE TABLE Loan (
	artid integer,
	LoanStart date NOT NULL,
	LoanEnd date NOT NULL,
	OriginName varchar NOT NULL,
	PRIMARY KEY (artid),
	FOREIGN KEY(artid) REFERENCES Painting(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (OriginName) REFERENCES Associate_Gallery(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	CONSTRAINT dates CHECK (LoanStart<LoanEnd)
	
);

CREATE TABLE Position (
	Room varchar,
	Pos_no integer,
	Storage boolean,
	In_Display boolean,
	PRIMARY KEY (Room,Pos_no),
	CONSTRAINT TWOPLACE CHECK (Storage <> In_Display)
);

CREATE TABLE Takes (
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
);

CREATE TABLE IsDisplayed (
	artid integer,
	ExhibitionId integer,
	PRIMARY KEY (artid, ExhibitionId),
	FOREIGN KEY (artid) REFERENCES Loan(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (ExhibitionId) REFERENCES Exhibition(ID)
	ON	DELETE CASCADE		ON	UPDATE		CASCADE
);











