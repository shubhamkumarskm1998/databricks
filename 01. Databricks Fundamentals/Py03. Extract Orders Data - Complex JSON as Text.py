# Databricks notebook source
# MAGIC %md
# MAGIC ## Extract Data From the Orders JSON File
# MAGIC 1. Query Orders File using JSON Format
# MAGIC 1. Query Orders File using TEXT Format
# MAGIC 1. Create Orders Table in Bronze Schema

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Query Orders File using JSON Format

# COMMAND ----------

df = spark.read.format("json").load("/Volumes/ginzobox/landing/operational_data/orders")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Query Orders File using TEXT Format

# COMMAND ----------

df= spark.read.text("/Volumes/ginzobox/landing/operational_data/orders")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Create Orders View in Bronze Schema

# COMMAND ----------

df.writeTo("ginzobox.bronze.py_orders").createOrReplace()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM ginzobox.bronze.py_orders;
