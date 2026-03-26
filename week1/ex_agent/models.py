from pydantic import BaseModel, Field

class UserProfile(BaseModel): 
  age: int = Field(description="사용자의 나이")
  gender: str = Field(description="사용자의 성별 (male | female)")
  height: int = Field(description="사용자의 키 (cm)")
  weight: int = Field(description="사용자의 몸무게 (kg)")
  activity_level: str = Field(description="사용자의 활동 레벨")
  # ---
  bmi: float 
  bmr: float
  tdee: float
  ideal_weight_min: float
  ideal_weight_max: float