import pandas as pd

PC_Extract = pd.read_csv (r'E:\MOSIAC\IN DATA\PC_Extract.csv')
M_Fields = pd.read_csv (r'E:\MOSIAC\IN DATA\M_Fields_Lookup.csv')

#renaming fields

PC_Extract.rename(columns={ PC_Extract.columns[0]: "Postcode_1" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[1]: "Postcode_2" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[3]: "Mosaic_7_Group" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[4]: "Mosaic_7_Type" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[7]: "HH_Estimate" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[8]: "Population" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[9]: "Adults_15plus" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[10]: "Adults_18plus" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[11]: "X" }, inplace = True)
PC_Extract.rename(columns={ PC_Extract.columns[12]: "Y" }, inplace = True)

#adding new field for Postcode

PC_Extract ["Postcode_NoSpaces"] = PC_Extract ["Postcode_1"]

#removing blank space in postcode field

PC_Extract["Postcode_NoSpaces"] = PC_Extract["Postcode_NoSpaces"].str.replace(' ', '')

#moving postcode column to first column and removing non required columns

PC_Extract = PC_Extract[['Postcode_NoSpaces','Postcode_1','Postcode_2','Mosaic_7_Type','Mosaic_7_Group','HH_Estimate','Population','Adults_15plus','Adults_18plus','X','Y']]

#PC_Extract.join (M_Fields,on=str,how='left',lsuffix="Mosaic_7_Type",rsuffix="JOIN___Mosaic_7_Type", sort=False)

out = pd.merge(PC_Extract,M_Fields, how = 'left', left_on = ['Mosaic_7_Type'],right_on= ['JOIN___Mosaic_7_Type'])

out.to_csv(r'E:\MOSIAC\IN DATA\PC_Extract_Joined.csv')
