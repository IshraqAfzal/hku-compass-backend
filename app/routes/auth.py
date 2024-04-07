from fastapi import APIRouter, Request

router = APIRouter(
  prefix="/auth",
  tags=["Authentication"]
)