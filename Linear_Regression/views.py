from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
# from sklearn.preprocessing._data import MinMaxScaler
# import sklearn.linear_model._base


# Create your views here.
def home(request):
    return render(request,'Linear_Regression/home.html')


def output(request):
    vehicle_name = request.POST.get('vehicle_name')
    battery = request.POST.get('battery')
    acceleration = request.POST.get('acceleration')
    top_speed = request.POST.get('top_speed')
    distance = request.POST.get('distance')
    efficiency = request.POST.get('efficiency')
    fast_charge = request.POST.get('fast_charge')
    data = {'vehicle_name':vehicle_name,'acceleration':acceleration,'battery':battery,
            'top_speed':top_speed,'distance':distance,'efficiency':efficiency,'fast_charge':fast_charge}
    electric_df = pd.DataFrame(data=data,index=[0])
    with open("C:/Users/HP/PycharmProjects/hamoye/electric vehicle/hotencoder",'rb') as file1:
        hot_encoder = pickle.load(file1)
        file1.close()
    df_try = pd.DataFrame(hot_encoder.transform(electric_df[['vehicle_name']]).toarray())
    electric_df = electric_df.join(df_try)
    electric_df.drop(columns=['vehicle_name'],inplace=True)
    with open("C:/Users/HP/PycharmProjects/hamoye/electric vehicle/scaler",'rb') as file2:
        scaler = pickle.load(file2)
        file1.close()
    ml_df = scaler.transform(electric_df)
    with open("C:/Users/HP/PycharmProjects/hamoye/electric vehicle/linear_model",'rb')as file3:
        linear_model = pickle.load(file3)
        file2.close()
    price_usd = round(np.float(abs(linear_model.predict(ml_df))))

    return render(request,'Linear_Regression/output.html',{'price_usd':price_usd,'vehicle_name':vehicle_name})
