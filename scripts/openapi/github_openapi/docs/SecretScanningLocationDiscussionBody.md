# SecretScanningLocationDiscussionBody

Represents a 'discussion_body' secret scanning location type. This location type shows that a secret was detected in the body of a discussion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discussion_body_url** | **str** | The URL to the discussion where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_discussion_body import SecretScanningLocationDiscussionBody

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationDiscussionBody from a JSON string
secret_scanning_location_discussion_body_instance = SecretScanningLocationDiscussionBody.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationDiscussionBody.to_json())

# convert the object into a dict
secret_scanning_location_discussion_body_dict = secret_scanning_location_discussion_body_instance.to_dict()
# create an instance of SecretScanningLocationDiscussionBody from a dict
secret_scanning_location_discussion_body_from_dict = SecretScanningLocationDiscussionBody.from_dict(secret_scanning_location_discussion_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


