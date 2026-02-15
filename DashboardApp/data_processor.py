import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Load the dataset from the given Excel file."""  
        self.df = pd.read_excel(self.file_path)
        print(f"Data loaded successfully from {self.file_path}")

    def clean_data(self):
        """Clean the dataset by removing NaN values and duplicates."""  
        self.df.dropna(inplace=True)  
        self.df.drop_duplicates(inplace=True)  
        print("Data cleaned: NaN values and duplicates removed.")

    def process_data(self):
        """Process the data applying CIIU4 normalization."""  
        # Example of CIIU4 normalization: Assuming a mapping function or dict
        # For demonstration, I'm just normalizing assuming a specific column exists
        ciuu_mapping = {"example_value": "normalized_value"}  # Define your CIIU4 mapping
        if 'CIIU4' in self.df.columns:
            self.df['CIIU4'] = self.df['CIIU4'].map(ciuu_mapping)
            print("Data processed using CIIU4 normalization.")
        else:
            print("CIIU4 column not found in the data.")

    def get_processed_data(self):
        """Return the processed DataFrame."""  
        return self.df
