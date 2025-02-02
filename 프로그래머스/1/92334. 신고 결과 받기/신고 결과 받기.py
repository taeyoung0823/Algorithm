def solution(id_list, report, k):
    answer = []  # 최종 결과값을 출력할 리스트
    report_list = []  # k번 이상 신고당한 사람 리스트
    report_count = {}  # 사람별 신고 당한 횟수
    result = 0  # answer에 넣을 수
    report = list(set(report))  # 중복 원소 제거
    
    # report_count 등록
    for r in report:
        reported = r.split()[-1]
        report_count[reported] = report_count.get(reported, 0) + 1  # 신고 당한 횟수 누적

    # report_list 등록
    for key, value in report_count.items():
        if value >= k:
            report_list.append(key)

    # answer 계산
    user_reports = {user: set() for user in id_list}  # 각 사용자가 신고한 사람 집합으로 저장
    for r in report:
        reporter, reported = r.split()
        user_reports[reporter].add(reported)  # 신고한 대상 저장

    for user in id_list:
        result = 0
        for reported in user_reports[user]:
            if reported in report_list:
                result += 1
        answer.append(result)

    return answer
