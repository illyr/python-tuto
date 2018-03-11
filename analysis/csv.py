#! /usr/bin/env python3
# coding: utf-8

import os
import pprint
import logging as lg

import pandas as pd
import matplotlib
matplotlib.use('TkAgg') # you need this if you are on MacOS
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns # Pimp my Matplotlib

class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f pourcents"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result

def launch_analysis(data_file, by_party = False):
    sopm = SetOfParliamentMembers("All MPs")

    directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
    # with this path, we go inside the folder `data` and get the file.
    path_to_file = os.path.join(directory, "data", data_file) 
   
    sopm.data_from_csv(path_to_file)
    sopm.display_chart()
    print("===")
    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()


       
if __name__ == "__main__":
    launch_analysis('current_mps.csv')