# TokenView

Show token's current key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.token_view import TokenView

# TODO update the JSON string below
json = "{}"
# create an instance of TokenView from a JSON string
token_view_instance = TokenView.from_json(json)
# print the JSON string representation of the object
print(TokenView.to_json())

# convert the object into a dict
token_view_dict = token_view_instance.to_dict()
# create an instance of TokenView from a dict
token_view_from_dict = TokenView.from_dict(token_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


