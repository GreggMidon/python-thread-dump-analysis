"""
Name....: sqlrepo.py
Date....: 06/17/2017
Author..: Gregg Midon
Desc....: Repository of SQL statements used by the main application.
"""

sqlids = """
select  distinct
        inst_id,
        session_id,
        session_serial#,
        sql_id
from    anf_ash_sql_id 
where   sql_id is not null
order by session_id,session_serial#
"""

