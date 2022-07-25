USE ASCRA;


-- Drop Table [fitch_rating]
Create Table [fitch_rating] (
	[fitch_rating_id]					[bigint]				PRIMARY KEY IDENTITY(1,1) NOT NULL,
	[value]										[varchar](10)		NOT NULL
)


/**

Insert Into fitch_rating Values('AAA')
Insert Into fitch_rating Values('AA+')
Insert Into fitch_rating Values('AA')
Insert Into fitch_rating Values('AA-')
Insert Into fitch_rating Values('A+')
Insert Into fitch_rating Values('A')
Insert Into fitch_rating Values('A-')
Insert Into fitch_rating Values('BBB+')
Insert Into fitch_rating Values('BBB')
Insert Into fitch_rating Values('BBB-')
Insert Into fitch_rating Values('BB+')
Insert Into fitch_rating Values('BB')
Insert Into fitch_rating Values('BB-')
Insert Into fitch_rating Values('B+')
Insert Into fitch_rating Values('B')
Insert Into fitch_rating Values('B-')
Insert Into fitch_rating Values('CCC+')
Insert Into fitch_rating Values('CCC ')
Insert Into fitch_rating Values('CCC-')
Insert Into fitch_rating Values('CC')
Insert Into fitch_rating Values('C')
Insert Into fitch_rating Values('DDD')
Insert Into fitch_rating Values('DD')
Insert Into fitch_rating Values('D')





*/