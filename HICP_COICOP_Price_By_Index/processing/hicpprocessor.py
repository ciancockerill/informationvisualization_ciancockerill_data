import pandas as pd
import numpy as np

# expand:   "Statistic Label","Year","Commodity Group","UNIT","VALUE"
# to:       "Year", "CommodityName", "CommodityCode", "IsMainCommodity", "ParentCommodity", "Value"

def main():
    df = pd.read_csv('HCIP_COICOP_Price_By_Index/data/original/hicp.csv')

    # Drop Statistic Label (Static String) & UNIT (Static String)
    df = df.drop(columns=['Statistic Label', 'UNIT'])

    # Split Existing Commodity Group Column
    cg_series = df['Commodity Group']
    cg_series_code = cg_series.str.extract(r'\(COICOP\s(.*)\)') # Sewerage collection (COICOP 04.4.3) -> 04.4.3
    cg_series_name = cg_series.str.extract(r'(.*)(?:\s\(.*\))') # Sewerage collection (COICOP 04.4.3) -> Sewerage collection

    df = df.drop(columns=['Commodity Group'])
    df['CommodityName'] = cg_series_name
    df['CommodityCode'] = cg_series_code

    # IsMainCommodity if Code contains a period (subcategory delimiter)
    df["IsMainCommodity"] = (df["CommodityCode"].str.count(r"\.") == 0).astype(int)

    # Gets Parent Commodity if not link it to 00 which is "Overall HPIC" commodity
    df["ParentCommodity"] = df["CommodityCode"].str.split(".").str[0]
    df.loc[df["IsMainCommodity"] == 1, "ParentCommodity"] = "00"

    # Drop if value = NA or 0
    df = df.dropna(subset=["VALUE"])
    df = df[df["VALUE"] != 0]

    # Order Columns
    order = [
        "CommodityCode",
        "CommodityName",
        "Year",
        "IsMainCommodity",
        "ParentCommodity",
        "VALUE"
    ]

    df = df[order]

    df.to_csv('HCIP_COICOP_Price_By_Index/data/cleaned/hicp.csv', index=False)


if __name__ == '__main__':
    main()