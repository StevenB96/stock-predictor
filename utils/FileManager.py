import os
import pandas
import concurrent.futures
import multiprocessing


class FileManager:
    def __init__(self):
        self.company_data = []
        self.stock_data = []
        self.combined_data = []

    def santise_data(self):
        combined_data = self.combined_data
        combined_data.sort_values(['Date', 'Ticker'], ascending=[True, True])
        self.combined_data = combined_data

    def combine_data(self):
        print(type(self.stock_data), type(self.company_data))
        merged_df = pandas.merge(
            self.stock_data, self.company_data, left_on='Ticker', right_on='Symbol')
        new_order = [
            'Date', 'Ticker', 'Country',
            'IPO Year', 'Sector', 'Industry',
            'Open', 'High', 'Low',
            'Close', 'Volume', 'OpenInt'
        ]
        merged_df = merged_df.reindex(columns=new_order)
        self.combined_data = merged_df

    def load_stock_file(self, file_path, sep=',', usecols=None):
        try:
            df = self.load_file(file_path, sep, usecols)
            ticker_code = os.path.basename(file_path).split('.')[0].upper()
            country_code = os.path.basename(file_path).split('.')[1].upper()
            df['Ticker'] = ticker_code
            df['Country'] = country_code
            return df
        except:
            return None

    def load_file(self, file_path, sep=',', usecols=None):
        try:
            df = pandas.read_csv(file_path, sep=sep, usecols=usecols)
            return df
        except:
            return None

    def load_data(self):
        self.load_stock_data()
        self.load_company_data()
        self.combine_data()
        self.santise_data()

    def load_stock_data(self):
        # Set the path to the folder that contains the .txt files
        folder_path = './stock_market_data/Stocks'

        # Get a list of the .txt files in the folder
        file_list = os.listdir(folder_path)
        txt_files = [file for file in file_list if file.endswith('.txt')]

        # Use multiprocessing to read files concurrently
        with multiprocessing.Pool() as pool:
            results = pool.map_async(self.load_stock_file, [os.path.join(
                folder_path, file) for file in txt_files])

            # Use multithreading to concatenate the results
            with concurrent.futures.ThreadPoolExecutor() as executor:
                dfs = []
                for df in results.get():
                    if df is not None:
                        executor.submit(dfs.append, df)

        # Concatenate the dataframes into one
        merged_df = pandas.concat(dfs, ignore_index=True)

        self.stock_data = merged_df

    def load_company_data(self):
        # Set the path to the folder that contains the .csv file
        file_path = './stock_market_data/nasdaq_company_data.csv'
        df = self.load_file(file_path, sep=',', usecols=['Symbol', 'IPO Year', 'Sector', 'Industry'])
        self.company_data = df
