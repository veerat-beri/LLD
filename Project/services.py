from collections import defaultdict

from exceptions import TableNotFoundException, InvalidColumnException, RecordNotFoundException
from model import Column, Table, Row


class TableServices:
    tables_rows = defaultdict(list)
    tables_record = {}

    def create_table(self, table_name, col_names: []):
        print("Creating Table")
        table = Table(table_name)
        for col_name in col_names:
            print("adding column: ", col_name)
            table.add_column(Column(col_name))

        TableServices.tables_record[table_name] = table
        return table

    def _get_table(self, table_name):
        table = TableServices.tables_record.get(table_name)
        if not table:
            raise TableNotFoundException(f"{table_name} not found")
        return table

    def insert_row(self, table_name, col_values_list):
        print("Inserting Row")
        self._get_table(table_name)

        # can add validation logic

        row = Row(col_values_list)
        TableServices.tables_rows[table_name].append(row)
        print("Inserted row: ", row)

    def __is_required_row(self, row, col_values_map, table_col_pos_map):
        for col_name in col_values_map:
            table_col_pos = table_col_pos_map.get(col_name)
            if table_col_pos is None:
                raise InvalidColumnException(f"{col_name} doesn't exists")

            col_val = row.get_values()[table_col_pos]
            if col_val == col_values_map[col_val]:
                continue
            return False

        return True

    def _get_old_new_col_values(self, col_name, new_col_values_map):
        return new_col_values_map[col_name]['old_value'], new_col_values_map[col_name]['new_value']

    def _find_row(self, table_name, table_col_pos_map, new_col_values_map):
        for row in TableServices.tables_rows[table_name]:
            for col_name in new_col_values_map:
                table_col_pos = table_col_pos_map.get(col_name)
                if table_col_pos is None:
                    raise InvalidColumnException(f"{col_name} doesn't exists")
                col_val = row.get_values()[table_col_pos]
                if col_val == self._get_old_new_col_values(col_name, new_col_values_map)[0]:
                    if self.__is_required_row(row, new_col_values_map, table_col_pos_map):
                        return row
        return

    def __get_ordered_col_values(self, new_col_values_map, table_col_order):
        return []

    def update_row(self, table_name, new_col_values_map):
        print("\nUpdating Row with values: ", new_col_values_map)
        table = self._get_table(table_name)
        table_col_pos_map = table.get_column_name_pos_map()
        required_row = self._find_row(table_name, table_col_pos_map, new_col_values_map)

        print("required row to be updated: ", required_row)

        if not required_row:
            raise RecordNotFoundException(f"required record not found")

        new_ordered_values = self.__get_ordered_col_values(new_col_values_map, table.get_columns_list())
        self.__update_row(required_row, new_ordered_values)

    def __update_row(self, row, new_ordered_value_list):
        row.update_values(new_ordered_value_list)
        print("Updated row: ", row)














