# Databricks notebook source
# MAGIC %md
# MAGIC ## Extract Data From the Memberships - Image Files
# MAGIC 1. Query Memberships File using binaryFile Format
# MAGIC 1. Create Memberships Table in Bronze Schema

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Query Memberships Folder using binaryFile Format

# COMMAND ----------

# MAGIC %fs ls '/Volumes/ginzobox/landing/operational_data/memberships'

# COMMAND ----------

df= spark.read.format('binaryFile').load("/Volumes/ginzobox/landing/operational_data/memberships/2024-10/*.png")
display(df)

# COMMAND ----------

df = spark.read.format('binaryFile').load('/Volumes/ginzobox/landing/operational_data/memberships/*/*.png')
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Create Memberships Table in Bronze Schema

# COMMAND ----------

df.writeTo("ginzobox.bronze.py_memberships").createOrReplace()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM ginzobox.bronze.py_memberships;
