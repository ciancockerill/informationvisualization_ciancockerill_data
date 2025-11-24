import pandas as pd
import numpy as np

# Add countygroup to standardize for geographic map + multiselect

def to_county_group(area):
    # Dublin Handler 
    dublin_areas = [
        "Dublin City",
        "South Dublin",
        "Fingal",
        "Dun Laoghaire-Rathdown",
        "Dún Laoghaire-Rathdown"
    ]

    if area in dublin_areas:
        return "Dublin"

    # Base cleaning for all counties
    area_clean = area.replace(" City", "").replace(" County", "")

    # Tipperary handler
    if area_clean in ["North Tipperary", "South Tipperary"]:
        return "Tipperary"

    return area_clean


def main():
    df = pd.read_csv('Stillbirth_and_Infant_Mort_per_1000/data/original/saimpt.csv')
    df['CountyGroup'] = df['Area of Residence'].apply(to_county_group)

    df = df.dropna(subset=["VALUE"])
    df = df[df["VALUE"].astype(str).str.strip() != ""]

    df.to_csv('Stillbirth_and_Infant_Mort_per_1000/data/cleaned/saimpt.csv', index=False)


    print(df)


if __name__ == '__main__':
    main()

