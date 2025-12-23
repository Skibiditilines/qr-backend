from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import Account
from app.schemas.user import UserLogin, Token
from app.services.hash_service import verify_password
from app.core.security import create_access_token

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    # Buscar el usuario por account_user
    db_user = db.query(Account).filter(Account.account_user == user_data.account_user).first()
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    
    # Verificar la contraseña usando el hash_service
    if not verify_password(user_data.account_password, db_user.account_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    
    if not db_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cuenta desactivada"
        )
    
    # Generar el Token
    access_token = create_access_token(
        data={"sub": db_user.account_user}
    )
        
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
