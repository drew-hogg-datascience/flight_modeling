import pandas as pd
import glob as glob
import re

DATA_DIR = '../data/'
DATA_FILE = 'united_flight_data.csv'


def main():

    count = 0 # Row counter

    ### Read in acquisition data and setup dataframe ###
    file_list = glob.glob(DATA_DIR+'*ONTIME*.csv')

    data_list = []
    for file_name in file_list:
        print 'Reading File %s' %file_name
        data = pd.read_table(file_name, sep=",")
        count += data['FL_NUM'].count()
        data = data[data['CARRIER'] == 'UA']
        data = data.drop(['Unnamed: 12'], axis=1)
        data_list.append(data)

    full_data = pd.concat(data_list)
    #full_data.sort_values(by='FL_DATE')
    print full_data.head()
    print 'Saving to %s' %(DATA_DIR+DATA_FILE)
    full_data.to_csv(DATA_DIR+DATA_FILE)

    print 'Finished reduction.  Total rows processed = %s' %count
