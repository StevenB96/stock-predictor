import utils

if __name__ == '__main__':
    class Main:
        file_manager = utils.FileManager()
        file_manager.load_data()
        print(file_manager.combined_data.loc[file_manager.combined_data['Ticker'] == 'A'])

