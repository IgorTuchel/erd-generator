class Column():
    def __init__(self, name, is_pk, datatype):
        self.name = name
        self.is_pk = is_pk
        self.datatype = datatype

class ForeignKey():
    def __init__(self, col=None,fk_table=None,fk_col=None):
        self.column = col
        self.fk_table = fk_table
        self.fk_col = fk_col

class Table():
    def __init__(self, name):
        self.name = name
        self.columns = []
        self.fk = []

    def add_column(self, col):
        self.columns.append(col)

    def add_fk(self,fk):
        self.fk.append(fk)