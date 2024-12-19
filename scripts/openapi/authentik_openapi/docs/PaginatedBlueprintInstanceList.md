# PaginatedBlueprintInstanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[BlueprintInstance]**](BlueprintInstance.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_blueprint_instance_list import PaginatedBlueprintInstanceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBlueprintInstanceList from a JSON string
paginated_blueprint_instance_list_instance = PaginatedBlueprintInstanceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBlueprintInstanceList.to_json())

# convert the object into a dict
paginated_blueprint_instance_list_dict = paginated_blueprint_instance_list_instance.to_dict()
# create an instance of PaginatedBlueprintInstanceList from a dict
paginated_blueprint_instance_list_from_dict = PaginatedBlueprintInstanceList.from_dict(paginated_blueprint_instance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


