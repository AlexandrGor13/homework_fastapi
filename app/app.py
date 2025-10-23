from typing import Annotated

import uvicorn
from fastapi import FastAPI, HTTPException, Body, Path, Depends
from fastapi_keycloak import FastAPIKeycloak, OIDCUser

from ml import translate
from schemas import Text, UserLogin

app = FastAPI(title="ML Model API")

keycloak = FastAPIKeycloak(
    server_url="http://localhost:8080/",
    client_id="ml-fastapi",
    client_secret="kparjV5AiVpYNutupa3EPnmZp336woPF",
    admin_client_id="admin-fastapi",
    admin_client_secret="Bk3sYdhAqKQXb2dNfJE5fKngLLwDLqIP",
    realm="fastapi-realm",
    callback_uri="http://localhost:8000/callback",
    ssl_verification=False,
)
keycloak.add_swagger_config(app)

@app.get("/")
def read_root():
    return {"message": "Welcome to the text translation API"}


@app.post("/translation/{src}-{dest}", response_model=Text)
def translation(
        text: Annotated[Text, Body()],
        src: Annotated[str, Path(pattern=r'^(ru|en)$')],
        dest: Annotated[str, Path(pattern=r'^(ru|en)$')],
        user: OIDCUser = Depends(keycloak.get_current_user(required_roles=["user"])),
):
    try:
        translated_text = translate(text, src, dest) if src != dest else text
        return translated_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
async def login(user_data: UserLogin):
    """Get a GWT-token by creds"""
    try:
        # Get user's token
        token = keycloak.user_login(
            username=user_data.username,
            password=user_data.password
        )
        return {
            "access_token": token.access_token,
            "refresh_token": token.refresh_token,
            "token_type": "Bearer"
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Authentification failed: {str(e)}"
        )


@app.get("/flexible")
async def flexible_route(user: OIDCUser = Depends(keycloak.get_current_user())):
    """Accessible for admins and users"""
    if "admin" not in user.roles and "user" not in user.roles:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"message": "Access granted"}


@app.get("/admin")
async def admin_route(user: OIDCUser = Depends(keycloak.get_current_user(required_roles=["admin"]))):
    """Only accessible by admins"""
    return {"message": "Admin access granted", "user": user}


@app.get("/callback", tags=["auth-flow"])
def callback(session_state: str, code: str):
    return keycloak.exchange_authorization_code(session_state=session_state, code=code)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
