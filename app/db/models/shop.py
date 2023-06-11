from typing import Optional

from sqlmodel import SQLModel, Field

class ShopModel(SQLModel, table=True):
    
    __tablename__ = "parent"

    id: Optional[int] = Field(
        primary_key=True,
        default=None
    )

    name:str =Field(
        max_length=100,
        unique=True
    )

    description:str =Field(
        max_length=100,
        unique=True  
    )

    count_left:int =Field(
        unique=True  
    )

    create_time:str =Field(
        max_length=100,
        unique=True  
    )

    update_time:str =Field(
        max_length=100,
        unique=True  
    )