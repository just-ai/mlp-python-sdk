from mlp_api.paths.api_mlpgate_account_account_model_model.get import ApiForget
from mlp_api.paths.api_mlpgate_account_account_model_model.post import ApiForpost
from mlp_api.paths.api_mlpgate_account_account_model_model.delete import ApiFordelete


class ApiMlpgateAccountAccountModelModel(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
