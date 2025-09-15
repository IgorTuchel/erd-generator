from tables import Table, Column, ForeignKey

def extract_tables(cursor, tables):
    tbl_arr = []
    for table in tables:
        tbl_arr.append(create_tables(table,cursor))
    return tbl_arr

def create_tables(table, cursor):
    table_name = table[0].title()
    new_tbl = Table(name=table_name)
    
    # Get column information
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()

    for col in columns:
        new_tbl.add_column(create_column(col))

    cursor.execute(f"PRAGMA foreign_key_list({table_name});")
    foreign_keys = cursor.fetchall()
    if foreign_keys:
        for fk in foreign_keys:
            new_tbl.add_fk(create_fk(fk,new_tbl))
    return new_tbl

def create_column(col):
    name = col[1]
    data_type = col[2]
    is_pk = bool(col[5])
    col = Column(name,is_pk,data_type)
    return col

def create_fk(fk, tbl):
    local_field_name = fk[3]
    foreign_table_name = fk[2]
    foreign_field_name = fk[4]
    fk_col = None
    for col in tbl.columns:
        if col.name == local_field_name:
            fk_col = col
            break
    foreign_key = ForeignKey(fk_col,foreign_table_name,foreign_field_name)
    return foreign_key