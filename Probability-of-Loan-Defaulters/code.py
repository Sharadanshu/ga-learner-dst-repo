# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

#Task 1

p_a = len(df[df['fico'] > 700])/len(df)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = len(df[(df['fico'] > 700) & (df['purpose'] == 'debt_consolidation')])/len(df[df['fico'] > 700])
def checkindependency(a,b):
    if(a == b):
        return True
    else:
        return False
result = checkindependency(p_a,p_a_b)
print(result)

#Task 2

prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = (len(df[(df['paid.back.loan'] == 'Yes') & (df['credit.policy'] == 'Yes')])/len(df))/prob_lp
bayes = (prob_pd_cs * prob_lp)/prob_cs

#Task 3

df['purpose'].value_counts().plot(kind='bar')
plt.title('Distribution of Purpose')
plt.show()

df1 = df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts().plot(kind='bar')
plt.title('Distribution of Purpose when Paid Back Loan is No')
plt.show()
print(df1.shape)

#Task 4

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

plt.hist(df['installment'], bins=50)
plt.axvline(inst_mean, color='g')
plt.axvline(inst_median, color='b')
plt.legend({'Mean':inst_mean,'Median':inst_median})
plt.title('Distribution of Installment')
plt.show()

plt.hist(df['log.annual.inc'], bins=50)
plt.title('Distribution of Log Annnual Income')
plt.show()



