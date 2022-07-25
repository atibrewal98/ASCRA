USE ASCRA;


-- Drop Table [snp_rating]
Create Table [snp_rating] (
	[snp_rating_id]						[bigint]				PRIMARY KEY IDENTITY(1,1) NOT NULL,
	[value]										[varchar](10)		NOT NULL
)


/**

Insert Into snp_rating Values('AAA')
Insert Into snp_rating Values('AA+')
Insert Into snp_rating Values('AA')
Insert Into snp_rating Values('AA-')
Insert Into snp_rating Values('A+')
Insert Into snp_rating Values('A')
Insert Into snp_rating Values('A-')
Insert Into snp_rating Values('BBB+')
Insert Into snp_rating Values('BBB ')
Insert Into snp_rating Values('BBB-')
Insert Into snp_rating Values('BB+')
Insert Into snp_rating Values('BB')
Insert Into snp_rating Values('BB-')
Insert Into snp_rating Values('B+')
Insert Into snp_rating Values('B')
Insert Into snp_rating Values('B-')
Insert Into snp_rating Values('CCC+')
Insert Into snp_rating Values('CCC ')
Insert Into snp_rating Values('CCC-')
Insert Into snp_rating Values('CC')
Insert Into snp_rating Values('C')
Insert Into snp_rating Values('RD')
Insert Into snp_rating Values('SD')
Insert Into snp_rating Values('D')



*/