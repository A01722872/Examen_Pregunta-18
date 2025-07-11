# -*- coding: utf-8 -*-
"""Examen_A01722872

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JWyBS706YBfbFUZAgNPvu7bft-P-P2bk
"""

from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

# Upload the Excel file in Colab
uploaded = files.upload()

# Read the Excel file (assumes EXAMEN TABLA.xlsx is uploaded)
df = pd.read_excel("EXAMEN TABLA.xlsx")

# Extract PDI column and apply natural logarithm
pdi = df['PDI']
log_pdi = np.log(pdi)

# Plot log(PDI) series
plt.figure(figsize=(10, 6))
plt.plot(log_pdi, label='log(PDI)')
plt.title('Log of Personal Disposable Income (1970.1 - 1991.4)')
plt.xlabel('Time')
plt.ylabel('log(PDI)')
plt.legend()
plt.show()

# Function to perform ADF test and print results
def adf_test(series, title=''):
    result = adfuller(series, autolag='AIC')
    print(f'ADF Test for {title}:')
    print(f'ADF Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    print(f'Critical Values: {result[4]}')
    print('Stationary' if result[1] < 0.05 else 'Non-stationary')
    print()

# Perform ADF test on log(PDI)
adf_test(log_pdi, 'log(PDI)')

# If non-stationary, difference the series and test again
if adfuller(log_pdi)[1] >= 0.05:
    diff_log_pdi = log_pdi.diff().dropna()
    plt.figure(figsize=(10, 6))
    plt.plot(diff_log_pdi, label='Differenced log(PDI)')
    plt.title('Differenced Log of Personal Disposable Income')
    plt.xlabel('Time')
    plt.ylabel('Differenced log(PDI)')
    plt.legend()
    plt.show()

    adf_test(diff_log_pdi, 'Differenced log(PDI)')
else:
    diff_log_pdi = log_pdi  # Use original if stationary

# Plot ACF and PACF
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
acf_vals = acf(diff_log_pdi, nlags=20)
pacf_vals = pacf(diff_log_pdi, nlags=20)

ax1.stem(range(len(acf_vals)), acf_vals)
ax1.set_title('ACF of Differenced log(PDI)')
ax1.set_xlabel('Lag')
ax1.set_ylabel('Autocorrelation')

ax2.stem(range(len(pacf_vals)), pacf_vals)
ax2.set_title('PACF of Differenced log(PDI)')
ax2.set_xlabel('Lag')
ax2.set_ylabel('Partial Autocorrelation')

plt.tight_layout()
plt.show()

# Fit ARIMA model (p,d,q to be determined from ACF/PACF, using d=1 if differenced)
# Example: ARIMA(1,1,1) based on typical ACF/PACF patterns
order = (1, 1 if adfuller(log_pdi)[1] >= 0.05 else 0, 1)
model = ARIMA(log_pdi, order=order)
results = model.fit()

# Print model summary
print(results.summary())

# Plot fitted values vs actual
fitted = results.fittedvalues
plt.figure(figsize=(10, 6))
plt.plot(log_pdi, label='Actual log(PDI)')
plt.plot(fitted, label='Fitted log(PDI)', linestyle='--')
plt.title('Actual vs Fitted log(PDI)')
plt.xlabel('Time')
plt.ylabel('log(PDI)')
plt.legend()
plt.show()

from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima.model import ARIMA
import warnings
import io
import base64
from IPython.display import HTML

warnings.filterwarnings("ignore")

# Python code as a string for HTML output
code_string = """
from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima.model import ARIMA
import warnings
import io
import base64
from IPython.display import HTML

warnings.filterwarnings("ignore")

# Upload the Excel file in Colab
uploaded = files.upload()

# Read the Excel file
df = pd.read_excel("EXAMEN TABLA.xlsx")

# Extract PDI column and apply natural logarithm
pdi = df['PDI']
log_pdi = np.log(pdi)

# Plot log(PDI) series
plt.figure(figsize=(10, 6))
plt.plot(log_pdi, label='log(PDI)')
plt.title('Log of Personal Disposable Income (1970.1 - 1991.4)')
plt.xlabel('Time')
plt.ylabel('log(PDI)')
plt.legend()

# Function to perform ADF test and capture results
def adf_test(series, title=''):
    result = adfuller(series, autolag='AIC')
    output = f'ADF Test for {title}:<br>'
    output += f'ADF Statistic: {result[0]:.4f}<br>'
    output += f'p-value: {result[1]:.4f}<br>'
    output += f'Critical Values: {result[4]}<br>'
    output += f'{"Stationary" if result[1] < 0.05 else "Non-stationary"}<br><br>'
    return output, result[1]

# Perform ADF test on log(PDI)
adf_result, p_value = adf_test(log_pdi, 'log(PDI)')

# If non-stationary, difference the series and test again
if p_value >= 0.05:
    diff_log_pdi = log_pdi.diff().dropna()
    plt.figure(figsize=(10, 6))
    plt.plot(diff_log_pdi, label='Differenced log(PDI)')
    plt.title('Differenced Log of Personal Disposable Income')
    plt.xlabel('Time')
    plt.ylabel('Differenced log(PDI)')
    plt.legend()
    adf_diff_result, _ = adf_test(diff_log_pdi, 'Differenced log(PDI)')
else:
    diff_log_pdi = log_pdi

# Plot ACF and PACF
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
acf_vals = acf(diff_log_pdi, nlags=20)
pacf_vals = pacf(diff_log_pdi, nlags=20)

ax1.stem(range(len(acf_vals)), acf_vals)
ax1.set_title('ACF of Differenced log(PDI)')
ax1.set_xlabel('Lag')
ax1.set_ylabel('Autocorrelation')

ax2.stem(range(len(pacf_vals)), pacf_vals)
ax2.set_title('PACF of Differenced log(PDI)')
ax2.set_xlabel('Lag')
ax2.set_ylabel('Partial Autocorrelation')

plt.tight_layout()

# Fit ARIMA model
order = (1, 1 if p_value >= 0.05 else 0, 1)
model = ARIMA(log_pdi, order=order)
results = model.fit()

# Plot fitted values vs actual
plt.figure(figsize=(10, 6))
plt.plot(log_pdi, label='Actual log(PDI)')
plt.plot(results.fittedvalues, label='Fitted log(PDI)', linestyle='--')
plt.title('Actual vs Fitted log(PDI)')
plt.xlabel('Time')
plt.ylabel('log(PDI)')
plt.legend()
"""

# Initialize HTML content
html_content = f"""
<html>
<head><title>ARIMA Analysis of PDI</title></head>
<body>
<h1>ARIMA Analysis of Personal Disposable Income</h1>
<h2>Python Code</h2>
<pre>{code_string.replace('<', '&lt;').replace('>', '&gt;')}</pre>
<h2>Analysis Output</h2>
"""

# Function to convert plot to base64 for HTML embedding
def plot_to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return img_str

# Upload the Excel file in Colab
uploaded = files.upload()

# Read the Excel file
df = pd.read_excel("EXAMEN TABLA.xlsx")

# Extract PDI column and apply natural logarithm
pdi = df['PDI']
log_pdi = np.log(pdi)

# Plot log(PDI) series
plt.figure(figsize=(10, 6))
plt.plot(log_pdi, label='log(PDI)')
plt.title('Log of Personal Disposable Income (1970.1 - 1991.4)')
plt.xlabel('Time')
plt.ylabel('log(PDI)')
plt.legend()
html_content += f'<h3>Log(PDI) Plot</h3><img src="data:image/png;base64,{plot_to_base64()}"/>'
plt.close()

# Function to perform ADF test and capture results
def adf_test(series, title=''):
    result = adfuller(series, autolag='AIC')
    output = f'ADF Test for {title}:<br>'
    output += f'ADF Statistic: {result[0]:.4f}<br>'
    output += f'p-value: {result[1]:.4f}<br>'
    output += f'Critical Values: {result[4]}<br>'
    output += f'{"Stationary" if result[1] < 0.05 else "Non-stationary"}<br><br>'
    return output, result[1]

# Perform ADF test on log(PDI)
adf_result, p_value = adf_test(log_pdi, 'log(PDI)')
html_content += f'<h3>ADF Test for log(PDI)</h3><pre>{adf_result}</pre>'

# If non-stationary, difference the series and test again
if p_value >= 0.05:
    diff_log_pdi = log_pdi.diff().dropna()
    plt.figure(figsize=(10, 6))
    plt.plot(diff_log_pdi, label='Differenced log(PDI)')
    plt.title('Differenced Log of Personal Disposable Income')
    plt.xlabel('Time')
    plt.ylabel('Differenced log(PDI)')
    plt.legend()
    html_content += f'<h3>Differenced log(PDI) Plot</h3><img src="data:image/png;base64,{plot_to_base64()}"/>'
    plt.close()

    adf_diff_result, _ = adf_test(diff_log_pdi, 'Differenced log(PDI)')
    html_content += f'<h3>ADF Test for Differenced log(PDI)</h3><pre>{adf_diff_result}</pre>'
else:
    diff_log_pdi = log_pdi

# Plot ACF and PACF
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
acf_vals = acf(diff_log_pdi, nlags=20)
pacf_vals = pacf(diff_log_pdi, nlags=20)

ax1.stem(range(len(acf_vals)), acf_vals)
ax1.set_title('ACF of Differenced log(PDI)')
ax1.set_xlabel('Lag')
ax1.set_ylabel('Autocorrelation')

ax2.stem(range(len(pacf_vals)), pacf_vals)
ax2.set_title('PACF of Differenced log(PDI)')
ax2.set_xlabel('Lag')
ax2.set_ylabel('Partial Autocorrelation')

plt.tight_layout()
html_content += f'<h3>ACF and PACF Plots</h3><img src="data:image/png;base64,{plot_to_base64()}"/>'
plt.close()

# Fit ARIMA model
order = (1, 1 if p_value >= 0.05 else 0, 1)
model = ARIMA(log_pdi, order=order)
results = model.fit()

# Capture model summary
summary = results.summary().as_html()
html_content += f'<h3>ARIMA{order} Model Summary</h3>{summary}'

# Plot fitted values vs actual
plt.figure(figsize=(10, 6))
plt.plot(log_pdi, label='Actual log(PDI)')
plt.plot(results.fittedvalues, label='Fitted log(PDI)', linestyle='--')
plt.title('Actual vs Fitted log(PDI)')
plt.xlabel('Time')
plt.ylabel('log(PDI)')
plt.legend()
html_content += f'<h3>Actual vs Fitted log(PDI) Plot</h3><img src="data:image/png;base64,{plot_to_base64()}"/>'
plt.close()

# Finalize HTML
html_content += "</body></html>"

# Save HTML to file
html_filename = "arima_pdi_analysis.html"
with open(html_filename, 'w') as f:
    f.write(html_content)

# Download the HTML file
files.download(html_filename)