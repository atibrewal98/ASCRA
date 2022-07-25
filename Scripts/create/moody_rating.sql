USE ASCRA;


-- Drop Table [moody_rating]
Create Table [moody_rating] (
	[moody_rating_id]					[bigint]				PRIMARY KEY IDENTITY(1,1) NOT NULL,
	[value]										[varchar](10)		NOT NULL
)


/**

Insert Into moody_rating Values('Aaa')
Insert Into moody_rating Values('Aa1')
Insert Into moody_rating Values('Aa2')
Insert Into moody_rating Values('Aa3')
Insert Into moody_rating Values('A1')
Insert Into moody_rating Values('A2')
Insert Into moody_rating Values('A3')
Insert Into moody_rating Values('Baa1')
Insert Into moody_rating Values('Baa2')
Insert Into moody_rating Values('Baa3')
Insert Into moody_rating Values('Ba1')
Insert Into moody_rating Values('Ba2')
Insert Into moody_rating Values('Ba3')
Insert Into moody_rating Values('B1')
Insert Into moody_rating Values('B2')
Insert Into moody_rating Values('B3')
Insert Into moody_rating Values('Caa1')
Insert Into moody_rating Values('Caa2')
Insert Into moody_rating Values('Caa3')
Insert Into moody_rating Values('Ca')
Insert Into moody_rating Values('C')



*/