# Load Python modules for object serialization
import pickle

# Initialize FastAPI object and import relevant modules
from typing import Union, Optional
from fastapi import FastAPI, Path, Query

# Load Body Parameters
from parameters.body_params import HouseFeatures

# Load the model
filename = "saved_models/rf_dep.pkl"
rf_model = pickle.load(open(filename, "rb"))

# Initialize the app
app = FastAPI()

# Initialize results for sending a response via GET request
results = {}


# Define the API route to ACCESS the parameters and perform predictions. 'POST' request
@app.post("/get-House-Fs")
def get_House_fs(*, request: HouseFeatures):
    overallQuality = request.overallQuality
    if overallQuality == "Very Poor":
        overallQuality = 1
    elif overallQuality == "Poor":
        overallQuality = 2
    elif overallQuality == "Fair":
        overallQuality = 3
    elif overallQuality == "Below Average":
        overallQuality = 4
    elif overallQuality == "Average" or overallQuality is None:
        overallQuality = 5
    elif overallQuality == "Above Average":
        overallQuality = 6
    elif overallQuality == "Good":
        overallQuality = 7
    elif overallQuality == "Very Good":
        overallQuality = 8
    elif overallQuality == "Excellent":
        overallQuality = 9
    elif overallQuality == "Very Excellent":
        overallQuality = 10

    results.update({"Overall Quality": overallQuality})

    livingRoomArea = request.livingRoomArea
    if livingRoomArea is None:
        livingRoomArea = 334
    else:
        livingRoomArea = int(round(livingRoomArea, 2))

    results.update({"Available Living Room Area": livingRoomArea})

    basementArea = request.basementArea
    if basementArea is None:
        basementArea = 0
    else:
        basementArea = int(round(basementArea, 2))

    results.update({"Available Basement Area": basementArea})

    firstFloorArea = request.firstFloorArea
    if firstFloorArea is None:
        firstFloorArea = 334
    else:
        firstFloorArea = int(round(firstFloorArea, 2))

    results.update({"Available First Floor Total Area": firstFloorArea})

    type1FinishedArea = request.type1FinishedArea
    if type1FinishedArea is None:
        type1FinishedArea = 0
    else:
        type1FinishedArea = int(round(type1FinishedArea), 2)

    results.update({"Constructed first floor area": type1FinishedArea})

    secondFloorArea = request.secondFloorArea
    if secondFloorArea is None:
        secondFloorArea = 0
    else:
        secondFloorArea = int(round(secondFloorArea), 2)

    results.update({"Total second floor area": secondFloorArea})

    lotArea = request.lotArea
    if lotArea is None:
        lotArea = 1300
    else:
        lotArea = int(round(lotArea), 2)

    results.update({"Lot Area": lotArea})

    yearBuilt = request.yearBuit
    if yearBuilt is None:
        yearBuilt = 1872
    else:
        yearBuilt = int(round(yearBuilt), 2)

    results.update({"Year of house built": yearBuilt})

    bathAboveGrade = request.bathAboveGrade
    if bathAboveGrade is None:
        bathAboveGrade = 0
    else:
        bathAboveGrade = int(round(bathAboveGrade), 2)

    results.update({"No. of bathrooms above grade": bathAboveGrade})

    yearGarageBuilt = request.yearGarageBuilt
    if yearGarageBuilt is None:
        yearGarageBuilt = 1895
    else:
        yearGarageBuilt = yearGarageBuilt

    results.update({"Year of garage built": yearGarageBuilt})

    porchArea = request.porchArea
    if porchArea is None:
        porchArea = 0
    else:
        porchArea = int(round(porchArea), 2)

    results.update({"Total Porch Area": porchArea})

    garageArea = request.garageArea
    if garageArea is None:
        garageArea = 0
    else:
        garageArea = int(round(porchArea), 2)

    results.update({"Total Garage Area": garageArea})

    garageCarCapacity = request.garageCarCapacity
    if garageCarCapacity is None:
        garageCarCapacity = 0
    else:
        garageCarCap = int(garageCarCapacity)

    results.update({"Total Garage Car Capacity": garageCarCapacity})

    overallCondition = request.overallCondition
    if overallCondition is None:
        overallCondition = 1
    elif overallCondition == "Very Poor":
        overallCondition = 1
    elif overallCondition == "Poor":
        overallCondition = 2
    elif overallCondition == "Fair":
        overallCondition = 3
    elif overallCondition== "Below Average":
        overallCondition = 4
    elif overallCondition == "Average" or overallCondition == "Cannot Say":
        overallCondition = 5
    elif overallCondition == "Above Average":
        overallCondition = 6
    elif overallCondition == "Good":
        overallCondition = 7
    elif overallCondition == "Very Good":
        overallCondition = 8
    elif overallCondition == "Excellent":
        overallCondition = 9
    elif overallCondition == "Very Excellent":
        overallCondition = 10

    results.update({"Overall Condition Rating ": overallCondition})

    # Perform predictions
    preds = rf_model.predict([[overallQuality, livingRoomArea, basementArea, firstFloorArea, type1FinishedArea,
                               secondFloorArea, lotArea, yearBuilt, bathAboveGrade, yearGarageBuilt, porchArea, garageArea,
                               garageCarCapacity, overallCondition]])
    preds_final = round(preds[0], 2)

    return {"Predicted House Price": preds_final}
