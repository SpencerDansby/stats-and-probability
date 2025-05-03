import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(by=['emp_id', 'event_day'], as_index=False)['total_time'].sum()
        

accounts = pd.DataFrame({
    'emp_id': [1,1,1,2,2],
    'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
    'in_time': [4, 55, 1, 3, 47],
    'out_time': [32, 200, 42, 33, 74]
})

print(total_time(accounts))

# Input: 
# Employees table:
# +--------+------------+---------+----------+
# | emp_id | event_day  | in_time | out_time |
# +--------+------------+---------+----------+
# | 1      | 2020-11-28 | 4       | 32       |
# | 1      | 2020-11-28 | 55      | 200      |
# | 1      | 2020-12-03 | 1       | 42       |
# | 2      | 2020-11-28 | 3       | 33       |
# | 2      | 2020-12-09 | 47      | 74       |
# +--------+------------+---------+----------+
