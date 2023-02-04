## Simple script to demonstate running our pretrained model, stored as pmml, in python

from pypmml import Model

#Import our previously trained model
model = Model.fromFile('11_chocolate_recommendations.pmml')

## call the model - note the format on how we pass in the parameters needed
result = model.predict({'Customer_Age': 50, 'Country_Code': 100})

## print the result
print(result)
