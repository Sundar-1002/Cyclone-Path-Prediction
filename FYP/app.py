from flask import Flask,render_template,request,redirect,json
import prediction_atlantic,prediction_pacific,prediction_indian
import requests,csv,subprocess
import pandas as pd

data = pd.read_csv("myvalues.csv")

latit = data['Latitude']
longi = data['Longitude']

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/templates/upload.html",methods=['GET','POST'])
def getValues():
    if request.method=='GET':
        return render_template('upload.html')
    elif request.method=='POST':
        return render_template('success.html')

@app.route('/run-script/<string:title>',methods=['GET','POST'])
def runscript(title):
    title = json.loads(title)
    tit = title;
    print(tit)
    response = requests.get("https://eonet.gsfc.nasa.gov/api/v3/categories/severeStorms")

    c = csv.writer(open("myvalues.csv","w"), lineterminator="\n")

    i = 0
    r = response.json()
    print(response.status_code)
    headerList = ['CycloneName','DateTime','Type','Latitude','Longitude','Maximum Wind']
    c.writerow(headerList)
    s = len(r['events'])
    for k in range(0,s):
        title = r['events'][k]['title']
        print(r['events'][k]['title'])


    for j in range(0,s):
        for item in r['events'][j]['geometry']:
            if tit == r['events'][j]['title']:
                c.writerow([r['events'][j]['title'],r['events'][j]['geometry'][i]['date'],r['events'][j]['geometry'][i]['type'],r['events'][j]['geometry'][i]['coordinates'][1],r['events'][j]['geometry'][i]['coordinates'][0],r['events'][j]['geometry'][i]['magnitudeValue']])
                i=i+1

        return render_template('upload.html')

@app.route('/templates/predict.html',methods=['GET','POST'])
def predict():
    if latit[0] in range(-60,69) and longi[0] in range(-98,20):
        coords,title = prediction_atlantic.predcyc()
        return render_template('predict.html',coords=coords,title=title)
    elif latit[0] in range(-60,66) and longi[0] in range(117,-67):
        coords,title = prediction_pacific.predcyc()
        return render_template('predict.html',coords=coords,title=title)
    else:
        coords,title = prediction_indian.predcyc()
        return render_template('predict.html',coords=coords,title=title)



if __name__ == '__main__':
    app.run(debug=True,port=5000)