# Databricks notebook source
# MAGIC %md
# MAGIC ### This is my first notebook.

# COMMAND ----------

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# COMMAND ----------

print(pd.__version__)
