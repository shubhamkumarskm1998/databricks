# Databricks notebook source
# MAGIC %md
# MAGIC ## Insert Overwrite
# MAGIC 1. Replace all the data in a table
# MAGIC 1. Replace all the data from a specific partition
# MAGIC 1. How to handle schema changes

# COMMAND ----------

# MAGIC %md
# MAGIC INSERT OVERWITE - Overwrites the existing data in a table or a specific partition with the new data. 
# MAGIC
# MAGIC INSERT INTO - Appends new data
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Replace all the data in a table

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.gold_companies;
# MAGIC
# MAGIC CREATE TABLE demo.delta_lake.gold_companies
# MAGIC   (company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING);
# MAGIC
# MAGIC INSERT INTO demo.delta_lake.gold_companies 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),  
# MAGIC        ("Tencent", "1998-11-11", "China"); 
# MAGIC
# MAGIC SELECT * FROM demo.delta_lake.gold_companies;        

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.bronze_companies;
# MAGIC
# MAGIC CREATE TABLE demo.delta_lake.bronze_companies
# MAGIC   (company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING);
# MAGIC
# MAGIC INSERT INTO demo.delta_lake.bronze_companies 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),
# MAGIC        ("Microsoft", "1975-04-04", "USA"),
# MAGIC        ("Google", "1998-09-04", "USA"),
# MAGIC        ("Amazon", "1994-07-05", "USA"),
# MAGIC        ("Tencent", "1998-11-11", "China");   
# MAGIC
# MAGIC SELECT * FROM demo.delta_lake.bronze_companies;       

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT OVERWRITE TABLE demo.delta_lake.gold_companies
# MAGIC SELECT *
# MAGIC   FROM demo.delta_lake.bronze_companies;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.gold_companies;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.delta_lake.gold_companies;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Replace all the data from a specific partition

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.gold_companies_partitioned;
# MAGIC
# MAGIC CREATE TABLE demo.delta_lake.gold_companies_partitioned
# MAGIC   (company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING)
# MAGIC PARTITIONED BY (country);
# MAGIC
# MAGIC INSERT INTO demo.delta_lake.gold_companies_partitioned 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),  
# MAGIC        ("Tencent", "1998-11-11", "China"); 
# MAGIC
# MAGIC SELECT * FROM demo.delta_lake.gold_companies_partitioned;        

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC EXTENDED demo.delta_lake.gold_companies_partitioned

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS demo.delta_lake.bronze_companies_usa;
# MAGIC
# MAGIC CREATE TABLE demo.delta_lake.bronze_companies_usa
# MAGIC   (company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING);
# MAGIC
# MAGIC INSERT INTO demo.delta_lake.bronze_companies_usa 
# MAGIC (company_name, founded_date, country)
# MAGIC VALUES ("Apple", "1976-04-01", "USA"),
# MAGIC        ("Microsoft", "1975-04-04", "USA"),
# MAGIC        ("Google", "1998-09-04", "USA"),
# MAGIC        ("Amazon", "1994-07-05", "USA");   
# MAGIC
# MAGIC SELECT * FROM demo.delta_lake.bronze_companies_usa;       

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT OVERWRITE TABLE demo.delta_lake.gold_companies_partitioned
# MAGIC PARTITION (country = "USA")
# MAGIC SELECT company_name,
# MAGIC        founded_date
# MAGIC   FROM demo.delta_lake.bronze_companies_usa;     

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.gold_companies_partitioned;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. How to handle schema changes

# COMMAND ----------

# MAGIC %md
# MAGIC Insert Overwrite -> Use to overwrite the data in a table or a partition when there are no schema changes.  
# MAGIC Create or replace table -> Use when there are schema changes. 
# MAGIC
