-- Databricks notebook source
-- MAGIC %md
-- MAGIC ## Transform Orders Data - String to JSON
-- MAGIC 1. Pre-process the JSON String to fix the Data Quality Issues
-- MAGIC 1. Transform JSON String to JSON Object
-- MAGIC 1. Write transformed data to the silver schema

-- COMMAND ----------

SELECT * 
  FROM ginzobox.bronze.v_orders;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### 1. Pre-process the JSON String to fix the Data Quality Issues
-- MAGIC [regexp_replace function](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/functions/regexp_replace)

-- COMMAND ----------

CREATE OR REPLACE TEMP VIEW tv_orders_fixed
AS
SELECT value,
       regexp_replace(value, '"order_date": (\\d{4}-\\d{2}-\\d{2})', '"order_date": "\$1"') AS fixed_value 
  FROM ginzobox.bronze.v_orders;

-- COMMAND ----------

select schema_of_json(fixed_value) from tv_orders_fixed limit 1;
select from_json(fixed_value,'STRUCT<customer_id: BIGINT, items: ARRAY<STRUCT<category: STRING, details: STRUCT<brand: STRING, color: STRING>, item_id: BIGINT, name: STRING, price: BIGINT, quantity: BIGINT>>, order_date: STRING, order_id: BIGINT, order_status: STRING, payment_method: STRING, total_amount: BIGINT, transaction_timestamp: STRING>') as json_value from tv_orders_fixed;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### 2. Transform JSON String to JSON Object
-- MAGIC - Function [schema_of_json](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/functions/schema_of_json)
-- MAGIC - Function [from_json](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/functions/from_json)

-- COMMAND ----------

SELECT schema_of_json(fixed_value) AS schema,
       fixed_value
  FROM tv_orders_fixed
 LIMIT 1;

-- COMMAND ----------

SELECT from_json(fixed_value, 
                 'STRUCT<customer_id: BIGINT, items: ARRAY<STRUCT<category: STRING, details: STRUCT<brand: STRING, color: STRING>, item_id: BIGINT, name: STRING, price: BIGINT, quantity: BIGINT>>, order_date: STRING, order_id: BIGINT, order_status: STRING, payment_method: STRING, total_amount: BIGINT, transaction_timestamp: STRING>') AS json_value,
       fixed_value
  FROM tv_orders_fixed;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### 3. Write transformed data to the silver schema

-- COMMAND ----------

DROP TABLE IF EXISTS ginzobox.silver.orders_json;
CREATE TABLE IF NOT EXISTS ginzobox.silver.orders_json
AS
SELECT from_json(fixed_value, 
                 'STRUCT<customer_id: BIGINT, items: ARRAY<STRUCT<category: STRING, details: STRUCT<brand: STRING, color: STRING>, item_id: BIGINT, name: STRING, price: BIGINT, quantity: BIGINT>>, order_date: STRING, order_id: BIGINT, order_status: STRING, payment_method: STRING, total_amount: BIGINT, transaction_timestamp: STRING>') AS json_value
  FROM tv_orders_fixed;

-- COMMAND ----------

SELECT * FROM ginzobox.silver.orders_json;
