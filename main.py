from typing import List
from fastapi import FastAPI
from DataModel import DataModel
from PredictionModel import Model
from DataModelWithLabel import DataModelWithLabel
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

@app.post("/predict")
def make_predictions(data: DataModel | List[DataModel] ):
    model = Model()
    if isinstance(data, list):
        return model.make_predictions(data)
    else:
        return model.make_prediction(data)

@app.post("/fit")
def make_fit(dataModels: List[DataModelWithLabel] ):
    X = []
    y = []
    for dataModel in dataModels:
        xrow = []
        yrow = []
        for attribute, value in dataModel.__dict__.items():
            if attribute != 'admission_points':
                xrow.append(value)
            else:
                y.append(value)
        X.append(xrow)
        # y.append(yrow)

    rf = RandomForestClassifier()
    rf.fit(X,y)
    print(rf.predict(X))
    return [X,y]
