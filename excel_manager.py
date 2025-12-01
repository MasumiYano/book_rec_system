from openpyxl import Workbook
import pandas as pd
import os


class ExcelManager():
    def __init__(self, kagge_df: pd.DataFrame, excel_path: str):
        self.dataframe = kagge_df.head(100)
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.excel_path = excel_path

    def to_excel (self):
        os.makedirs(self.excel_path, exist_ok=True)
        file_path = os.path.join(self.excel_path, "data.xlsx")
        try: 
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                self.dataframe.to_excel(writer, sheet_name='Sheet1', index=False)
                
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']

                worksheet.column_dimensions['A'].width = 15
                worksheet.column_dimensions['B'].width = 20

                print("Sucess")

        except (FileNotFoundError, Exception) as e:
            print(f"An error ocurred: {e}")
