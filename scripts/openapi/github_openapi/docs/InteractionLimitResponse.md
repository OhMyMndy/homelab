# InteractionLimitResponse

Interaction limit settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | [**InteractionGroup**](InteractionGroup.md) |  | 
**origin** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.interaction_limit_response import InteractionLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionLimitResponse from a JSON string
interaction_limit_response_instance = InteractionLimitResponse.from_json(json)
# print the JSON string representation of the object
print(InteractionLimitResponse.to_json())

# convert the object into a dict
interaction_limit_response_dict = interaction_limit_response_instance.to_dict()
# create an instance of InteractionLimitResponse from a dict
interaction_limit_response_from_dict = InteractionLimitResponse.from_dict(interaction_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


