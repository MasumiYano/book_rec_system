from openpyxl import load_workbook 
import pandas as pd
import os


class ExcelManager():
    def __init__(self, kagge_df: pd.DataFrame, excel_path: str):
        self.dataframe = kagge_df.head(100)
        self.excel_path = excel_path

    def to_excel (self):
        os.makedirs(self.excel_path, exist_ok=True)
        file_path = os.path.join(self.excel_path, "data.xlsx")
        try: 
            self.dataframe.to_excel(f"{file_path}", index=False, engine='openpyxl')
            self.format_excel(self.dataframe)

        except (FileNotFoundError, Exception) as e:
            print(f"An error ocurred: {e}")

    def format_excel(self, excel_file: pd.ExcelFile):
        wb = load_workbook(f"{excel_file}")
        ws = wb.active

        for col in ws.columns:
            max_length = 0
            col_letter = col[0].column_letter
            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))

        ws.column_dimensions[col_letter].width = max_length + 2

        wb.save(f"{excel_file}")
