from sqlalchemy import Integer, Table, Column, Numeric, TIMESTAMP
from src.database import metadata

accounts = Table(
    "accounts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("uder_id", Integer, nullable=False, index=True),
    Column("balance", Numeric(10, 2), nullable=False, default=0),
    Column("created_at", TIMESTAMP(timezone=True))
)
