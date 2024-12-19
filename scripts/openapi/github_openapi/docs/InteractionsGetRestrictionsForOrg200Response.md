# InteractionsGetRestrictionsForOrg200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | [**InteractionGroup**](InteractionGroup.md) |  | 
**origin** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.interactions_get_restrictions_for_org200_response import InteractionsGetRestrictionsForOrg200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionsGetRestrictionsForOrg200Response from a JSON string
interactions_get_restrictions_for_org200_response_instance = InteractionsGetRestrictionsForOrg200Response.from_json(json)
# print the JSON string representation of the object
print(InteractionsGetRestrictionsForOrg200Response.to_json())

# convert the object into a dict
interactions_get_restrictions_for_org200_response_dict = interactions_get_restrictions_for_org200_response_instance.to_dict()
# create an instance of InteractionsGetRestrictionsForOrg200Response from a dict
interactions_get_restrictions_for_org200_response_from_dict = InteractionsGetRestrictionsForOrg200Response.from_dict(interactions_get_restrictions_for_org200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


