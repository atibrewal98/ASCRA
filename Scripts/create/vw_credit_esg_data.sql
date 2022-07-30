USE ASCRA;
GO;


Create or Alter View vw_credit_esg_data As
	Select C.*, R.region_id, R.[value] as [Region], CO.country_name, CO.country_code, M.[value] as [moody], S.[value] as [s&p],
		F.[value] as [fitch]
	From credit_esg_data C
	Left Join country CO on C.country_id = CO.country_id
	Left Join region R on CO.region_id = R.region_id
	Left Join moody_rating M on C.moody_rating_id = M.moody_rating_id
	Left Join snp_rating S on C.snp_rating_id = S.snp_rating_id
	Left Join fitch_rating F on C.fitch_rating_id = F.fitch_rating_id
GO;