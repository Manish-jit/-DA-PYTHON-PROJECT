import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Train.csv'
df = pd.read_csv(file_path)

print("### Descriptive Statistics ###")
print(df.describe())

print("\n### Correlation Matrix ###")
numeric_cols = df.select_dtypes(include=['number'])  
correlation_matrix = numeric_cols.corr()  
print(correlation_matrix)

print("\n### On-Time vs Late Deliveries ###")
on_time_distribution = df['Reached.on.Time_Y.N'].value_counts()
print(f"On-Time Deliveries: {on_time_distribution[1]}")
print(f"Late Deliveries: {on_time_distribution[0]}")

labels = ['Late Deliveries', 'On-Time Deliveries']
sizes = [on_time_distribution[0], on_time_distribution[1]]
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
plt.title("On-Time vs Late Deliveries")
plt.show()

print("\n### Shipment Mode vs On-Time Delivery ###")
shipment_mode_on_time = df.groupby(['Mode_of_Shipment', 'Reached.on.Time_Y.N']).size().unstack()
print(shipment_mode_on_time)

shipment_mode_on_time.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Mode of Shipment vs On-Time Delivery")
plt.xlabel("Mode of Shipment")
plt.ylabel("Count")
plt.legend(title="Reached on Time (1 = Yes, 0 = No)")
plt.show()

print("\n### Warehouse Block vs On-Time Delivery ###")
warehouse_block_on_time = df.groupby(['Warehouse_block', 'Reached.on.Time_Y.N']).size().unstack()
print(warehouse_block_on_time)

warehouse_block_on_time.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Warehouse Block vs On-Time Delivery")
plt.xlabel("Warehouse Block")
plt.ylabel("Count")
plt.legend(title="Reached on Time (1 = Yes, 0 = No)")
plt.show()

print("\n### Analysis of Discounts Offered ###")
plt.figure(figsize=(10, 6))
sns.barplot(x='Reached.on.Time_Y.N', y='Discount_offered', data=df, estimator=sum, ci=None)
plt.title("Total Discount Offered vs Delivery Time")
plt.xlabel("Reached on Time (1 = Yes, 0 = No)")
plt.ylabel("Total Discount Offered")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Mode_of_Shipment', hue='Reached.on.Time_Y.N', data=df)
plt.title("Mode of Shipment vs Delivery Time")
plt.xlabel("Mode of Shipment")
plt.ylabel("Count")
plt.legend(title="Reached on Time (1 = Yes, 0 = No)")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Warehouse_block', hue='Reached.on.Time_Y.N', data=df)
plt.title("Warehouse Block vs Delivery Time")
plt.xlabel("Warehouse Block")
plt.ylabel("Count")
plt.legend(title="Reached on Time (1 = Yes, 0 = No)")
plt.show()



print("\n### Customer Rating vs On-Time Delivery ###")
customer_rating_on_time = df.groupby(['Customer_rating', 'Reached.on.Time_Y.N']).size().unstack()
print(customer_rating_on_time)

customer_rating_on_time.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Customer Rating vs Delivery Time")
plt.xlabel("Customer Rating")
plt.ylabel("Count")
plt.legend(title="Reached on Time (1 = Yes, 0 = No)")
plt.show()



print("\n### Product Importance vs On-Time Delivery ###")
product_importance_on_time = df.groupby(['Product_importance', 'Reached.on.Time_Y.N']).size().unstack()
print(product_importance_on_time)

product_importance_on_time.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Product Importance vs Delivery Time")
plt.xlabel("Product Importance")
plt.ylabel("Count")
plt.legend(title="Reached on Time (1 = Yes, 0 = No)")
plt.show()

print("\n### Gender vs On-Time Delivery ###")
gender_on_time = df.groupby(['Gender', 'Reached.on.Time_Y.N']).size().unstack()
print(gender_on_time)

gender_on_time.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Gender vs Delivery Time")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Reached on Time (1 = Yes, 0 = No)")
plt.show()

print("\n### Product Weight vs On-Time Delivery ###")
plt.figure(figsize=(10, 6))
sns.barplot(x='Reached.on.Time_Y.N', y='Weight_in_gms', data=df, estimator=sum, ci=None)
plt.title("Total Product Weight vs Delivery Time")
plt.xlabel("Reached on Time (1 = Yes, 0 = No)")
plt.ylabel("Total Weight in gms")
plt.show()

print("\n### Discount Offered vs Customer Rating ###")
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer_rating', y='Discount_offered', data=df, estimator=sum, ci=None)
plt.title("Total Discount Offered vs Customer Rating")
plt.xlabel("Customer Rating")
plt.ylabel("Total Discount Offered")
plt.show()

print("\n### Product Importance vs Discount Offered ###")
plt.figure(figsize=(10, 6))
sns.barplot(x='Product_importance', y='Discount_offered', data=df, estimator=sum, ci=None)
plt.title("Total Discount Offered vs Product Importance")
plt.xlabel("Product Importance")
plt.ylabel("Total Discount Offered")
plt.show()
