class Column:
    def __init__(self, name, col_type='string'):
        self.name = name
        self.col_type = col_type

    def __repr__(self):
        return f"Column(name={self.name})"


class Row:
    def __init__(self, value_list):
        # self.table_name = table_name
        self.__ordered_col_values = value_list

    def validate(self):
        pass

    def get_values(self):
        return self.__ordered_col_values

    def update_values(self, new_ordered_value_list):
        self.__ordered_col_values = new_ordered_value_list

    def __str__(self):
        return f"Row(values={self.get_values()})"


class Table:
    def __init__(self, name):
        self.name = name
        self.__columns = []
        self.__col_name_pos_map = {}

    def add_column(self, column: Column):
        self.__columns.append(column)
        self.__col_name_pos_map[column.name] = len(self.__columns) - 1

    def get_columns_list(self):
        return self.__columns

    def get_column_name_pos_map(self):
        return self.__col_name_pos_map

    def __str__(self):
        return f"Table(name={self.name}), columns= {self.get_columns_list()}"



class TableIndex:
    def __init__(self, col_name='id'):
        self.__col_name = col_name

    def get_col_name(self):
        return self.__col_name
