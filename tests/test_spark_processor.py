import pytest
from src.spark_processor import get_spark_session, filter_high_price, count_by_channel
from pyspark.sql import Row

@pytest.fixture(scope="session")
def spark():
    """Fixture for Spark session."""
    return get_spark_session("PyTestSession")

def test_filter_high_price(spark):
    """Tests the filter_high_price function."""
    data = [
        Row(article_id="1", price=0.01),
        Row(article_id="2", price=0.06),
        Row(article_id="3", price=0.051)
    ]
    df = spark.createDataFrame(data)
    
    result_df = filter_high_price(df, threshold=0.05)
    
    assert result_df.count() == 2
    assert result_df.filter(col("article_id") == "1").count() == 0

def test_count_by_channel(spark):
    """Tests the count_by_channel function."""
    data = [
        Row(sales_channel_id=1),
        Row(sales_channel_id=1),
        Row(sales_channel_id=2)
    ]
    df = spark.createDataFrame(data)
    
    result_df = count_by_channel(df)
    counts = result_df.collect()
    
    # Convert to dict for easier testing
    count_dict = {row["sales_channel_id"]: row["count"] for row in counts}
    
    assert count_dict[1] == 2
    assert count_dict[2] == 1

from pyspark.sql.functions import col
