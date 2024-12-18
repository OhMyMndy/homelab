# GetAwsExternalIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reusable** | **bool** | If set to true, this same AWS external id will be returned on future calls to this endpoint, if and only if those calls also mark &#x60;reusable&#x60; as true, and the ID has not yet been linked with an AWS account. | [optional] 

## Example

```python
from tailscale_openapi.models.get_aws_external_id_request import GetAwsExternalIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAwsExternalIdRequest from a JSON string
get_aws_external_id_request_instance = GetAwsExternalIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetAwsExternalIdRequest.to_json())

# convert the object into a dict
get_aws_external_id_request_dict = get_aws_external_id_request_instance.to_dict()
# create an instance of GetAwsExternalIdRequest from a dict
get_aws_external_id_request_from_dict = GetAwsExternalIdRequest.from_dict(get_aws_external_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


