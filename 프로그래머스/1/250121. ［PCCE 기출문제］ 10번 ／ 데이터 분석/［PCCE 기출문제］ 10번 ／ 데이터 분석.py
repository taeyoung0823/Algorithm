def solution(data, ext, val_ext, sort_by):
    answer = []

    columns = ["code", "date", "maximum", "remain"]

    ext_idx = columns.index(ext)
    sort_idx = columns.index(sort_by)
    
    
    for row in data:
        if row[ext_idx] < val_ext:  
            answer.append(row)

    answer.sort(key=lambda x: x[sort_idx])

    return answer
