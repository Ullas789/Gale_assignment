CREATE OR REPLACE PROCEDURE test(
    source_db STRING,
    source_schema STRING,
    target_table STRING
)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
DECLARE
    sql_command STRING;
    result_msg STRING;
    truncate_command STRING;
BEGIN
    BEGIN
      LET truncate_command := 'TRUNCATE TABLE ' || target_table || ';';
        EXECUTE IMMEDIATE truncate_command;
        LET sql_command := '
       
            INSERT INTO ' || target_table || '
            
                SELECT
                *
            FROM
                 ' || source_db || '.' || source_schema || '.APPLICABLE_ROLES
            ';

        
        EXECUTE IMMEDIATE sql_command;
        
        CALL SEND_EMAIL_NOTIFICATION_JS(
  'test sucess  ',
  'data loaded success',
  'ullas78999@gmail.com'
);
        
        result_msg := 'Success: Data loaded successfully';


    EXCEPTION
        WHEN STATEMENT_ERROR THEN
            result_msg := 'Statement error: ' || ERROR_MESSAGE();
            CALL SEND_EMAIL_NOTIFICATION_JS(
  'Test failed',
  'sattement errror.',
  'ullas78999@gmail.com'
);

        WHEN OTHER THEN
            result_msg := 'Unexpected error: ' || ERROR_MESSAGE();
                        CALL SEND_EMAIL_NOTIFICATION_JS(
  'Test failed',
  'unexcepted errror.',
  'ullas78999@gmail.com'
);
    END;

    RETURN result_msg;

END;
$$;
