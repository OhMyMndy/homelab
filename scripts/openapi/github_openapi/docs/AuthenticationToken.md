# AuthenticationToken

Authentication Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token used for authentication | 
**expires_at** | **datetime** | The time this token expires | 
**permissions** | **object** |  | [optional] 
**repositories** | [**List[Repository]**](Repository.md) | The repositories this token has access to | [optional] 
**single_file** | **str** |  | [optional] 
**repository_selection** | **str** | Describe whether all repositories have been selected or there&#39;s a selection involved | [optional] 

## Example

```python
from github_openapi.models.authentication_token import AuthenticationToken

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationToken from a JSON string
authentication_token_instance = AuthenticationToken.from_json(json)
# print the JSON string representation of the object
print(AuthenticationToken.to_json())

# convert the object into a dict
authentication_token_dict = authentication_token_instance.to_dict()
# create an instance of AuthenticationToken from a dict
authentication_token_from_dict = AuthenticationToken.from_dict(authentication_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


