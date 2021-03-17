CREATE TABLE Meetings(
    Name text PRIMARY KEY  
    DateCreated DATETIME NOT NULL DEFAULT(GETDATE())  
);