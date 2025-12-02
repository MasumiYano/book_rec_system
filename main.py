from copy import Error
from kaggle import Kaggle
from excel_manager import ExcelManager
from nl_to_json import NlToJson
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

kaggle = Kaggle()
kaggle_df = kaggle.get_data_from_kaggle()
print(f"Here's the result: {kaggle_df}")


file_path = "/mnt/data/nict/masumiy1/book_rec_system"
xcel_manager = ExcelManager(kaggle_df, file_path)
xcel_manager.to_excel()


nl_to_json = NlToJson(prompt_path="./prompt.txt", device=device)
nl_to_json.setup_pipeline()

try:
    res = nl_to_json.get_result()
    print(f"The result: {res}")

except Error as e:
    print(f"Error occured: {e}")
