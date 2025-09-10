import yfinance as yf
import json
import pullData


def main():
    print("Please Enter exact stock name: ")
    m_stock = str(input().upper())
    stockData: dict = pullData.pstockData_JSON(m_stock)
    print(stockData)

if __name__ == "__main__":
    main()