"""
Trading API routes
Handles trading operations and portfolio management
"""

from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_active_user
from app.models.user import User

router = APIRouter()


@router.get("/portfolio")
async def get_portfolio(current_user: User = Depends(get_current_active_user)):
    """Get current user's portfolio"""
    return {
        "total_value": 1000000,
        "cash_balance": 1000000,
        "invested_value": 0,
        "holdings": []
    }
