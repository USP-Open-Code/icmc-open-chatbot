from fastapi import HTTPException, Request

from src.api.models import APIRequest
from src.services.llama_guard import LlamaGuard
from src.infrastructure.database import (
    MongoDB,
    get_user_details,
    block_user
)


class Guardrail:
    def __call__(self, api_request: APIRequest, req: Request) -> None:
        if req.app.llama_guard:
            self.llama_guard_layer(
                api_request.message,
                req.app.llama_guard,
                api_request.user_id,
                req.app.database
            )
        self.check_user(api_request.user_id, req.app.database)

    def llama_guard_layer(
        self,
        message: str,
        llama_guard: LlamaGuard,
        user_id: str,
        db: MongoDB
    ) -> None:
        response = llama_guard(message)
        if not response:
            _ = block_user(user_id, db)

            raise HTTPException(
                status_code=400,
                detail=f"""
                    O conteúdo fornecido viola as políticas da plataforma.
                    O seu usuário foi bloqueado.

                    Retorno do LLAMA GUARD: {response}
                """
            )

    def check_user(self, user_id: str, db: MongoDB):
        user_details = get_user_details(user_id, db)
        if user_details and user_details.get("blocked"):
            raise HTTPException(
                status_code=400,
                detail="""
                    O usuário está bloqueado devido a violação de políticas.
                """
            )

    # More Guardrails could be added here.
