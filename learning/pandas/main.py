import pandas as pd
 
def second_highest_salary(employee:pd.DataFrame)-> pd.DataFrame:
    #(employee: pd.DataFrame) 和 -> pd.DataFrame 
    # 是 Python 函数的类型提示（Type Hinting）部分，
    # 用于提供函数参数和返回值的类型信息
    
    # (employee: pd.DataFrame):参数类型提示,
    # 该参数的类型应该是 pd.DataFrame，也就是 Pandas 数据帧
    # 它告诉你这个函数接受一个名为 employee 的参数
    # -> pd.DataFrame：这部分是函数的返回值类型提示。
    # 它告诉你这个函数返回一个 Pandas 数据帧，类型为 pd.DataFrame
    
    #按照工资降序排序
    employee=employee.sort_values(by='salary',ascending=False)
    
    #去掉重复的工资
    employee=employee.drop_duplicates(subset='salary',keep='first')

    
    #选择第N高工资，如果不存在则返回null
    if len(employee)>=2:
        return pd.DataFrame({'SecondHighestSalary': [employee.iloc[1]['salary']]})
        # pd.DataFrame({})：这部分代码创建了一个新的空DataFrame对象，使用Pandas库的pd.DataFrame()构造函数。
        #内部的字典{'SecondHighestSalary': [int(employee.iloc[1]['salary'])]}：
        # 这个字典包含一个键值对，其中键是"SecondHighestSalary"，
        # 值是一个包含一个元素的列表。这个元素是从名为"employee"的
        # DataFrame中提取的第二行的"salary"列的值，并将其强制转换为整数
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    
    
    
    