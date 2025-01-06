def solution(participant, completion):
    part_dict = {}
    for name in participant:
        if name in part_dict:
            part_dict[name] += 1
        else:
            part_dict[name] = 1

    for name in completion:
        if name in part_dict:
            part_dict[name] -= 1

    for key, value in part_dict.items():
        if value == 1:
            return key
