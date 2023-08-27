import os
import pandas


class FileManager:
    def __init__(self):
        pass

    def load_stock_data(self):
        # Set the path to the folder that contains the .txt files
        folder_path = '/path/to/folder/'

        # Get a list of the .txt files in the folder
        file_list = os.listdir(folder_path)
        txt_files = [file for file in file_list if file.endswith('.txt')]

        # Loop through the .txt files and create a DataFrame for each one
        dfs = []
        for file in txt_files:
            file_path = os.path.join(folder_path, file)
            df = pandas.read_csv(file_path, sep='\t')
            dfs.append(df)
        pass

    def load_company_data(self):
        pass
