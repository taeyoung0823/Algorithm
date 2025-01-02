def solution(players, callings):
    name_to_rank = {name: i + 1 for i, name in enumerate(players)}
    rank_to_name = {i + 1: name for i, name in enumerate(players)}

    for call in callings:
        current_rank = name_to_rank[call]
        new_rank = current_rank - 1

        if new_rank in rank_to_name:
            other_name = rank_to_name[new_rank]
            name_to_rank[call] = new_rank
            name_to_rank[other_name] = current_rank
            rank_to_name[new_rank] = call
            rank_to_name[current_rank] = other_name

    answer = [rank_to_name[i] for i in sorted(rank_to_name)]
    return answer
