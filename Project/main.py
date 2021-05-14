from services import TableServices


def main():
    table_service = TableServices()

    # args = list(map(str, input().split()))
    # table_name, col_names = args[0], args[1:]
    table_name, col_names = "sample", ["id", "name"]

    created_table = table_service.create_table(table_name, col_names)
    print(created_table)

    # args = list(map(str, input().split()))
    # table_name, row_values = args[0], args[1:]
    table_name, row_values = "sample", ["123", "veerat"]

    table_service.insert_row(table_name, row_values)

    table_name, new_col_values = "sample", {
        "id": {
            'old_value': "123",
            'new_value': '456'
        },
        "name": {
            'old_value': "veerat",
            "new_value": "new_name"
        }
    }

    table_service.update_row(table_name, new_col_values)



if __name__ == '__main__':
    main()

