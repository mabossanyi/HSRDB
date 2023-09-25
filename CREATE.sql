/* 
	Author: Marc-Andre Bossanyi
	Email: ma.bossanyi@gmail.com
	Creation Date: 2023/09/24
	Last Updated: 2023/09/24
*/

-- Script CREATE for the table "Type"
CREATE TABLE Type(
	idType SERIAL NOT NULL, 
	name VARCHAR(20) NOT NULL,
	isDeleted BOOL NOT NULL,
	CONSTRAINT pk_idType PRIMARY KEY (idType)
);


-- Script CREATE for the table "Path"
CREATE TABLE Path(
	idPath SERIAL NOT NULL,
	name VARCHAR(25) NOT NULL,
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idPath PRIMARY KEY (idPath)
);


-- Script CREATE for the table "Character"
CREATE TABLE Character(
	idCharacter SERIAL NOT NULL,
	name VARCHAR(30) NOT NULL, 
	rarity INT NOT NULL,
	idType INT NOT NULL,
	idPath INT NOT NULL, 
	isOwned BOOL NOT NULL,
	isDeleted BOOL NOT NULL,
	CONSTRAINT pk_idCharacter PRIMARY KEY (idCharacter),
	CONSTRAINT fk_idType FOREIGN KEY (idType) REFERENCES Type(idType),
	CONSTRAINT fk_idPath FOREIGN KEY (idPath) REFERENCES Path(idPath)
);


-- Script CREATE for the table "Stat"
CREATE TABLE Stat(
	idStat SERIAL NOT NULL, 
	name VARCHAR(20) NOT NULL,
	description VARCHAR(30) NOT NULL,
	isDeleted BOOL NOT NULL,
	CONSTRAINT pk_idStat PRIMARY KEY (idStat)
);

-- Script CREATE for the table "Slot"
CREATE TABLE Slot(
	idSlot SERIAL NOT NULL, 
	name VARCHAR(15) NOT NULL, 
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idSlot PRIMARY KEY (idSlot)
);


-- Script CREATE for the table "CharacterStat"
CREATE TABLE CharacterStat(
	idCharacter INT NOT NULL, 
	idSlot INT NOT NULL, 
	idStat INT NOT NULL, 
	CONSTRAINT pk_idCharacterStat PRIMARY KEY (idCharacter, idSlot),
	CONSTRAINT fk_idCharacter FOREIGN KEY (idCharacter) REFERENCES Character(idCharacter),
	CONSTRAINT fk_idSlot FOREIGN KEY (idSlot) REFERENCES Slot(idSlot),
	CONSTRAINT fk_idStat FOREIGN KEY (idStat) REFERENCES Stat(idStat)
);


-- Script CREATE for the table "Item"
CREATE TABLE Item(
	idItem SERIAL NOT NULL,
	name VARCHAR(40) NOT NULL,
	isDeleted BOOL NOT NULL,
	CONSTRAINT pk_idItem PRIMARY KEY (idItem)
);


-- Script CREATE for the table "CharacterItem"
CREATE TABLE CharacterItem(
	idCharacter INT NOT NULL, 
	idSlot INT NOT NULL, 
	idItem INT NOT NULL,
	CONSTRAINT pk_CharacterItem PRIMARY KEY (idCharacter, idSlot, idItem),
	CONSTRAINT fk_idCharacter FOREIGN KEY (idCharacter) REFERENCES Character(idCharacter),
	CONSTRAINT fk_idSlot FOREIGN KEY (idSlot) REFERENCES Slot(idSlot),
	CONSTRAINT fk_idItem FOREIGN KEY (idItem) REFERENCES Item(idItem)
);