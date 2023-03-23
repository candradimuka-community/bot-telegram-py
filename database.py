# host    : db-jcc-aio-4326.8nk.cockroachlabs.cloud
# port    : 26257
# database: platform_telegram_ajcc
# username: chairman
# password: Wqsv8nVZjaLSsOUVKcbX8g

# ----------
# pyAlchemy

# $env:DATABASE_URL = "cockroachdb://chairman:<ENTER-SQL-USER-PASSWORD>@db-jcc-aio-4326.8nk.cockroachlabs.cloud:26257/platform_telegram_ajcc?sslmode=verify-full"
# --------------
import os
from sqlalchemy import create_engine, text

engine = create_engine(os.environ["DATABASE_URL"])
conn = engine.connect()

res = conn.execute(text("SELECT now()")).fetchall()
print(res)