from app.user import user_schema, user_model
from fastapi import HTTPException, status, APIRouter
from app.database import database
from app.core.oauth2 import auth_user
from app.core import oauth2 as oauth2, utils

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login")
def login(req_body: user_model.UserBase, db: database):
    user = (
        db.query(user_schema.User)
        .filter(user_schema.User.email == req_body.email)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="invalid credetials"
        )
    if not utils.verify_password(req_body.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="invalid credetials"
        )
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    # create a token and return the same
    return {
        "msg": "user data fetched",
        "token": access_token,
        "token_type": "Bearer",
        "user": user,
    }


@router.get("/list")
def user_list(db: database, page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    users = db.query(user_schema.User).offset(skip).limit(limit).all()
    total_users = db.query(user_schema.User).count()
    return {
        "detail": "User list fetched",
        "data": users,
        "total": total_users,
        "page": page,
        "limit": limit,
    }


@router.post("/add")
def create_user(req_body: user_model.UserBase, db: database, auth_user: auth_user):
    req_body.password = utils.hash_password(req_body.password)
    user = user_schema.User(**req_body.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "detail": "user created",
        "data": user_model.UserOut(
            id=user.id, email=user.email, created_at=user.created_at
        ),
    }


@router.get("/fetch/{id}")
def get_user(id: int, db: database, auth_user: auth_user):
    user = db.query(user_schema.User).filter(user_schema.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    else:
        return {
            "detail": "user fetched",
            "data": user_model.UserOut(
                id=user.id, email=user.email, created_at=user.created_at
            ),
        }


@router.delete("/delete/{id}")
def delete_user(id: int, db: database, auth_user: auth_user):
    user_query = db.query(user_schema.User).filter(user_schema.User.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    else:
        user_query.delete(synchronize_session=False)
        db.commit()
        return {"detail": "user deleted"}
