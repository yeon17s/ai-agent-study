"""
건강 운동 코치 에이전트가 사용할 도구 목록
"""

from langchain_core.tools import tool
from models import UserProfile
# from typing import Dict

@tool
def caculate_body_metrics(
  age: int, 
  gender: str,
  height: int, 
  weight: int,
  activity_level: str,
) -> UserProfile :  # ) -> Dict:
  """신체 정보를 저장하고, BMI, BMR, TDEE 지수를 계산해서 반환합니다.

  Args:
    age: 나이
    gender: 성별 ("male" | "female")
    height: 키 (cm)
    weight: 몸무게 (kg)
    activity_level: 활동 레벨 (0 | 1 | 2 | 3 | 4)

  Returns: 
    UserProfile: BMI, BMR, TDEE 지수를 포함한 신체 정보 모델
  """

  bmi = weight / (height / 100) ** 2

  if gender.lower() == 'male':
    bmr = (10 * weight) + (6.25 + height) - (5 * age) + 5
  else:
    bmr = (10 * weight) + (6.25 + height) - (5 * age) - 161
  
  activity_multiplier = {
    "": 1.2
  }
  tdee = bmr * activity_multiplier.get(activity_level, 1.55)

  ideal_min = round(18.5 * (height / 100) ** 2, 1)
  ideal_max = round(23.0 * (height / 100) ** 2, 1)

  profile = UserProfile(
    age=age,
    gender=gender,
    height=height,
    weight=weight,
    activity_level=activity_level,
    bmi=bmi,
    bmr=bmr,
    tdee=tdee,
    ideal_weight_min=ideal_min,
    ideal_weight_max=ideal_max
  )

  # 개인화
  # DB -> 영속화
  store = get_store()
  store['profile'].append(profile)

  