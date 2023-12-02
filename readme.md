# Convert Step 09 Financial Analyst Project to Streamlit App

###### This is a Multi Modal ChatGPT Application with Streamlit DALLE-3 Function Calling From Scratch

"Financial-Analyst" is a simple financial analyst project leveraging REST APIs and OpenAI's Assistants API architecture to aid end users with financial analysis. 

Try it Out For:
1. Getting Financials Comparision
2. Plot Charts to see the Financials Comparision

Inspired by the idea of building an AI financial analyst, this project integrates advanced AI capabilities to provide insightful financial information.


### Try Prompts

#### 1 - Financials Comparision

Can you compare the financial health of Microsoft and Apple over the last four years, focusing on their balance sheets and key financial ratios?

#### 21 - Financials Comparision And Visual Charts

Evaluate Microsoft vs. Googles's revenue & profitability growth over the past 4 quarters. Visualize the results with one or more charts.


### - Features
1. AI-Driven Financial Analysis: Utilizes OpenAI's Assistants API to analyze financial data.
2. Streamlit Web Application: An interactive web interface for easy access and use.
3. Dynamic Data Retrieval: Fetches financial information from various REST APIs.

### - Assistant Functions

- get_income_statement: Retrieves the income statement data. This function likely fetches detailed revenue, expense, and profit information for a specified entity over a given period.

- get_balance_sheet: Obtains the balance sheet data. This would include assets, liabilities, and shareholder equity details, providing a snapshot of an entity's financial condition at a specific point in time.

- get_cash_flow_statement: Gathers cash flow statement data. It probably details the cash inflows and outflows from operating, investing, and financing activities, offering insights into how an entity generates and uses cash.

- get_key_metrics: Retrieves key financial metrics. This function likely provides important financial indicators that help in assessing a company's financial health, such as EBITDA, return on equity, debt to equity ratio, etc.

- get_financial_ratios: Fetches various financial ratios. These ratios, such as the price-to-earnings ratio, current ratio, or liquidity ratio, are crucial for financial analysis and comparative assessments.

- get_financial_growth: Accesses financial growth data. This function probably tracks the growth trends in various financial aspects like revenue growth, profit growth, etc., over time, indicating the entity's growth trajectory.

### Installation
To install the necessary dependencies, run:

```
pip install -r requirements.txt
```
### Configuration
Configure the .env file with your OpenAI API key and any other necessary settings.

### Usage

Streamlit App: Run the Streamlit app to interact with the financial analyst features.

```
streamlit run streamlit_app.py
```

- Assistant API: The assistant.py script manages OpenAI Assistant calls and functions.

- Utility Functions: The utils.py script contains utility functions for displaying messages and images.

### Contributing
Contributions are welcome. Please follow standard coding conventions and submit pull requests for any proposed changes.

