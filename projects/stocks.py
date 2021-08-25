import streamlit as st
from datetime import date
from datetime import timedelta
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

#Stock Market Application
print("Welcome to the Program")

start_date1 = "2020-01-01"
today_date = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction Web App")

stocks = ('AAPL', 'GOOG', "F", "MSFT","GME")
selected_stock = st.sidebar.selectbox("Select Stock Symbol", stocks)
st.sidebar.caption("OR")
type_stock = st.sidebar.text_input("Type Stock Symbol")

n_pastyears = st.slider("Years of History:", 1,40, value = 10, help = "Note: Recommended for \"Years of History\" is 10")
st.caption("Note: Recommended for \"Years of History\" is 10")
start_date = date.today() - timedelta(days = 1*365) - timedelta(days = n_pastyears*365)

n_years = st.slider("Years for Prediction:", 1,4)
period = n_years * (365) + 1


@st.cache
def load_data(ticker):
    data = yf.download(ticker, start_date, today_date)
    data.reset_index(inplace = True)
    return data

if type_stock != '':
    selected_stock = type_stock


data = load_data(selected_stock)
#st.warning("Please make sure you typed the Stock Symbol correctly")



def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y = data['Open'], name = 'stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y = data['Close'], name = 'stock_close'))
    fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    


#Checking the Stock Symbol
df_train = data[['Date','Close']]
if len(df_train) <= 0:
    st.warning("Please make sure you typed the Stock Symbol correctly")
    quit()
    
#Predicting   
current = yf.Ticker(selected_stock)
st.subheader("Company's Website:")
st.subheader(current.info['website'])
st.subheader("Raw Stock Data from Yahoo")
plot_raw_data()
st.write(data.tail())  
    
    
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
m = Prophet(interval_width = 0.90)
m.fit(df_train)
future = m.make_future_dataframe(periods = period)
forecast = m.predict(future)

st.subheader("Forecast Data")
#buildy = forecast
#buildy.rename

st.write(forecast.tail())

#st.write("forecast data")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Break Down of Forecast Components')
fig2 = m.plot_components(forecast)
st.write(fig2)













