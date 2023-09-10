import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):
    
    _logger.warning(('-== Migration started ==-'))

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