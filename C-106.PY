import csv
import plotly.express as px
import numpy as np
def GetDataSource(datapath):
    coffee = []
    sleep = []

    with open (datapath) as csv_files:
        df=csv.DictReader(csv_files)
        for row in df:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {'x':coffee, 'y':sleep}

       # fig=px.scatter(df,x='Temperature', y='Ice-cream Sales')
        # fig.show()
def FindCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'], datasource['y'])
    print('correlation between coffee and sleep-->',correlation[0,1])

def Setup():
    datapath='coffee.csv'
    datasource=GetDataSource(datapath)
    FindCorrelation(datasource)

Setup()