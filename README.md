# Inventory CRUD SQL

A robust inventory management system for laptops, featuring full CRUD (Create, Read, Update, Delete) operations with SQL database integration and CSV report generation.

## Features
- **SQL-based Persistence:** Efficiently manage laptop inventory records using SQL.
- **Reporting:** Export inventory data to CSV format for external analysis.
- **Modular Architecture:** Organized folder structure for better maintainability and code clarity.
- **Portability:** Uses relative paths to ensure the system runs correctly across different environments.
- **Data Isolation:** Separates logic from data by utilizing a dedicated `/data` directory.

## Technical Context
- **Language / Localization:** This project was developed in a Peruvian environment. Therefore, the user interface and variable names in the code are in Spanish.

## Project Structure
- `/config`: Database connection and configuration settings.
- `/crud`: Core logic for managing inventory (Add, Read, Update, Delete).
- `/data`: Storage for the inventory database and system logs.
- `/utils`: Utility scripts, including CSV export functionality.
- `main.py`: The main entry point and interactive menu.

## Prerequisites
- **Python:** Version 3.8 or higher.
- **Dependencies:** The project uses standard Python libraries, so no additional external installations are typically required for basic functionality.
