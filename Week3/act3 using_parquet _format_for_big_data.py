# Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format.
# Then, compute the maximum, minimum, average, and absolute values for each column in the dataset. 
# (see link to download a big numerical data in csv format from link: https://archive.ics.uci.edu/datasets)

#Before running that, install ucimlrepo using pip
from ucimlrepo import fetch_ucirepo 
import pandas as pd
  
# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
df = pd.concat([X, y], axis=1)
  
df.to_csv("Week3/heart_disease.csv", index=False)
print("heart_disease.csv has been saved.")


# DataProcessor class
class DataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    # Load CSV file into DataFrame
    def load_csv(self):
        self.df = pd.read_csv(self.data_path)

    # Convert DataFrame to Parquet format
    def convert_to_parquet(self):
        df = pd.read_csv(self.data_path)
        df.to_parquet(self.data_path.replace(".csv", ".parquet"))

    # Define a function to compute basic statistics
    def compute_statistic(self):
        print("Maximum:",self.df.max(numeric_only=True))
        print("Minimum:",self.df.min(numeric_only=True))
        print("Average:",self.df.mean(numeric_only=True))
        print("Abs:",self.df.abs().mean(numeric_only=True))

# Main function to execute the data processing
def main():
    processor = DataProcessor("Week3/heart_disease.csv")
    processor.load_csv()
    processor.convert_to_parquet()
    processor.compute_statistic()

# Entry point
if __name__ == "__main__":
    main()