# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here

#Replacing Gender Column
data.Gender.replace('-','Agender',inplace=True)

#Distribution of Gender
data['Gender'].value_counts().plot(kind='bar')
plt.title("Distribution of Gender")
plt.xlabel("Gender")
plt.xticks(rotation = 90)
plt.ylabel("Count")
plt.show()

#Distribution of Alignment
data['Alignment'].value_counts().plot(kind='bar')
plt.title("Distribution of Gender")
plt.xlabel("Gender")
plt.xticks(rotation = 90)
plt.ylabel("Count")
plt.show()

#Correleation betweeen Combat and Strength
plt.scatter(data.Combat,data.Strength)
plt.title('Distribution Between Combat and Strength')
plt.xlabel('Combat')
plt.ylabel('Strength')
plt.show()
covariance_combat_strength = np.cov(data.Combat, data.Strength)[0][1]
pearson_combat_strength = covariance_combat_strength/(np.std(data.Combat) * np.std(data.Strength))

#Correlation between Combat and Intelligence
plt.scatter(data.Combat,data.Intelligence)
plt.title('Distribution Between Combat and Intelligence')
plt.xlabel('Combat')
plt.ylabel('Intelligence')
plt.show()
covariance_combat_intelligence = np.cov(data.Combat, data.Intelligence)[0][1]
pearson_combat_intelligence = covariance_combat_intelligence/(np.std(data.Combat) * np.std(data.Intelligence))

#Best of the best
quantile = data['Total'].quantile(0.99)
best_of_the_best = data[data['Total'] > quantile]
super_best_names = best_of_the_best['Name'].tolist()
print(super_best_names)



