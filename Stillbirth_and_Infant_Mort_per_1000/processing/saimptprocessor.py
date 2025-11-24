import pandas as pd
import numpy as np

# Map to TopoJSON name for joining

def to_topojson_mapping(area):
    if pd.isna(area):
        return area

    area = str(area).strip()

    # Whitelist of names that already match TopoJSON exactly
    whitelist = [
        "Dublin City",
        "South Dublin",
        "Fingal",
        "Dun Laoghaire-Rathdown",
        "Dún Laoghaire-Rathdown",
        "North Tipperary",
        "South Tipperary"
    ]

    if area in whitelist:
        return area

    if area.endswith(" City") or area.endswith(" County"):
        return area

    return f"{area} County"


def main():
    df = pd.read_csv('Stillbirth_and_Infant_Mort_per_1000/data/original/saimpt.csv')

    df['TopoJsonMapping'] = df['Area of Residence'].apply(to_topojson_mapping)

    df = df.dropna(subset=["VALUE"])
    df = df[df["VALUE"].astype(str).str.strip() != ""]

    df.to_csv('Stillbirth_and_Infant_Mort_per_1000/data/cleaned/saimpt.csv', index=False)

    print(df)


if __name__ == '__main__':
    main()
