# Databricks notebook source
# MAGIC %md
# MAGIC ## Understanding Delta Lake Transaction Log
# MAGIC Understand the cloud storage directory structure behind delta lake tables

# COMMAND ----------

# MAGIC %md
# MAGIC Delta Lake is a storage layer on top of a data lake that provides ACID transactions, schema enforcement, and reliable data processing.

# COMMAND ----------

# MAGIC %md
# MAGIC Here are the key characteristics of Delta Lake (very short):
# MAGIC
# MAGIC ACID Transactions – reliable data operations
# MAGIC
# MAGIC Schema Enforcement – prevents bad data
# MAGIC
# MAGIC Schema Evolution – allows new columns
# MAGIC
# MAGIC Time Travel – query old versions of data
# MAGIC
# MAGIC Upserts (MERGE) – update & delete support
# MAGIC
# MAGIC Scalable Metadata Handling – handles big data efficiently
# MAGIC
# MAGIC Data Versioning – keeps table history
# MAGIC
# MAGIC Unified Batch + Streaming – works with both

# COMMAND ----------

# MAGIC %md
# MAGIC ####Delta Lake architecture consists of Parquet data files and a transaction log (_delta_log) that tracks all changes and enables ACID transactions. 🚀

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1773141078488.png](./image_1773141078488.png "image_1773141078488.png")

# COMMAND ----------

# MAGIC %md
# MAGIC #### 0. Create a new schema under the demo catalog for this section of the course (delta_lake)

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog if not exists demo
# MAGIC managed location 'abfss://demo@deacourseextdlshubh.dfs.core.windows.net';

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS demo.delta_lake
# MAGIC     MANAGED LOCATION 'abfss://demo@deacourseextdlshubh.dfs.core.windows.net/delta_lake';

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1773141138452.png](./image_1773141138452.png "image_1773141138452.png")

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1. Create a Delta Lake Table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS demo.delta_lake.companies
# MAGIC   (company_name STRING,
# MAGIC    founded_date DATE,
# MAGIC    country      STRING);

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC EXTENDED demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2. Insert some data

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO demo.delta_lake.companies
# MAGIC VALUES ("Apple", "1976-04-01", "USA");

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %md
# MAGIC #### 3. Insert some more data

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO demo.delta_lake.companies 
# MAGIC VALUES ("Microsoft", "1975-04-04", "USA"),
# MAGIC        ("Google", "1998-09-04", "USA"),
# MAGIC        ("Amazon", "1994-07-05", "USA");
