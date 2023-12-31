# Databricks notebook source
# MAGIC %fs ls
# MAGIC

# COMMAND ----------

from pyspark.sql import *
from pyspark.sql.functions import *

# COMMAND ----------

# dbutils.fs.mount(
#   source = "wasbs://raw@saunextadls.blob.core.windows.net",
#   mount_point = "/mnt/saunextadls/raw",
#   extra_configs = {"fs.azure.account.key.saunextadls.blob.core.windows.net":"DsZWJs7JVVHZz1I7GKyclV8ejCdj0V2UkqMlgAp6QyVOw5rvrHvmVTgwcThdHUymWg7MXon65/0z+AStj4Yiug=="})

# COMMAND ----------

# %fs ls dbfs:/mnt/saunextadls


# COMMAND ----------

df=spark.read.json("dbfs:/mnt/saunextadls/raw/json")

# COMMAND ----------

# df.display()

# COMMAND ----------

 df1=df.withColumn("ingestiondate",current_timestamp()).withColumn("path",input_file_name())

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema  if not exists json

# COMMAND ----------

df1.write.mode("overwrite").option("path","dbfs:/mnt/saunextadls/raw/output/manohar/json").saveAsTable("json.bronze")

# COMMAND ----------

# MAGIC %sql 
# MAGIC select count(*) from json.bronze

# COMMAND ----------


