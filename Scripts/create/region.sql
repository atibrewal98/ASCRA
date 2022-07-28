USE ASCRA;


-- Drop Table [region]
Create Table [region] (
	[region_id]								[bigint]				PRIMARY KEY IDENTITY(1,1) NOT NULL,
	[value]										[varchar](10)		NOT NULL
)


/**

Insert Into region Values('Americas')
Insert Into region Values('APAC')
Insert Into region Values('Africa')
Insert Into region Values('Europe')



*/