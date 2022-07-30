/*------------------------------------------------------------------
	Exec [sp_insert_update_country]		'Taiwan', 'TWN', 2
------------------------------------------------------------------**/

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
GO;

CREATE OR ALTER PROCEDURE [sp_insert_update_country] (
	@country_name			varchar(100),
	@country_code			varchar(10),
	@region_id				bigint
)
AS
Begin
	BEGIN TRANSACTION;

	If Exists (Select country_id From [country] Where country_name = @country_name)
	Begin
		Update [country]
		Set
			[country_code] = @country_code,
			[region_id] = @region_id
		Where country_name = @country_name
	End
	Else Begin
		Insert Into country
		Values(@country_name, @country_code, @region_id)
	End

	IF @@IDENTITY is NULL or @@IDENTITY <= 0
		ROLLBACK TRANSACTION
	ELSE
		COMMIT

End