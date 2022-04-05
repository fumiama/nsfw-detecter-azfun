# -*- coding: utf-8 -*-
from typing import Optional
from pydantic import BaseModel, PositiveFloat


class OutputData(BaseModel):
    sexy: PositiveFloat
    neutral: PositiveFloat
    porn: PositiveFloat
    hentai: PositiveFloat
    drawings: PositiveFloat
