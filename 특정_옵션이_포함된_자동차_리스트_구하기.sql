-- 동차들의 정보
-- CAR_RENTAL_COMPANY_CAR
-- CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트
-- 자동차 종류(CAR_TYPE)는 '세단', 'SUV', '승합차', '트럭', '리무진'
-- 자동차 옵션 리스트(OPTIONS)는 콤마(',')로 구분된 키워드 리스트 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트'

-- '네비게이션' 옵션이 포함된 자동차 리스트를 출력하는 SQL, 자동차 ID를 기준으로 내림차순 정렬

select * from CAR_RENTAL_COMPANY_CAR where options like '%네비게이션%' order by car_id desc