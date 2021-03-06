import csv
import plotly.express as px
import numpy as np
def GetDataSource(datapath):
    icecream = []
    temperature = []

    with open (datapath) as csv_files:
        df=csv.DictReader(csv_files)
        for row in df:
            icecream.append(float(row['Ice-cream Sales']))
            temperature.append(float(row['Temperature']))
    return {'x':icecream, 'y':temperature}

       # fig=px.scatter(df,x='Temperature', y='Ice-cream Sales')
        # fig.show()
def FindCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'], datasource['y'])
    print('correlation between temperature and icecream sale-->',correlation[0,1])

def Setup():
    datapath='Ice.csv'
    datasource=GetDataSource(datapath)
    FindCorrelation(datasource)

Setup()