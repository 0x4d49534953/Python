import pandas as pd



def GetBillMean(time,day,sex,smoker) -> float :
    le_masque = df["sex"] == sex
    le_masque = le_masque & (df["day"] == day)
    le_masque &= df["smoker"] == smoker
    le_masque &= df["time"] == time
    mean_bill= df[le_masque]["total_bill"].mean()

    return mean_bill

if __name__ == "__main__":
    f = 'datasets/tips.csv'
    df= pd.read_csv(f)
    m = GetBillMean("Lunch","Fri","Male","Yes")
    print(m)
