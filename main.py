import pandas as pd


def calc_bmr(height, weight, gender, age):
    if gender == 'M': 
        return (10 * (weight * 0.453592)) + (6.25 * height) - (5 * age) + 5
    elif gender == "F":
        return (10 * weight * 0.453592) + (6.25 * height) - (5 * age ) - 161   

def read_excel_file(file_path):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def weekly_count(file_path):
    #find a way to store user weight data to have a running weekly count.
    # Replace this with the path to your Excel file
    excel_data_df = read_excel_file(file_path)
    window_size = 7
    rolling_mean_list = excel_data_df.stack().dropna().tail(window_size).tolist()
    rolling_mean = sum(rolling_mean_list)/len(rolling_mean_list)
    return rolling_mean
   
    
def main():
    height = 172.72
    weight = 250
    gender = "M"
    age = 28
    bmr = calc_bmr(height, weight, gender, age) * 1.20
    file_path = "user.csv"

    print(weekly_count(file_path))

    #find a way to store user weight data to have a running weekly count.
    print(bmr)





main()