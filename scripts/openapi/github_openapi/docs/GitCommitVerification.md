# GitCommitVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | 
**reason** | **str** |  | 
**signature** | **str** |  | 
**payload** | **str** |  | 
**verified_at** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.git_commit_verification import GitCommitVerification

# TODO update the JSON string below
json = "{}"
# create an instance of GitCommitVerification from a JSON string
git_commit_verification_instance = GitCommitVerification.from_json(json)
# print the JSON string representation of the object
print(GitCommitVerification.to_json())

# convert the object into a dict
git_commit_verification_dict = git_commit_verification_instance.to_dict()
# create an instance of GitCommitVerification from a dict
git_commit_verification_from_dict = GitCommitVerification.from_dict(git_commit_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


