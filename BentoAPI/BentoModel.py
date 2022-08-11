import bentoml
import xgboost as xgb
from datetime import datetime


def make_label():
    now = datetime.now()
    time_tag = now.strftime("%Y%m%d%H%M")
    return time_tag


def XGBoost(x_data, y_data,
            model_name: str,
            num_class: int = 2,
            train_type: str = 'clf'):
    # TBA: reg, else 해야함.
    clf = xgb.DMatrix(x_data, label=y_data) if train_type == 'clf' else xgb.DMatrix(x_data, label=y_data)
    param = {"max_depth": 3, "eta": 0.3, "objective": "multi:softprob", "num_class": num_class}
    fitted_clf = xgb.train(param, clf)
    saved_model = bentoml.xgboost.save_model(
        f'{model_name}:{make_label()}',
        fitted_clf
    )
    return f'{saved_model.tag}'
