# Sentiment Classifier Deployed as a REST API using Flask

* [Flask Restful Documentation]()
* [HTTPie Documentation](https://httpie.org/doc)
* [Data Source: Kaggle](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data)
___

## Procedure
1. Start a virtual environment and install requirements
3. Build sentiment classifier
4. Write `app.py` which is the API application that will be deployed
5. Update requirements.txt as you write the code
6. Test the API


## File Structure
* app_name
  * app.py: Flask API application
  * model.py: class object for classifier
  * build_model.py: imports the class object from `model.py` and initiates a new model, trains the model, and pickle
  * util.py: helper functions for `model.py`
  * requirements.txt: list of packages that the app will import
  * lib
      * data: directory that contains the data files from Kaggle
      * models: directory that contains the pickled model files

Based on this [repository](https://github.com/mnguyenngo/flask-rest-setup/tree/master/sentiment-clf)
