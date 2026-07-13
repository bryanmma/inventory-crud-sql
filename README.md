# Inventory CRUD SQL

A robust inventory management system for laptops, featuring full CRUD (Create, Read, Update, Delete) operations with SQL database integration and CSV report generation.

## Features
- **SQL-based Persistence:** Efficiently manage laptop inventory records using SQL.
- **Reporting:** Export inventory data to CSV format for external analysis.
- **Modular Architecture:** Organized folder structure for better maintainability and code clarity.
- **Portability:** Uses relative paths to ensure the system runs correctly across different environments.
- **Data Isolation:** Separates logic from data by utilizing a dedicated `/data` directory.

## Technical Context
- **Language / Idioma:** This project was developed as a final assignment for a Python specialization course in Peru. Therefore, variable names and the user interface are in Spanish.
  *(Este proyecto fue desarrollado como trabajo final para una especialización en Python en Perú. Por este motivo, los nombres de las variables y la interfaz de usuario están en español).*

## Project Structure
- `/config`: Database connection and configuration settings.
- `/crud`: Core logic for managing inventory (Add, Read, Update, Delete).
- `/data`: Storage for the inventory database and system logs.
- `/utils`: Utility scripts, including CSV export functionality.
- `main.py`: The main entry point and interactive menu.

## Prerequisites
- **Python:** Version 3.8 or higher.
- **Dependencies:** The project uses standard Python libraries, so no additional external installations are typically required for basic functionality.
