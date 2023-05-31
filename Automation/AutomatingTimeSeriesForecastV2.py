#  Este codigo fue extraido desde la siguiente pagina
#  https://medium.com/@naseer1015922/5-killer-python-scripts-for-automation-part-2-33d7aa84cedc
#  Fue creado por https://medium.com/@naseer1015922

# Import visualization library
import matplotlib.pyplot as plt

# Plot predicted values
model.plot(forecast)
plt.show()

# Plot predicted values with uncertainty intervals
model.plot(forecast)
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='pink')
plt.show()

# Plot component of the forecast
model.plot_components(forecast)
plt.show()
