from datetime import datetime, timedelta

token_max_age = datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
safelist = ['없음', '맑음'] # 해당 리스트 시에는 초록색 표시
middleList = ['흐림'] # 해당 리스트 시에는 주황색 표시
dangerTemp = 30 # 해당 온도 이상 빨간색 표시



