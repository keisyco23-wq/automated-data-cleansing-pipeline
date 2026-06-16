# Corporate Data Cleansing & ETL Pipeline — Python Automation

## 📌 Business Problem & Objective
A multinational operations firm struggled with a legacy database that exported heavily corrupted CSV files. Human errors included mismatched date formats, duplicate records, blank revenue fields, and negative product quantities, which broke the business intelligence dashboards downstream.

The objective was to write a robust Python script using the Pandas library to automate the extraction, cleansing, and structural normalization of raw corporate files, cutting weekly manual preparation time from hours to seconds.

---

## 🛠️ Python & Libraries Stack
* **Pandas:** Utilized for vectorized data manipulation, handling datetime objects, and missing record imputations.
* **NumPy:** Deployed for conditional business logic mapping and mathematical error correction.

---

## 📊 Business Key Results & Actionable Insights
* **Operational Efficiency:** Replaced manual Excel filtering with a programmatic pipeline, ensuring **100% data formatting conformity** before ingestion.
* **Data Integrity Guardrails:** The script automatically flags data anomalies (like negative sales volume) and infers missing revenue using historical media structures, preventing visual errors in corporate reports.
