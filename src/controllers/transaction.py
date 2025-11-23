from fastapi import APIrouter, Depends, status
from src.schemas.transaction import TransactionIn
from src.security import login_required
from src.services.transaction import TransactionService
from src.views.transaction import TransactionOut

router = APIrouter()

service = TransactionService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
    return await service.create(transaction)
