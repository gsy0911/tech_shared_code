from datetime import datetime, timezone, timedelta
from logging import getLogger, INFO

import azure.functions as func


logger = getLogger()
logger.setLevel(INFO)


def main(mytimer: func.TimerRequest):
    # 日時の取得
    tz_jst = timezone(timedelta(hours=9))
    today = datetime.now(tz=tz_jst)

    logger.info(f"today: {today}")
