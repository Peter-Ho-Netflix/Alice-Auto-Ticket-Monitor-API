from fastapi import APIRouter, Query, Path
from typing import Literal
from Monitor_DM import DM
from Monitor_MY import MY
from Monitor_FWD import FWD
from Monitor_PXQ import PXQ

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello World"}

@router.get("/show-infos/{platform}/{show_id}")
def show_infos(platform: Literal["dm", "my", "fwd", "pxq"] = Path(description="购票平台，dm:大麦，my:猫眼，fwd:纷玩岛，pxq:票星球"), show_id: str = Path(description="演出id"), show_name: str = Query(description="演出名称")):
    perform = {
        "show_id": show_id,
        "show_name": show_name
    }
    if platform == "dm":
        return DM(perform).get_show_infos()
    elif platform == "my":
        return MY(perform).get_show_infos()
    elif platform == "fwd":
        return FWD(perform).get_show_infos()
    elif platform == "pxq":
        return PXQ(perform).get_show_infos()
    return {"message": "Hello World"}

@router.get("/monitor/{platform}/{show_id}")
def monitor(platform: str, show_id: str):
    return {"message": "Hello World"}