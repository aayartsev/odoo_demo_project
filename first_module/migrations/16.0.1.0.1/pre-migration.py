def migrate(cr, version):
    """   Update first_model table   """
    query = """
    DO $$
        BEGIN
        IF EXISTS(SELECT *
            FROM information_schema.columns
            WHERE table_name='first_model' and column_name='field_one' )
        THEN
            ALTER TABLE first_model RENAME COLUMN
                field_one TO field_three;
        END IF;
    END $$;
    """
    cr.execute(query)