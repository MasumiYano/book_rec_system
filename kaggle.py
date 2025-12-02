import json
import os
import pandas as pd
import zipfile
import subprocess

class Kaggle():
    def __init__(self):
        self._set_kaggle_env()
        self.kaggle_df = None

    def _set_kaggle_env(self):
        with open("kaggle.json") as f:
            token = json.load(f)
        os.environ["KAGGLE_USERNAME"] = token["username"]
        os.environ["KAGGLE_KEY"] = token["key"]

    def get_data_from_kaggle(self):
        try:
            subprocess.run(
                ["kaggle", "datasets", "download", "-d", "abdallahwagih/books-dataset", "-p", "/tmp/bx", "--force"],
                check=True
            )
            with zipfile.ZipFile("/tmp/bx/books-dataset.zip", "r") as zip_ref:
                zip_ref.extractall("/tmp/bx")

            df = pd.read_csv("/tmp/bx/data.csv", sep=",", encoding='latin-1', on_bad_lines="skip", engine="python", quotechar='"')
            self.kaggle_df = df
            return df
        except Exception as e:
            print(f"Error occurred: {e}")
            return None


if __name__ == "__main__":
    kaggle = Kaggle()
    res = kaggle.get_data_from_kaggle()

    if res is not None:
        print("Successfull!\n")
    else:
        print("Failed.")
