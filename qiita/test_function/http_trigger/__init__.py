import json
from logging import getLogger, INFO

import azure.functions as func
from cerberus import Validator

logger = getLogger()
logger.setLevel(INFO)


# Validation
SCHEMA = {
    "name": {"type": "string"}
}


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    以下のようなpayloadを受け取る関数
    ```
        {
            "name": "taro",
            "age": 10
        }
    ```

    Args:
        req: request

    Returns:

    """
    # POSTのみを対象としているため
    payload = req.get_json()

    # バリデータを作成
    validator = Validator(SCHEMA)

    # バリデーションがうまく通らない場合エラーを吐く
    # 不明なパラメータの入力も`allow_unknown`で許可している
    if not validator.validate(payload, allow_unknown=True):
        return func.HttpResponse(
            body=json.dumps(validator.errors),
            mimetype="application/json",
            charset="utf-8",
            status_code=400
        )

    # 正しい入力があった場合は、受け取ったpayloadをそのまま返す
    return func.HttpResponse(
        body=json.dumps(payload),
        mimetype="application/json",
        charset="utf-8",
        status_code=200
    )
