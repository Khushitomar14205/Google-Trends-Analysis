# Google Trends Analysis

Developed an interactive Streamlit dashboard that analyzes Google search trends using PyTrends, enabling keyword comparison, regional insights, related query analysis, and trend visualization.

##  Live Demo

https://app-trends-analysis-3stvogwt76hmhrevkvvq55.streamlit.app/

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- PyTrends
  
## Features

- **Keyword Comparison:** Enter one or more keywords to compare their popularity on Google Search over the past 5 years.
- **Regional Insights:** View which regions search most for each keyword.
- **Related Query Analysis:** Discover top related queries for each entered keyword.
- **Interactive Visualizations:** Explore trends with interactive line and bar charts (powered by Plotly).
- **Data Export:** Download search trend data as a CSV file.
- **Jupyter Notebook:** A notebook for more in-depth, customizable analysis is also included.

## Demo

Screenshots of the dashboard can be found in the [`Screenshots/`](https://github.com/Khushitomar14205/Google-Trends-Analysis/tree/main/Screenshots) directory.

## Getting Started

### Prerequisites

- Python 3.7 or above
- pip

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Khushitomar14205/Google-Trends-Analysis.git
    cd Google-Trends-Analysis
    ```

2. **Install dependencies:**

    *If you have a `requirements.txt`, run:*
    ```bash
    pip install -r requirements.txt
    ```

    *Or install main libraries manually:*
    ```bash
    pip install streamlit pytrends pandas plotly
    ```

### Running the Dashboard

```bash
streamlit run app.py
```

Then open the provided local URL in your web browser.

### Using the Jupyter Notebook

You can also run `Trend_analysis_Project.ipynb` in Jupyter for experimentation and additional analyses:
```bash
jupyter notebook Trend_analysis_Project.ipynb
```

## File Structure

- `app.py` — Streamlit dashboard main application.
- `Trend_analysis_Project.ipynb` — Jupyter notebook for step-by-step trend analysis.
- `Screenshots/` — Example screenshots of the dashboard.
- `requirements.txt` — List of required Python packages (add if empty).

## How It Works

The dashboard uses the [PyTrends](https://github.com/GeneralMills/pytrends) library to fetch trend data from Google Trends based on the keywords you enter. You can visualize:
- Search interest over time.
- Top regions for each keyword.
- Related queries for further exploration.

## License

This project is provided for educational and demonstration purposes.

---
Feel free to open issues or contribute!
