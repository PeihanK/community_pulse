from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.categories import CategoryBase


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: int  # Добавляем поле category_id для создания вопроса


class QuestionResponse(BaseModel):
    id: int
    text: str
    category: CategoryBase  # Добавляем категорию в ответ

    class Config:
        # Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
        from_attributes = True


class MessageResponse(BaseModel):
    message: str

    class Config:
        from_attributes = True
