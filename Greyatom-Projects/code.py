# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

data.replace("-","Agender",inplace=True)

gender_count = data['Gender'].value_counts()

gender_count.plot.bar()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.title("Character Alignment")
alignment.plot.pie()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]

sc_covariance = sc_df.cov().iloc[0,1]

sc_strength = sc_df.iloc[:,0].std()
sc_combat = sc_df.iloc[:,1].std()

sc_pearson = sc_covariance/(sc_strength*sc_combat)

ic_df = data[['Intelligence','Combat']]

ic_covariance = ic_df.cov().iloc[0,1]

ic_intelligence = ic_df.iloc[:,0].std()
ic_combat = ic_df.iloc[:,1].std()

ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

print("R(Str,Com) = ", sc_pearson)
print("R(Int,Com) = ", ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)

super_best = data[data['Total'] > total_high]

print(super_best)

super_best_names = list(super_best['Name'].values)

print(super_best_names)


# --------------
#Code starts here
fig,ax = plt.subplots(nrows = 2,ncols=2 , figsize=(4,4))

ax_1 = ax[0,0].boxplot(data['Intelligence'])
ax[0,0].set_title('Intelligence')

ax_2 = ax[0,1].boxplot(data['Speed'])
ax[0,1].set_title('Speed')

ax_3 = ax[1,0].boxplot(data['Power'])
ax[1,0].set_title('Power')

plt.show()


