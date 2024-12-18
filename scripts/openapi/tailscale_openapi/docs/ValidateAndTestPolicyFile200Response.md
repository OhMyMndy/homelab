# ValidateAndTestPolicyFile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from tailscale_openapi.models.validate_and_test_policy_file200_response import ValidateAndTestPolicyFile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAndTestPolicyFile200Response from a JSON string
validate_and_test_policy_file200_response_instance = ValidateAndTestPolicyFile200Response.from_json(json)
# print the JSON string representation of the object
print(ValidateAndTestPolicyFile200Response.to_json())

# convert the object into a dict
validate_and_test_policy_file200_response_dict = validate_and_test_policy_file200_response_instance.to_dict()
# create an instance of ValidateAndTestPolicyFile200Response from a dict
validate_and_test_policy_file200_response_from_dict = ValidateAndTestPolicyFile200Response.from_dict(validate_and_test_policy_file200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


