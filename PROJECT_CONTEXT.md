You are helping me build a placement-level Enterprise Azure Data Engineering project from scratch. Never simplify the architecture unless I explicitly ask you to.

Project Goal:
Build a complete Medallion Architecture pipeline using Python, Azure Data Lake Storage Gen2, Azure Databricks, Delta Lake, Auto Loader, SQL, and Power BI. Every design decision should resemble real enterprise data engineering practices.

==========================================
PROJECT THEME
==========================================

Source System:
DummyJSON REST API

Endpoints:
- Products
- Users
- Carts

These are the only source datasets.

==========================================
INGESTION ARCHITECTURE
==========================================

Python performs the ingestion.

Requirements:

- REST API extraction
- Dynamic pagination
- Dynamic total record detection
- Multithreading
- Modular code
- Environment variables using .env
- Azure Blob Storage upload using Connection String
- Logging
- Metadata
- GitHub-ready project structure

Folder structure follows enterprise standards.

Python modules include:

config.py
api_client.py (or ingestion.py)
multithreading.py
simulator.py
uploader.py
logger.py
main.py

==========================================
MULTITHREADING DESIGN
==========================================

The pipeline uses two levels of concurrency.

Level 1

Download endpoints simultaneously

Products
Users
Carts

Level 2

Within every endpoint

Download every page concurrently

Example

Products

Page1
Page2
Page3
...

Users

Page1
Page2
...

Carts

Page1
Page2
...

Totals must NEVER be hardcoded.

The API must first request

limit=1

to obtain

response["total"]

Pagination must be generated dynamically.

==========================================
SIMULATOR DESIGN
==========================================

DummyJSON never changes.

Therefore build a Source System Simulator.

Products

Simulate

- price changes
- stock changes
- rating changes
- discount changes
- ingestion_timestamp

Users

DO NOT simulate business changes.

Age
Role
Gender
Name
Birth Date

must remain unchanged.

Only add

ingestion_timestamp

because it represents pipeline ingestion metadata.

Carts

Simulate

- quantity
- totals
- discounted total
- ingestion_timestamp

Use deepcopy() before modifying data.

Never modify the original API response.

==========================================
UPLOAD STRATEGY
==========================================

Upload simulated JSON files to Azure Data Lake Storage Gen2.

Use Azure Blob Storage SDK with Connection String.

Folder hierarchy:

bronze/

products/

YYYY/MM/DD/

products_page_001_timestamp.json

users/

YYYY/MM/DD/

users_page_001_timestamp.json

carts/

YYYY/MM/DD/

carts_page_001_timestamp.json

Every execution must create NEW files.

Never overwrite previous files.

This simulates an incremental landing zone.

==========================================
MEDALLION ARCHITECTURE
==========================================

Bronze

Auto Loader reads raw JSON.

Do NOT join datasets.

Three Delta tables

bronze_products

bronze_users

bronze_carts

==========================================

Silver

Clean each dataset independently.

Products

- deduplicate
- latest timestamp
- merge
- null handling
- schema evolution

Users

- deduplicate
- latest ingestion_timestamp

Carts

- deduplicate
- latest timestamp

No joins in Silver.

==========================================

Gold

Perform business joins only here.

Create

Dim_Product

Dim_User

Fact_Cart

Flatten nested cart products using explode().

Join

Fact_Cart

↓

Dim_Product

↓

Dim_User

This is the reporting layer.

==========================================
POWER BI
==========================================

Power BI connects only to Gold tables.

Possible dashboards

Top Selling Products

Revenue

Customer Spending

Discount Analysis

Inventory

Product Trends

==========================================
PROJECT CODING STYLE
==========================================

Always generate clean production-style Python.

Rules

No unnecessary comments.

Minimal blank lines.

Short readable functions.

Modular architecture.

Avoid hardcoding.

Follow enterprise naming conventions.

Keep every module responsible for only one task.

==========================================
PROJECT OBJECTIVE
==========================================

The final project should demonstrate

Python

REST API

Multithreading

Pagination

Random Source System Simulation

Azure Data Lake Storage

Azure Databricks

Auto Loader

Delta Lake

Bronze

Silver

Gold

MERGE

Window Functions

Schema Evolution

Logging

Metadata

Power BI

GitHub

This should resemble an enterprise production data engineering pipeline suitable for placements, internships, and interviews rather than a beginner tutorial.

Whenever suggesting code or architecture, remain consistent with this design. Do not introduce shortcuts or redesign the pipeline unless explicitly requested.
==========================================
PROJECT PHILOSOPHY
==========================================

Every component should answer one interview question.

Multithreading → "Can you ingest APIs efficiently?"

Simulator → "How do you test incremental pipelines without a changing source?"

Azure Data Lake → "How do you build a landing zone?"

Auto Loader → "How do you perform incremental ingestion?"

Bronze → "How do you preserve raw history?"

Silver → "How do you clean and deduplicate data?"

Gold → "How do you model data for analytics?"

Power BI → "How do business users consume the data?"

Every technology included in the project must have a clear purpose. Avoid adding tools or code that do not strengthen the end-to-end enterprise data engineering workflow.