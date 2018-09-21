import pandas as pd


'''
Script to convert Digital Commons generated Excel metadata to CSV format. The CSV format currently
follows the template model from the datacite_csv_xml project https://github.com/Estella123/datacite_csv_xml
'''

# Set the path and open the DC Excel metadata

dpath = './data/'

dc_out = 'energizenm_subset.xls'

fpath = dpath + dc_out

df = pd.read_excel(fpath)

'''
Generate the XML and/or mint DOIs

1. Map DC Excel fields to categories in the incorporated project
2. Map categories to their column ids in the incorporated csv metadata template
3. Output to CSV per template

Start with required fields, in order given in DC Excel
Mapping model (for now) is {template_column_id : {template_category: mapped_DC_Excel_field}}

'''

metadata_mapping = {}
metadata_mapping[1] = {"identifier": ""}    # this is a required field, need to decide about generating DOIs

# Titles - repeatable in Datacite, unique in DC

metadata_mapping[3] = {"titles": {"title"}}

# Creators - repeatable in DC and DataCite
# Datacite schema in template is "creatorName|NameType|affiliation|nameIdentifier|nameIdentifierScheme"
# metadata_mapping[2] = {creators: {1: [creator_info], 2: [creator_info], etc.}}

