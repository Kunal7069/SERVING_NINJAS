from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.config import engine, Base
from app.routers import doctor_router, user_router, appointment_router,educator_routes,educator_appointment_routes

app = FastAPI(title="Serving Ninjas API")

# Configure CORS settings
origins = [
    "*"  # allow all origins, or specify your frontend URL(s) here e.g. "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods
    allow_headers=["*"],  # allow all headers
)

# Create tables at startup
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(doctor_router.router)
app.include_router(user_router.router)
app.include_router(appointment_router.router)
app.include_router(educator_routes.router)
app.include_router(educator_appointment_routes.router)