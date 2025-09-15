def create_uml(tables):
    uml = """
    @startuml

    """
    uml = table_uml(tables, uml)
    uml = fk_uml(tables, uml)
    return uml

def table_uml(tables, uml):
    for tbl in tables:
        tbl_uml = f"entity {tbl.name}" + " {\n"
        for col in tbl.columns:
            col_uml = ""
            if col.is_pk == True:
                col_uml += f"{col.name} : {col.datatype} <<PK>>\n---\n"
            else:
                col_uml += f"{col.name} : {col.datatype}\n"
            tbl_uml += col_uml
        tbl_uml += "}\n"
        uml += tbl_uml
    return uml

def fk_uml(tables,uml):
    for tbl in tables:
        for fk in tbl.fk:
            uml+=f"\n{tbl.name}::{fk.column.name}"+"||--"+"{"+f"{fk.fk_table.title()}::{fk.fk_col}"
    return uml