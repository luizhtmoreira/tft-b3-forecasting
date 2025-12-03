import pandas as pd
import yfinance as yf
import os

def download_data(tickers=["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA", "ABEV3.SA"], 
                 start_date="2015-01-01", end_date="2023-01-01"):
    """
    Pipeline de ingestão de dados Multi-Ativo: Yahoo Finance + NEFIN.
    Gera o dataset para o Global Forecasting Model.
    """
    print(f"--- Iniciando ETL para {len(tickers)} ativos ---")
    
    #Processar NEFIN (Fatores são iguais para todos)
    #O arquivo nefin_factors.csv deve estar na raiz
    nefin_path = "nefin_factors.csv"
    if not os.path.exists(nefin_path):
        print(f"Erro: Arquivo {nefin_path} não encontrado. Abortando.")
        return None

    try:
        df_nefin = pd.read_csv(nefin_path)
        if 'Date' not in df_nefin.columns:
             print("Erro: Coluna 'Date' não encontrada no CSV do NEFIN.")
             return None
             
        df_nefin['Date'] = pd.to_datetime(df_nefin['Date'])
        df_nefin.set_index('Date', inplace=True)
        df_factors = df_nefin[['Rm_minus_Rf', 'SMB', 'HML']]
    except Exception as e:
        print(f"Erro ao ler NEFIN: {e}")
        return None

    lista_dfs = []
    
    for t in tickers:
        print(f"Baixando: {t}...")
        try:
            df_yahoo = yf.download(t, start=start_date, end=end_date, auto_adjust=False, progress=False)

            if isinstance(df_yahoo.columns, pd.MultiIndex):
                df_yahoo = df_yahoo.xs(t, axis=1, level=1)

            df_clean = df_yahoo[['Adj Close', 'Volume']].rename(columns={'Adj Close': 'Close'})

            df_clean['Ticker_ID'] = t 

            df_merged = pd.merge(df_clean, df_factors, left_index=True, right_index=True, how='left')

            df_merged.ffill(inplace=True)
            
            lista_dfs.append(df_merged)
            
        except Exception as e:
            print(f"Erro ao baixar {t}: {e}")

    if len(lista_dfs) > 0:
        df_final = pd.concat(lista_dfs)
        print(f"--- Sucesso! Dataset Global montado: {df_final.shape} linhas ---")
        return df_final
    else:
        return None

if __name__ == "__main__":
    df = download_data()
    if df is not None:
        print(df.head())
        print(df.tail())
