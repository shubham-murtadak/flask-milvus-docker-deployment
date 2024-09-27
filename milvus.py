import time
from pymilvus import MilvusClient, DataType

client = MilvusClient(
    uri="http://localhost:19530"
)


schema = MilvusClient.create_schema(
    auto_id=False,
    enable_dynamic_field=True,
)

schema.add_field(field_name="my_id", datatype=DataType.INT64, is_primary=True)
schema.add_field(field_name="my_vector", datatype=DataType.FLOAT_VECTOR, dim=5)

index_params = client.prepare_index_params()

index_params.add_index(
    field_name="my_id",
    index_type="STL_SORT"
)

index_params.add_index(
    field_name="my_vector", 
    index_type="IVF_FLAT",
    metric_type="IP",
    params={ "nlist": 128 }
)


client.create_collection(
    collection_name="customized_setup_1",
    schema=schema,
    index_params=index_params
)

time.sleep(5)

res = client.get_load_state(
    collection_name="customized_setup_1"
)

print(res)

# 5. View Collections
res = client.describe_collection(
    collection_name="customized_setup_1"
)

# print(res)


# 6. List all collection names
res = client.list_collections()

print(res)
