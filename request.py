  
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':32, 'weight':45, 'gender':1,'Vo2MAx':57.34})

print(r.json())