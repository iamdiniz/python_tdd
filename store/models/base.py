import uuid
from bson import Decimal128
from decimal import Decimal
from typing import Any
from pydantic import UUID4, BaseModel, Field, model_serializer
from datetime import datetime


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(default_factory=datetime.utcnow)
    
    @model_serializer
    def set_model(self) -> dict[str, Any]:
        self_dict = dict(self)
        
        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))
                
        return self_dict