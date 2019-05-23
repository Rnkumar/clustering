## K-means GeoCoordinate Clustering

###  This algorithm allows admins to cluster the incoming requests into number of available drivers and efficiently provide delivery orders to the drivers for faster delivery and fuel efficiency.

## Instructions to run this project

    1.Run the following commands inside project directory:
	python3 -m venv venv
	pip install flask
	pip install sklearn
    pip install joblib
    pip install -U flask-cors
    pip install pandas

	run source venv/bin/activate
    2. run python3 -m flask run(make sure venv folder is created before this step)
    3. Open localhost:5000
    4. The List of data will be provided.Click on update model button on the bottom of the screen.
    5. This displays clusters of data.
    6. In the input box, you can enter a latitude and longitude as comma separated which will show you the cluster to which it can be assigned to so that it can be added dynamically to the driver list. 
    7.While testing the adminpanel, make sure to keep this python server up since this serves the clustering api for the adminpanel.



    Note: This is just a demo of how to cluster and find the respective cluster for assigning.