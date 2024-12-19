# InteractionLimit

Limit interactions to a specific type of user for a specified duration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | [**InteractionGroup**](InteractionGroup.md) |  | 
**expiry** | [**InteractionExpiry**](InteractionExpiry.md) |  | [optional] 

## Example

```python
from github_openapi.models.interaction_limit import InteractionLimit

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionLimit from a JSON string
interaction_limit_instance = InteractionLimit.from_json(json)
# print the JSON string representation of the object
print(InteractionLimit.to_json())

# convert the object into a dict
interaction_limit_dict = interaction_limit_instance.to_dict()
# create an instance of InteractionLimit from a dict
interaction_limit_from_dict = InteractionLimit.from_dict(interaction_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


