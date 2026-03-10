# Databricks notebook source
# MAGIC %md
# MAGIC ## Create Table - Table & Column Properties
# MAGIC Demonstrate adding Table and Column Properties to the CREATE TABLE statement. 
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Table Properties
# MAGIC       1.1. COMMENT - allows you to document the purpose of the table. 
# MAGIC       1.2. TBLPROPERTIES - used to specify table level metadata or configuration settings
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.companies;
# MAGIC CREATE TABLE demo.delta_lake.companies
# MAGIC   (company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING)
# MAGIC COMMENT 'This table contains information about some of the successful tech companies'   
# MAGIC TBLPROPERTIES ('sensitive' = 'true', 'delta.enableDeletionVectors' = 'false');

# COMMAND ----------

# MAGIC %md
# MAGIC 1️⃣ sensitive = true
# MAGIC
# MAGIC Marks the table as containing sensitive data (like PII).
# MAGIC
# MAGIC Mainly used for governance, security policies, or catalog tagging.
# MAGIC
# MAGIC Helps tools identify confidential datasets.
# MAGIC
# MAGIC ✅ Example: tables containing user emails, phone numbers, personal data.
# MAGIC
# MAGIC 2️⃣ delta.enableDeletionVectors = false
# MAGIC
# MAGIC Controls Deletion Vectors in Delta Lake.
# MAGIC
# MAGIC Deletion vectors allow row-level deletes without rewriting Parquet files.
# MAGIC
# MAGIC Setting it to false disables this optimization.
# MAGIC
# MAGIC Meaning:
# MAGIC
# MAGIC Deletes will rewrite data files instead of marking rows as deleted.

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC EXTENDED demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Column Properties
# MAGIC       2.1 NOT NULL Constraints - enforces data integrity and quality by ensuring that a specific column cannot contain NULL values
# MAGIC       2.2 COMMENT - documents the purpose or context of individual columns in a table

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.companies;
# MAGIC CREATE TABLE demo.delta_lake.companies
# MAGIC   (company_name STRING NOT NULL,
# MAGIC    founded_date DATE COMMENT 'The date the company was founded',
# MAGIC    country      STRING)
# MAGIC COMMENT 'This table contains information about some of the successful tech companies'   
# MAGIC TBLPROPERTIES ('sensitive' = 'true', 'delta.enableDeletionVectors' = 'false');

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC EXTENDED demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Column Properties
# MAGIC       2.3 Generated Columns - derived or computed columns, whose values are computed at the time of inserting a new records
# MAGIC           2.3.1. Generated Identity Columns - used to generate an identity for example a primary key value
# MAGIC           2.3.2. Generated Computed Columns - automatically calculate and store derived values based on other columns in the same table.

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2.3.1. Generated Identity Columns
# MAGIC `GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY [ ( [ START WITH start ] [ INCREMENT BY step ] ) ]`

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.companies;
# MAGIC CREATE TABLE demo.delta_lake.companies
# MAGIC   (company_id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
# MAGIC    company_name STRING NOT NULL,
# MAGIC    founded_date DATE COMMENT 'The date the company was founded',
# MAGIC    country      STRING)
# MAGIC COMMENT 'This table contains information about some of the successful tech companies'   
# MAGIC TBLPROPERTIES ('sensitive' = 'true', 'delta.enableDeletionVectors' = 'false');

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO demo.delta_lake.companies 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),
# MAGIC        ("Microsoft", "1975-04-04", "USA"),
# MAGIC        ("Google", "1998-09-04", "USA"),
# MAGIC        ("Amazon", "1994-07-05", "USA");

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies ;

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2.3.2. Generated Computed Columns
# MAGIC GENERATED ALWAYS AS ( `expr` )
# MAGIC
# MAGIC `expr` may be composed of literals, column identifiers within the table, and deterministic, built-in SQL functions or operators except:
# MAGIC - Aggregate functions
# MAGIC - Analytic window functions
# MAGIC - Ranking window functions
# MAGIC - Table valued generator functions
# MAGIC
# MAGIC Also `expr` must not contain any subquery.

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.companies;
# MAGIC CREATE TABLE demo.delta_lake.companies
# MAGIC   (company_id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
# MAGIC    company_name STRING NOT NULL,
# MAGIC    founded_date DATE COMMENT 'The date the company was founded',
# MAGIC    founded_year INT GENERATED ALWAYS AS (YEAR(founded_date)),
# MAGIC    country      STRING)
# MAGIC COMMENT 'This table contains information about some of the successful tech companies'   
# MAGIC TBLPROPERTIES ('sensitive' = 'true', 'delta.enableDeletionVectors' = 'false');

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO demo.delta_lake.companies 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),
# MAGIC        ("Microsoft", "1975-04-04", "USA"),
# MAGIC        ("Google", "1998-09-04", "USA"),
# MAGIC        ("Amazon", "1994-07-05", "USA");

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies;
