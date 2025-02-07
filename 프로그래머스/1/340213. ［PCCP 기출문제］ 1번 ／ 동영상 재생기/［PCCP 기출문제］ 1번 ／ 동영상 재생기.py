def skip_op(now_min, now_sec, start_min, start_sec, end_min, end_sec):
    """광고 구간을 건너뛰는 함수"""
    if (now_min > start_min or (now_min == start_min and now_sec >= start_sec)) and \
       (now_min < end_min or (now_min == end_min and now_sec < end_sec)):
        now_min, now_sec = end_min, end_sec  # 광고 끝나는 지점으로 이동
    return now_min, now_sec

def solution(video_len, pos, op_start, op_end, commands):
    # 시간 정보 변환
    video_min, video_sec = map(int, video_len.split(':'))
    now_min, now_sec = map(int, pos.split(':'))
    start_min, start_sec = map(int, op_start.split(':'))
    end_min, end_sec = map(int, op_end.split(':'))

    # 광고 구간 체크 (초기 위치에서 광고 구간 안에 있다면 skip)
    now_min, now_sec = skip_op(now_min, now_sec, start_min, start_sec, end_min, end_sec)

    # 명령어 처리
    for cmd in commands:
        if cmd == "prev":
            if now_min == 0 and now_sec <= 10:
                now_sec = 0
            else:
                now_sec -= 10
                if now_sec < 0:
                    now_min -= 1
                    now_sec += 60  # 음수가 되는 걸 방지

        elif cmd == "next":
            if now_min == video_min and now_sec >= video_sec - 10:
                now_sec = video_sec
            else:
                now_sec += 10
                if now_sec >= 60:
                    now_min += 1
                    now_sec -= 60  # 60초를 넘으면 1분 증가
                if now_min>=video_min and now_sec>=video_sec:
                    now_min = video_min
                    now_sec = video_sec
    
        # 광고 구간 체크 (명령어 수행 후)
        now_min, now_sec = skip_op(now_min, now_sec, start_min, start_sec, end_min, end_sec)
    
    # 최종 시간 반환
    return f"{str(now_min).zfill(2)}:{str(now_sec).zfill(2)}"
