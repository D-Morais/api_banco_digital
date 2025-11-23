from enum import Enum
from src.database import metadata
from sqlalchemy import Column, Table, Integer, ForeignKey, Numeric, TIMESTAMP
import sqlalchemy as sa


class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


transactions = Table(
    "transactions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("account_id", Integer, ForeignKey("accounts.id"), nullable=False),
    Column("type", sa.Enum(TransactionType, name="transaction_types"), nullable=False),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("timestamp", TIMESTAMP(timezone=True))
)
