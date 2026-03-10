# Databricks notebook source
# MAGIC %md
# MAGIC ## Create or Replace & CTAS
# MAGIC 1. Difference between Create or Replace and Drop and Create Table statements
# MAGIC 2. CTAS statement
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Difference between Create or Replace and Drop and Create Table statements
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Behaviour of the DROP and CREATE statements

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.companies;
# MAGIC
# MAGIC CREATE TABLE demo.delta_lake.companies
# MAGIC   (company_id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
# MAGIC    company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING);
# MAGIC
# MAGIC INSERT INTO demo.delta_lake.companies 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),
# MAGIC        ("Microsoft", "1975-04-04", "USA"),
# MAGIC        ("Google", "1998-09-04", "USA"),
# MAGIC        ("Amazon", "1994-07-05", "USA"),
# MAGIC        ("Tencent", "1998-11-11", "China");   

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %md
# MAGIC #### Behaviour of the CREATE OR REPLACE statement

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE demo.delta_lake.companies
# MAGIC   (company_id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
# MAGIC    company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING);
# MAGIC
# MAGIC INSERT INTO demo.delta_lake.companies 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),
# MAGIC        ("Microsoft", "1975-04-04", "USA"),
# MAGIC        ("Google", "1998-09-04", "USA"),
# MAGIC        ("Amazon", "1994-07-05", "USA"),
# MAGIC        ("Tencent", "1998-11-11", "China");   

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. CTAS statement

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE demo.delta_lake.companies_china;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE demo.delta_lake.companies_china
# MAGIC AS
# MAGIC SELECT CAST(company_id AS INT) AS company_id,
# MAGIC        company_name,
# MAGIC        founded_date,
# MAGIC        country 
# MAGIC   FROM demo.delta_lake.companies
# MAGIC  WHERE country = 'China';

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC demo.delta_lake.companies_china;

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE demo.delta_lake.companies_china 
# MAGIC   ALTER COLUMN founded_date COMMENT 'Date the company was founded';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE demo.delta_lake.companies_china 
# MAGIC   ALTER COLUMN company_id SET NOT NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC EXTENDED demo.delta_lake.companies_china ;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies_china;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.delta_lake.companies_china;
