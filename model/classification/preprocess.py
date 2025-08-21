import os
import pandas as pd

directory = "./data"

thing = {
    "Non_Demented": 0,
    "Very_mild_Dementia": 1,
    "Mild_Dementia": 2,
    "Moderate_Dementia": 3
}

data = []

for subdir in os.listdir(directory):
    subdir_path = os.path.join(directory, subdir)
    if os.path.isdir(subdir_path) and subdir in thing:
        for image in os.listdir(subdir_path):
            image_path = os.path.join(subdir_path, image)

            data.append({
                "image_path": image_path,
                "subdir": subdir,
                "label": thing[subdir]
            })

df = pd.DataFrame(data, columns=["image_path", "subdir", "label"])

df.to_csv("dataset.csv", index=False)