
import os
import numpy as np
import pandas as pd
import flask
import xml.etree.ElementTree as ET
import joblib 
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from flask import Flask, render_template, request, Response, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/return',methods=["POST"])
def returns():
    coords = str(request.values.get("coords"))
    lat,lng = map(float,coords.split(","))
    result = ValuePredictor(list([lat,lng]))
    print(result)
    return jsonify(data=str(result))

@app.route('/updateModel',methods=["POST"])
def updateModel():
    n = int(request.values.get("numofclusters"))
    datas = parseXML('map.xml')
    # x = datas[:10]
    # y = datas[20:30]
    # z = datas[40:50]
    # l =x+y+z
    value = createModel(datas[:20],n)
    return jsonify(data=value)

@app.route('/populate')
def populate():
    locations = parseXML('map.xml')
    return jsonify(data=locations[:20])


@app.route('/clusterData',methods=["POST"])
def clusterData():
    content = request.get_json()
    value = runDBSCAN(content)
    return jsonify(data=value)

def ValuePredictor(coords):
    loaded_model = joblib.load(open("model.pkl","rb"))
    result = loaded_model.predict(list([coords]))
    return result[0]

def createModel(X,n):
    kmeans = KMeans(n_clusters=n).fit(X)
    joblib.dump(kmeans, 'model.pkl')
    categories={}
    labels = kmeans.labels_
    for i in range(len(labels)):
        if labels[i] in categories:
            categories[labels[i].item()].append(X[i])
        else:
            datas = list()
            datas.append(X[i])
            categories[labels[i].item()] = datas
    return categories

def parseXML(xmlfile): 
    tree = ET.parse(xmlfile) 
    root = tree.getroot() 
    locations = [] 
    for item in root.findall('./node'):
        k = list()
        k.append(float(item.attrib['lat']))
        k.append(float(item.attrib['lon']))
        locations.append(k)
    return locations


def runDBSCAN(X):
    coords = np.array(X) #np.array([[13.0544,77.6047],[13.0499,77.6122],[13.0228,77.7714],[13.0915,77.6414]])
    kms_per_radian = 6371.0088
    epsilon = 7 / kms_per_radian
    db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_
    print(cluster_labels)
    num_clusters = len(set(cluster_labels))
    clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
    print(clusters)
    return clusters.to_json(orient='index')

    