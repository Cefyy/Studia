import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

api_url = "https://api.nbp.pl/api/exchangerates/"

def process(df):
    if df.empty:
        return pd.Series(dtype="float64")
    df["effectiveDate"] = pd.to_datetime(df["effectiveDate"])
    df.set_index("effectiveDate",inplace=True)
    return df["mid"].resample("ME").mean()

def fetch_exchange_rates(year,currency_code):
    data = []
    start_date = datetime.strptime(f"{year}-01-01", "%Y-%m-%d")
    end_date = datetime.strptime(f"{year}-12-31", "%Y-%m-%d")
    curr_start = start_date
    while(curr_start<end_date):
        curr_end = min(curr_start + timedelta(days=93),end_date)
        s_str = curr_start.strftime("%Y-%m-%d")
        e_str = curr_end.strftime("%Y-%m-%d")
        try:
            response = requests.get(
                f"{api_url}rates/A/{currency_code}/{s_str}/{e_str}/",
                timeout=10,
            )
            response.raise_for_status()
            data.extend(response.json().get("rates", []))
        except Exception as e:
            print(f"Error while fetching exchange rates: {e}")
        curr_start = curr_end + timedelta(days=1)
    df = pd.DataFrame(data)
    return process(df)

def linear_regression(x, y):

    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
    
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    
    return slope, intercept

def predict_future(data, months_ahead=3):

    df = data.to_frame(name='rate')
    df = df.dropna()

    x = list(range(len(df)))
    y = df['rate'].tolist()

    slope, intercept = linear_regression(x, y)

    last_x = x[-1]
    predictions = []
    last_date = df.index[-1]
    
    for i in range(1, months_ahead + 1):
        future_x = last_x + i
        pred_y = slope * future_x + intercept
        future_date = last_date + pd.DateOffset(months=i)
        predictions.append({'date': future_date, 'predicted_rate': pred_y})
    
    result = pd.DataFrame(predictions)  
    return result

def plot_comprehensive(all_currencies_data, years, prediction_year=2024, months_to_predict=12):

    fig, axes = plt.subplots(3, 1, figsize=(14, 12))
    fig.suptitle('Analiza kursów walut USD i EUR względem PLN (2023-2025)', 
                 fontsize=16, fontweight='bold')
    
    colors = {'USD': '#1f77b4', 'EUR': '#ff7f0e'}
    markers = {'USD': 'o', 'EUR': 's'}
    

    ax1 = axes[0]
    for currency, data_dict in all_currencies_data.items():
        year_data = data_dict['years'][years[0]]
        months = range(1, len(year_data) + 1)
        ax1.plot(months, year_data.values, 
                color=colors[currency], linewidth=2, 
                label=f'{currency}/PLN', marker=markers[currency], markersize=6)
    
    ax1.set_title(f'Kursy walut w roku {years[0]}', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Miesiąc', fontsize=11)
    ax1.set_ylabel('Kurs (PLN)', fontsize=11)
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze', 
                         'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru'])
    ax1.legend(loc='best', fontsize=10)
    ax1.grid(True, alpha=0.3)
    

    ax2 = axes[1]
    for currency, data_dict in all_currencies_data.items():
        year_data = data_dict['years'][years[1]]
        months = range(1, len(year_data) + 1)
        ax2.plot(months, year_data.values, 
                color=colors[currency], linewidth=2, 
                label=f'{currency}/PLN', marker=markers[currency], markersize=6)
    
    ax2.set_title(f'Kursy walut w roku {years[1]}', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Miesiąc', fontsize=11)
    ax2.set_ylabel('Kurs (PLN)', fontsize=11)
    ax2.set_xticks(range(1, 13))
    ax2.set_xticklabels(['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze', 
                         'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru'])
    ax2.legend(loc='best', fontsize=10)
    ax2.grid(True, alpha=0.3)

    ax3 = axes[2]
    for currency, data_dict in all_currencies_data.items():
        predictions = data_dict['predictions']
        months = range(1, len(predictions) + 1)
        ax3.plot(months, predictions['predicted_rate'].values, 
                color=colors[currency], linewidth=2, linestyle='--',
                label=f'{currency}/PLN (prognoza)', marker=markers[currency], markersize=6)
    
    ax3.set_title(f'Prognoza kursów walut na rok {prediction_year + 1}', 
                 fontsize=12, fontweight='bold')
    ax3.set_xlabel('Miesiąc', fontsize=11)
    ax3.set_ylabel('Kurs (PLN)', fontsize=11)
    ax3.set_xticks(range(1, months_to_predict + 1))
    month_labels = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze', 
                    'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']
    ax3.set_xticklabels(month_labels[:months_to_predict])
    ax3.legend(loc='best', fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    
    currencies = ["USD", "EUR"]
    years = [2023, 2024]
    months_to_predict = 12 
    
    all_currencies_data = {}
    

    for currency in currencies:
        
        currency_data = {
            'years': {},
            'predictions': None
        }

        for year in years:
            data = fetch_exchange_rates(year, currency)
            currency_data['years'][year] = data

        data_2024 = currency_data['years'][2024]
        predictions = predict_future(data_2024, months_ahead=months_to_predict)
        currency_data['predictions'] = predictions
        
        all_currencies_data[currency] = currency_data
    

    plot_comprehensive(all_currencies_data, years, prediction_year=2024, 
                      months_to_predict=months_to_predict)


