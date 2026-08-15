from pydantic import BaseModel, Field


class RepositoryAnalysis(BaseModel):
    overview: str
    architecture: str
    technologies: list[str]
    important_files: list[str]
    issues: list[str]
    security_concerns: list[str]
    recommendations: list[str]
    score: int = Field(ge=0, le=100)
def create_analysis_model(model):
    return model.with_structured_output(RepositoryAnalysis)    