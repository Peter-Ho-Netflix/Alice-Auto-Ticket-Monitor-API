from fastapi import FastAPI
import json
import uvicorn

api_config = json.load(open("config.json", "r", encoding="utf-8")).get("api")   

app = FastAPI(
    title=api_config.get("title"),
    description=api_config.get("description"),
    version=api_config.get("version"),
    contact=api_config.get("contact"),
    license_info=api_config.get("license_info"),
    openapi_url=api_config.get("openapi_url"),
)

if __name__ == "__main__":
    uvicorn.run(app, host=api_config.get("host"), port=api_config.get("port"))