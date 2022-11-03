import pandas as pd
from joblib import load

class Model:

    def __init__(self):
        self.model = load("assets/pipeline.joblib")

    def make_prediction(self, dataModel):
        df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
        df.columns = dataModel.columns()
        result = self.model.predict(df)[0]
        return result

    def make_predictions(self, dataModels):
        results = []
        for dataModel in dataModels:
            result = self.make_prediction(dataModel)
            results.append(result)
        return results
