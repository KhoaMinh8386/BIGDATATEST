from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_spark_session(app_name="BigDataTest"):
    """Creates a Spark session."""
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

def filter_high_price(df, threshold=0.05):
    """Filters products with price higher than threshold."""
    return df.filter(col("price") > threshold)

def count_by_channel(df):
    """Counts sales by channel id."""
    return df.groupBy("sales_channel_id").count()
