#Loading csv file
import pandas as pd
df = pd.read_csv("src/transactions.csv")

"""Data cleaning processes"""

#removing duplicates
df.drop_duplicates(inplace=True)

#removing by specific condition
df=df[df["transaction_status"]!="failed"]
df=df[df["transaction_status"].notna()]

#converting to numeric_type
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['retry_count'] = pd.to_numeric(df['retry_count'], errors='coerce')
df['previous_fraud_flag'] = pd.to_numeric(df['previous_fraud_flag'], errors='coerce')
print(df.dtypes)

#displaying missing values and filling them
df.fillna({
    'location_merchant': 'unknown',
    'transaction_type': 'unknown',
    'merchant_id': 'unknown',
    'merchant_category': 'unknown'
}, inplace=True)

#resetting index
df.reset_index(drop=True, inplace=True)

#writing to cleaned csv file
df.to_csv("src/transactions_cleaned.csv", index=False)

#display of before and after cleaning
before_df = pd.read_csv("src/transactions.csv")
print("\n===== BEFORE CLEANING =====")
print(before_df.head())
print(before_df.info())
print(before_df.isnull().sum())
cleaned_df = pd.read_csv("src/transactions_cleaned.csv")
print("\n===== AFTER CLEANING =====")
print(cleaned_df.head())
print(cleaned_df.info())
print(cleaned_df.isnull().sum())

"""Fraud detection"""
#calculation of diff types of fraud 
threshold = 300000
sus_merchant=['gambling','crypto','unknown']
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['hour'] = df['timestamp'].dt.hour

high_amount_fraud = df[df['amount'] > threshold]
night_fraud = df[(df['hour'] >= 1) & (df['hour'] <= 5)]
retry_fraud = df[df['retry_count'] > 0]
previous_fraud_flag=df[df['previous_fraud_flag'] > 0]
sus_merchant_fraud=df[df['merchant_category'].isin(sus_merchant)]

#Total fraud cases
fraud_cases=pd.concat([
    high_amount_fraud,
    night_fraud,
    retry_fraud,
    previous_fraud_flag,
    sus_merchant_fraud
]).drop_duplicates()
fraud_cases.reset_index(drop=True, inplace=True)

#Generating report for fraud cases
print("\n===== FRAUD DETECTION REPORT =====")
print(f"High amount fraud: {len(high_amount_fraud)}")
print(f"Night time fraud: {len(night_fraud)}")
print(f"Retry fraud: {len(retry_fraud)}")
print(f"Previous fraud flag: {len(previous_fraud_flag)}")
print(f"Suspicious merchant fraud: {len(sus_merchant_fraud)}")
print(f"Total unique fraud cases detected: {len(fraud_cases)}")
print("\nFraud cases are:",fraud_cases)

#writing to fraud cases csv file
fraud_cases.to_csv("src/fraud_cases.csv",index=False)

#calculating risk score and adding risk score & risk level &fraud label to fraud cases csv
fraud_cases['risk_score'] = 0
fraud_cases.loc[fraud_cases['amount'] > threshold, 'risk_score'] += 30
fraud_cases.loc[(fraud_cases['hour'] >= 1) & (fraud_cases['hour'] <= 5), 'risk_score'] += 30
fraud_cases.loc[fraud_cases['retry_count'] > 0, 'risk_score'] += 20
fraud_cases.loc[fraud_cases['previous_fraud_flag'] > 0, 'risk_score'] += 20
fraud_cases.loc[fraud_cases['merchant_category'].isin(sus_merchant), 'risk_score'] += 20

#labels for high risk transactions
fraud_cases['risk_level'] = fraud_cases['risk_score'].apply(lambda x: "HIGH" if x >= 50 else "LOW")
fraud_cases.to_csv("src/fraud_cases.csv",index=False)

#reporting high risk transactions
high_fraud_cases = fraud_cases[fraud_cases['risk_level'] == "HIGH"]
print("\n===== ENHANCED FRAUD DETECTION REPORT =====")
print("High risk transactions:", len(high_fraud_cases))
print("\nFlagged persons:")
print(high_fraud_cases)

#Visualization using graph
import matplotlib.pyplot as plt
fraud_counts = {
    "High Amount": len(high_amount_fraud),
    "Night Time": len(night_fraud),
    "Previous flag": len(previous_fraud_flag),
    "Retry Fraud": len(retry_fraud),
    "Sus merchant": len(sus_merchant_fraud)
}
plt.bar(fraud_counts.keys(), fraud_counts.values())
plt.title("Fraud Cases Summary")
plt.xlabel("Fraud Type")
plt.ylabel("Count")
plt.show()
