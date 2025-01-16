import pandas as pd

class DataPreparation:
    @staticmethod
    def load_data(file_path):
        """Load CSV data into a Pandas DataFrame."""
        return pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")

    @staticmethod
    def validate_data(df):
        """Ensure no missing or invalid data."""
        if df.isnull().values.any():
            raise ValueError("Data contains missing values. Please clean your dataset.")
        return df
