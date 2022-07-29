''' creating a dataframe with the help of dictionaries '''
pr={"1":[1,2,3,4],
       "2":["pravalika","rajesh","varun","niharika"],
       "3":["python","Full Stack","java","Advance Python"],
       "4":["feb","oct","july","aug"]
       }

# print(pr,type(pr))
# import pandas as pd
# df2=pd.DataFrame(pr)
# print(df2)

''' we now create a dataframe with the help of tuples '''
# import pandas as pd
# a=[(10,"prava",),(11,"rajesh","falaknama"),(13,"akhilcj6","kerela"),(14,"pravalika","hyderabad")]
# df3=pd.DataFrame(a,columns=["id","name","place"])
# print(df3)

# import pandas as pd
# f=pd.read_csv('10b.csv')
# print(f)

# import pandas as pd
# f=pd.read_excel('b100.xlsx')
# print(f)


# import pandas
# b=pandas.read_csv("B5.csv")
# print(b)
# print(b.shape) # shape method will show how many rows and columns
# print(b.head()) # head method will show first 5 rows data
# print(b.tail())  # tail method will print last 5 rows data
# print(b.head(1))
# print(b.tail(3))
# print(b[:]) # it will print all the rows in the table
# print(b[2:6])
# print(b[1:4])
# print(b.columns)
# print(b.Place)
# print(b[['Place','Name']])
# print(b)
# print(b['sal'].max())
# print(b['sal'].min())
# print(b.describe())
# print(b[b.sal>400])
# print(b['Place'][b.sal>400])
# print(b[b.sal<450])
# print(b[b.sal==b.sal.max()])
# print(b)
# print(b.loc[5])
# b1=b.set_index('ID')
# print(b1)


# print(dir(pandas))
# print(len(['BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame',
# 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Flags', 'Float32Dtype', 
# 'Float64Dtype', 'Float64Index', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 'Int16Dtype', 'Int32Dtype',
# 'Int64Dtype', 'Int64Index', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 'MultiIndex',
# 'NA', 'NaT', 'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 'Series', 'SparseDtype',
# 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype',
# 'UInt64Index', 'UInt8Dtype', '__builtins__', '__cached__', '__doc__', '__docformat__', '__file__',
# '__getattr__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__',
# '__version__', '_config', '_hashtable', '_is_numpy_dev', '_lib', '_libs', '_np_version_under1p18',
# '_testing', '_tslib', '_typing', '_version', 'api', 'array', 'arrays', 'bdate_range', 'compat',
# 'concat', 'core', 'crosstab', 'cut', 'date_range', 'describe_option', 'errors', 'eval', 'factorize',
# 'get_dummies', 'get_option', 'infer_freq', 'interval_range', 'io', 'isna', 'isnull','json_normalize', 
# 'lreshape', 'melt', 'merge', 'merge_asof', 'merge_ordered', 'notna', 'notnull','offsets', 'option_context',
# 'options', 'pandas', 'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard',
# 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json',
# 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 'read_sql','read_sql_query',
# 'read_sql_table', 'read_stata', 'read_table', 'read_xml', 'reset_option', 'set_eng_float_format', 
# 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 'to_numeric', 
# 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts','wide_to_long']))