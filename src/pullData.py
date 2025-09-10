import yfinance as yf
import json




def pstockData_JSON(stock: str) -> dict:
    print("Pulling data from " + stock)
    m_stock = yf.Ticker(stock)
    info = m_stock.info
    balance_sheet = m_stock.balance_sheet

    m_stockData = {
        "stock": stock,
        "currentPrice": info.get("currentPrice", None),
        "forwardPE": info.get("forwardPE", None),
        "revenuePerShare": info.get("revenuePerShare", None),
        "dividentYield": info.get("dividentYield", None),
        "52WeekHigh": info.get("52WeekHigh", None),
        "52WeekLow": info.get("52WeekLow", None),
        "equity": balance_sheet.loc['Total Stockholder Equity'][0] if 'Total Stockholder Equity' in balance_sheet.index else None,
        "debt": balance_sheet.loc['Total Debt'][0] if 'Total Debt' in balance_sheet.index else None
    }

    return m_stockData

