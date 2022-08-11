import bentoml
from bentoml.io import JSON


def bentoml_service(model_name: str, tag: str = 'latest') -> bentoml.Service:
    runner = bentoml.xgboost.get(f'{model_name}:{tag}').to_runner()
    service = bentoml.Service(f'{model_name}_service', runners=[runner])

    @service.api(input=JSON(), output=JSON())
    def predict(input_data: dict) -> dict:
        res = dict()
        res['y_pred'] = runner.predict.run(input_data)
        return res

    return service
