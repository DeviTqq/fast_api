from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers, fastapi_users

from auth.auth import auth_backend
from auth.datebase import User
from auth.manager import get_user_manager
from auth.schemas import UserCreate, UserRead

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

origins = ["http://localhost:3000", "localhost:3000"]


app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


@app.get("/")
def index():
    return "Hello World!"


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username }"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonym"
