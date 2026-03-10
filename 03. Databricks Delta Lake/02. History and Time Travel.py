# Databricks notebook source
# MAGIC %md
# MAGIC ## History and Time Travel
# MAGIC 1. Query Delta Lake table history
# MAGIC 1. Query previous versions of the data
# MAGIC 1. Query data from a specific time. 
# MAGIC 1. Restore data to a specific version.

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1. Query Delta Lake Table History

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2. Query Data from a Specific Version

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies version as of 0;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies
# MAGIC VERSION AS OF 1;

# COMMAND ----------

# MAGIC %md
# MAGIC #### 3. Query Data from a Specific Time

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies
# MAGIC TIMESTAMP AS OF '2025-01-07T11:45:12.000+00:00';
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### 4. Restore Data in the Table to a Specific Version

# COMMAND ----------

# MAGIC %sql
# MAGIC RESTORE TABLE demo.delta_lake.companies VERSION AS OF 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.delta_lake.companies;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.delta_lake.companies;
