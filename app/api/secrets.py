from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Secret
from app.services.crypto import encrypt, decrypt
from app.services.audit import log_action
from uuid import UUID

router = APIRouter(prefix="/secrets")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_secret(value: str, user_id: UUID, db: Session = Depends(get_db)):
    secret = Secret(
        encrypted_value=encrypt(value),
        owner_id=user_id
    )
    db.add(secret)
    db.commit()
    log_action(db, user_id, "CREATE", secret.id)
    return {"id": secret.id}

@router.get("/{secret_id}")
def get_secret(secret_id: UUID, user_id: UUID, db: Session = Depends(get_db)):
    secret = db.query(Secret).filter(Secret.id == secret_id).first()
    if not secret or secret.owner_id != user_id:
        raise HTTPException(status_code=403)
    log_action(db, user_id, "READ", secret_id)
    return {"value": decrypt(secret.encrypted_value)}
