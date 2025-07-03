import pandas as pd

def check_data():
    try:
        # Read the Excel file
        df = pd.read_excel('data.xlsx')
        print("\nCurrent data in Excel file:")
        print(df)
        
        # Check if file is empty
        if df.empty:
            print("\nNote: The Excel file is empty. No entries have been saved yet.")
        else:
            print("\nData columns:", df.columns.tolist())
            print("\nNumber of entries:", len(df))
            
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")

if __name__ == '__main__':
    check_data()
