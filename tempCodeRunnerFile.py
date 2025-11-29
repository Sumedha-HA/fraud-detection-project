fraud_cases['fraud_label'] = fraud_cases['risk_score'].apply(lambda x: "fraud" if x >= 50 else "safe")
fraud_cases['risk_level'] = fraud_cases['risk_score'].apply(lambda x: "HIGH" if x >= 50 else "LOW")

#writing to fraud cases csv file
fraud_cases.to_csv("fraud_cases.csv",index=False)

high_fraud_cases = fraud_cases[fraud_cases['fraud_label'] == "fraud"]
print("\n===== ENHANCED FRAUD DETECTION REPORT =====")
print("Total flagged rows:", len(high_fraud_cases))
print("High risk transactions:", sum(fraud_cases['risk_score'] >= 50))
print("Flagged persons:")
print(high_fraud_cases)