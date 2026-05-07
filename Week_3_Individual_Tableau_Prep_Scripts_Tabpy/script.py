import pandas as pd


def get_output_schema():
    return pd.DataFrame({
        'Employee_ID':                    prep_string(),
        'Employee_Name':                  prep_string(),
        'Department':                     prep_string(),
        'Age':                            prep_int(),
        'Salary':                         prep_int(),
        'Hire_Date':                      prep_string(),
        'City':                           prep_string(),
        'Average_Salary_All_Employees':   prep_decimal(),
        'Oldest_Employee_Name':           prep_string(),
        'Oldest_Employee_Department':     prep_string()
    })


def filter_and_enrich(df):
    # Step 1: Compute metrics across ALL employees BEFORE filtering
    avg_salary = df['Salary'].mean()
    oldest_row = df.loc[df['Age'].idxmax()]
    oldest_name = oldest_row['Employee_Name']
    oldest_dept = oldest_row['Department']

    # Step 2: Add new columns
    df['Average_Salary_All_Employees'] = avg_salary
    df['Oldest_Employee_Name'] = oldest_name
    df['Oldest_Employee_Department'] = oldest_dept

    # Step 3: Filter to IT department only
    it_df = df[df['Department'] == 'IT'].copy()

    # Step 4: Force column order explicitly
    it_df = it_df[['Employee_ID', 'Employee_Name', 'Department', 'Age', 'Salary',
                   'Hire_Date', 'City',
                   'Average_Salary_All_Employees',
                   'Oldest_Employee_Name',
                   'Oldest_Employee_Department']]

    return it_df


# Run it (for testing outside Tableau Prep)
if __name__ == '__main__':
    df = pd.read_csv('employee_tableau_prep_python_sample.csv')
    result = filter_and_enrich(df)

    print("=== IT Department Employees ===")
    print(result[['Employee_Name', 'Department', 'Age', 'Salary',
                  'Average_Salary_All_Employees',
                  'Oldest_Employee_Name',
                  'Oldest_Employee_Department']].to_string(index=False))