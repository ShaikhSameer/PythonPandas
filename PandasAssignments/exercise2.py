import pandas as pd

df = pd.read_csv('data/sample_data_2.csv')

print(df)

"""
#
#   remove the duplicates from 'WHO region' column of World alcohol consumption
#
"""

no_duplicates = df.drop_duplicates(subset='WHO region')

print(df)

"""
#
#   find out the alcohol consumption details in the year '1987' or '1989' from the world alcohol consumption
#
"""

year_from_87_89 = df[df['Year'].isin([1987, 1989])]

print(year_from_87_89)

"""
#
#   find out the alcohol consumption details by the 'Americas' in the year '1985' from the world alcohol consumption
#
"""

df_americas_1985 = df[(df['WHO region'] == 'Americas') & (df['Year'] == 1985)]
print(df_americas_1985)

"""
#
#   find out the alcohol consumption details in the year '1986' where WHO region is 'Western Pacific' 
#   and country is 'VietNam' from the world alcohol consumption
#
"""
df_1986_western_pacific_vietnam = df[(df['Year'] == 1986) & (df['WHO region'] == 'Western Pacific') & (df['Country'] == 'VietNam')]
print(df_1986_western_pacific_vietnam)

"""
#
#   find out the alcohol consumption details in the year '1986' or '1989' 
#   where WHO region is 'Americas' from the world alcohol consumption dataset
#
"""

df_americas_86_89 = df[(df['Year'].isin([1986, 1989])) & (df['WHO region'] == 'Americas')]
print(df_americas_86_89)


"""
#
#   find out the alcohol consumption details in the year '1986' or '1989' 
#   where WHO region is 'Americas' or 'Europe' from the world alcohol consumption dataset.
#
"""

df_americas_europe_86_89 = df[(df['Year'].isin([1986, 1989])) & (df['WHO region'].isin(['Americas', 'Europe']))]
print(df_americas_europe_86_89)


"""
#
#   filter those records where WHO region contains "Ea" substring from world alcohol consumption dataset.
#
"""

df_ea_substring = df[df['WHO region'].str.contains("Ea")]
print(df_ea_substring)


"""
#
#   filter those records where WHO region 
#   matches with multiple values (Africa, Eastern Mediterranean, Europe) from world alcohol consumption dataset.
#
"""

filter_regions = ['Africa', 'Eastern Mediterranean', 'Europe']
multiple_regions = df[df['WHO region'].isin(filter_regions)]

print(multiple_regions)


"""
#
#   filter those records which not appears in a given list from world alcohol consumption dataset
#
"""

regions_to_exclude = ['Region1', 'Region2', 'Region3'] 
not_in_list = df[~df['WHO region'].isin(regions_to_exclude)]

print(not_in_list)


