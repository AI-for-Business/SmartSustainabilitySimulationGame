import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


num_machines_to_read = 5

df_train = pd.DataFrame()

#Read out the sensordata of all machines and put them in one dataframe
for i in range(num_machines_to_read):
    df_temp = pd.read_csv('sensor_data/sensor_data_robot_{}.csv'.format(i), index_col=False)
    df_temp.insert(0, 'Machine', i)
    df_temp.insert(1, 'Cycle', df_temp.index)
    df_train = pd.concat([df_train, df_temp])
    print(len(df_train))

df_train = df_train.reset_index(drop=True)


# For the prediction of time intervalls it is better to revert the ordering of the data [optional]
# So as the next step revert the data so that 0 ist the yet last data point and e.g. -6000 is the first data point [optional]

#iniatial index is due to the revert not longer used so it can be droped
df_train_reverted = df_train.drop(df_train.index)

#to be sure that there are no duplicates in the data, drop them
unit_numbers_train = df_train["Machine"].drop_duplicates()


for u_num in unit_numbers_train:
    #add code here to revert the data [optional]
    df_train_reverted = df_temp


df_train_reverted = df_train_reverted.reset_index(drop=True)

df_train_reverted["Label"] = df_train_reverted.apply(lambda _: "", axis=1)

#Label the data -> in this example all the data has the same label; you have to change this !!
df_train_reverted.loc[df_train_reverted["Cycle"] < 0, "Label"] = "Long"

print(df_train_reverted)

# Do some Preprocessing to get better results (e.g. Rolling Average)
# ADD Preprocessing Code here



# Split your data into train and test 

# Define your classifier and train it
# Tip: Do not forget to optimize the parameters of your classifier



# Create your confusion matrix and save it
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.savefig('matrix' + '.png')