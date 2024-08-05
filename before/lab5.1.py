def score(n):
    
    sum_score = 0
    
    for i in range(n):
        score = int(input(f"รับคะแนนนักศึกษาคนที่ {i+1}:"))
        sum_score += score
        
        avgscore = sum_score/n
    return avgscore

n = int(input("จำนวนนักศึกษา : "))
average = score(n)
print(f"คะแนนเฉลี่ยของนักศึกษา {n} คน คือ {average}")