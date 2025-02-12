from fastapi import APIRouter, status, Request, Depends

from src.api.models import APIResponse, APIRequest
from src.api.controllers import chat_new_message


router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    # dependencies=[Depends(validate_user)]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def router_test() -> APIResponse:
    return APIResponse(
        status_code=200,
        status_message="-- CHAT ROUTER WORKING! --"
    )


@router.post("/new_message", status_code=status.HTTP_200_OK)
async def new_message(api_request: APIRequest, req: Request) -> APIResponse:
    try:
        response = await chat_new_message(
            req.app.database,
            req.app.llm,
            api_request.message,
            api_request.service_name
        )

        return APIResponse(
            status_code=200,
            response={
                "user": api_request.message,
                "ai": response
            }
        )

    except Exception as e:
        return APIResponse(
            status_code=500,
            status_message=f"Error: {e}"
        )
