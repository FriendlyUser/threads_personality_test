from fastapi import FastAPI

from app.routers import reports
# from app.middleware import custom_middleware
# from app.exceptions import http_error_handler

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Actions to perform on app startup
    pass

@app.on_event("shutdown")
async def shutdown():
    # Actions to perform on app shutdown
    pass


# Register routers
app.include_router(reports.router)
# app.include_router(users.router)

# Register exception handlers 
# app.add_exception_handler(HTTPException, http_error_handler)