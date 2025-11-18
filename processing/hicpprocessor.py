import pandas as pd
import numpy as np

# expand:   "Statistic Label","Year","Commodity Group","UNIT","VALUE"
# to:       "Year", "CategoryName", "CategoryCode", "Root Category", "IsMainCategory", "ParentCategory", "Value"

def main():
    df = pd.read_csv('data/original/hicp.csv')


if __name__ == '__main__':
    main()