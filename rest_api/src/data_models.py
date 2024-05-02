from pydantic import BaseModel


class TemperatureMeasurement(BaseModel):
    timestamp: float
    temperature: float
