from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder.appName("TarunPySparkDemo").getOrCreate()

# Sample data
data = [
    ("Tarun", "QA", 50000),
    ("Alex", "Dev", 80000),
    ("Meera", "QA", 60000),
    ("John", "Dev", 90000)
]

# Create DataFrame
columns = ["Name", "Department", "Salary"]
df = spark.createDataFrame(data, columns)

# Show data
print("Original Data: ")
df.show()

#Filter example
print("QA Employees:")
df.filter(col("Department") == "QA").show()

# Group By example
print("Average Salary by Department: ")
df.groupBy("Department").avg("Salary").show()

# Stop Spark Session
spark.stop()