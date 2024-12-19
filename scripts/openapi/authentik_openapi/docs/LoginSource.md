# LoginSource

Serializer for Login buttons of sources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**icon_url** | **str** |  | [optional] 
**challenge** | [**LoginChallengeTypes**](LoginChallengeTypes.md) |  | 

## Example

```python
from authentik_openapi.models.login_source import LoginSource

# TODO update the JSON string below
json = "{}"
# create an instance of LoginSource from a JSON string
login_source_instance = LoginSource.from_json(json)
# print the JSON string representation of the object
print(LoginSource.to_json())

# convert the object into a dict
login_source_dict = login_source_instance.to_dict()
# create an instance of LoginSource from a dict
login_source_from_dict = LoginSource.from_dict(login_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


