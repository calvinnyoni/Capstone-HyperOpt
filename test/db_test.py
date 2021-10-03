from db_adapter import CarlSATDB

print("Starting test")

test_con = CarlSATDB()

test_con.create_ancestor_table()

test_con.disconnect()