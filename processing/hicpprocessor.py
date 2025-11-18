import pandas as pd
import numpy as np

# expand:   "Statistic Label","Year","Commodity Group","UNIT","VALUE"
# to:       "Year", "CategoryName", "CategoryCode", "Root Category", "IsMainCategory", "ParentCategory", "Value"

def main():
    df = pd.read_csv('data/original/hicp.csv')

    # Drop Statistic Label (Static String) & UNIT (Static String)
    df = df.drop(columns=['Statistic Label', 'UNIT'])

    # Split Existing Commodity Group Column
    cg_series = df['Commodity Group']
    cg_series_code = cg_series.str.extract('\(COICOP\s(.*)\)') # Sewerage collection (COICOP 04.4.3) -> 04.4.3
    cg_series_name = cg_series.str.extract('(.*)(?:\s\(.*\))') # Sewerage collection (COICOP 04.4.3) -> Sewerage collection

    print(cg_series_name)

if __name__ == '__main__':
    main()