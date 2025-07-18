# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T09:40:38+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, RootModel


class PlayerInfo(BaseModel):
    Name: Optional[str] = None
    PlayerID: Optional[int] = None
    Position: Optional[str] = None
    Team: Optional[str] = None
    TeamID: Optional[int] = None


class Format(Enum):
    xml = 'xml'
    json = 'json'


class Article(BaseModel):
    ArticleID: Optional[int] = None
    Author: Optional[str] = None
    Content: Optional[str] = None
    Players: Optional[List[PlayerInfo]] = None
    Source: Optional[str] = None
    TermsOfUse: Optional[str] = None
    Title: Optional[str] = None
    Updated: Optional[str] = None
    Url: Optional[str] = None


class FieldFormatRotoBallerArticlesGetResponse(RootModel[List[Article]]):
    root: List[Article]


class FieldFormatRotoBallerArticlesByDateDateGetResponse(RootModel[List[Article]]):
    root: List[Article]


class FieldFormatRotoBallerArticlesByPlayerIDPlayeridGetResponse(
    RootModel[List[Article]]
):
    root: List[Article]
