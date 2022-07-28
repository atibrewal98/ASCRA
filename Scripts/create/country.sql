USE ASCRA;


-- Drop Table [country]
Create Table [country] (
	[country_id]						[bigint]						NOT NULL PRIMARY KEY IDENTITY (1,1) ,
	[country_name]					[varchar](200)			NOT NULL,
	[country_code]					[varchar](10)				NOT NULL,
	[region_id]							[bigint]						NULL FOREIGN KEY References [region]([region_id])
)
