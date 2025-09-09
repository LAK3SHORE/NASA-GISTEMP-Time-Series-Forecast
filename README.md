# Climate Temperature Anomaly Forecasting: ARIMA Time Series Analysis

## Project Overview

This project presents a comprehensive time series analysis of global temperature anomalies using NASA's GISTEMP dataset (1880-2024) to forecast climate trends through 2030. The analysis employs ARIMA methodology to model temperature patterns and supports climate action objectives aligned with SDG 13.

## Key Findings

- **Historical Analysis**: Global temperatures have increased by 1.18°C since 1880, with accelerated warming in recent decades
- **Future Projections**: Model forecasts sustained temperature anomalies of ~1.13°C through 2030
- **Critical Threshold**: Current temperatures are dangerously close to the 1.5°C Paris Agreement threshold
- **Extreme Years**: The five warmest years on record are all from 2016-2024

## Technical Implementation

### Dataset
- **Source**: NASA GISTEMP v4 (Land-Ocean Temperature Index)
- **Period**: 1880-2024 (145 years, 1,752 monthly observations)
- **Reference baseline**: 1951-1980 average

### Methodology
- **Model**: ARIMA(0,1,2) selected via AIC criterion (AIC = -198.79)
- **Stationarity**: Augmented Dickey-Fuller test confirmed first-order differencing requirement
- **Validation**: 85/15 train-test split with comprehensive residual diagnostics

### Model Performance
- **MAE**: 0.2792°C
- **RMSE**: 0.3435°C  
- **MAPE**: 31.02%
- **Diagnostics**: Passed Ljung-Box test, normality test, and homoscedasticity assessment

## Key Features

- Time series decomposition and trend analysis
- Stationarity testing and transformation
- ARIMA model selection and validation
- 6-year forecasting with confidence intervals
- Comprehensive residual diagnostics
- Climate policy implications analysis

## Forecast Results

| Year | Forecast (°C) | 95% Confidence Interval |
|------|---------------|-------------------------|
| 2025 | 1.173 | 0.965 - 1.381 |
| 2026 | 1.129 | 0.875 - 1.383 |
| 2027 | 1.129 | 0.856 - 1.402 |
| 2028 | 1.129 | 0.838 - 1.420 |
| 2029 | 1.129 | 0.821 - 1.437 |
| 2030 | 1.129 | 0.805 - 1.453 |

## Applications

- Climate policy decision-making
- Long-term environmental planning
- Risk assessment for climate thresholds
- Supporting evidence for transformational climate action
