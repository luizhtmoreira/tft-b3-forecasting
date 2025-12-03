# TFT B3 Forecasting

Research project on critical regime detection and concept drift in the Brazilian Stock Market (B3) using Temporal Fusion Transformers (TFT).

## Objective
To investigate whether Self-Attention mechanisms and Gated Residual Networks can outperform static models (SVM) in directional forecasting and risk management within emerging markets, addressing gaps identified by Souza & Peng (2024).

## Methodology
- **Model:** Temporal Fusion Transformer (implementation via `pytorch-forecasting`).
- **Baseline:** Support Vector Machine (SVM) with RBF Kernel.
- **Data Sources:** - Market Data: IBrX-100 constituents (Yahoo Finance API).
  - Risk Factors: SMB, HML, Rm-Rf (NEFIN).
- **Validation Strategy:** Anchored Walk-Forward Analysis to mitigate look-ahead bias.

## Project Structure
- `src/data_loader.py`: ETL pipeline for multi-asset data ingestion and factor merging.
- `notebooks/`: Exploratory data analysis and model training (WIP).

## Current Status
- [x] Architecture definition and bibliography review.
- [x] Data pipeline implemented (Yahoo + NEFIN).
- [ ] Baseline (SVM) implementation.
- [ ] TFT training and hyperparameter tuning.

## License
MIT
