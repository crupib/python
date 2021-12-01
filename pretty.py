from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Month","Earning"]
table.add_rows(
    [
        ["JANUARY",1020],
        ["FEBRUARY", 1233],
        ["MARCH", 1892],
        ["APRIL", 1500]
    ]
)
print(table)                                                                                              
