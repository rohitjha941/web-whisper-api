from fastapi import APIRouter, HTTPException, Depends
from fastapi import HTTPException
from auth import schemas, helpers, exceptions
# from jose import JWTError, jwt
from auth.models import *

router = APIRouter(
    prefix="/v1/auth",
)


@router.post("/login")
async def login(data: schemas.LoginSchema):
    user = await helpers.validatePassword(data.password, data.email)
    return helpers.returnUser(user)


@router.post("/register")
async def register(data: schemas.RegisterSchema):
    """
    We need to take p1 and p2 and also provision for password rules
    """
    if data.password1 != data.password2:
        raise HTTPException(
            status_code=400,
            detail=[{
                "type":"incorrect_password",
                "msg":"Passwords does not matches"
            }]
        )
    name = data.email.split("@")[0]
    user = await User.create(
        email=data.email, password=helpers.generateHash(data.password1), name=name
    )
    return helpers.returnUser(user)


@router.get("/token/validate")
async def validateTokenAPI(user=Depends(helpers.validateToken)):
    return helpers.returnUser(user)


@router.post("/password/change")
async def changePassword(
    data: schemas.NewPasswordSchema, user=Depends(helpers.validateToken)
):
    if data.newpassword1 != data.newpassword2:
        raise HTTPException(
            status_code=400,
            detail="Passwords does not matches",
        )
    user.password = helpers.generateHash(data.newpassword1)
    await user.save()
    return helpers.returnUser(user)
