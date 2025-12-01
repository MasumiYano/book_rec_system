from kaggle import Kaggle
from excel_manager import ExcelManager


kaggle = Kaggle()
kaggle_df = kaggle.get_data_from_kaggle()
print(f"Here's the result: {kaggle_df}")


file_path = "/mnt/data/nict/masumiy1/book_rec_system"
xcel_manager = ExcelManager(kaggle_df, file_path)
xcel_manager.to_excel()
