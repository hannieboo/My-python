def sum_cal(homework, mid, final):
    total = homework + mid + final
    return total

def sort(total):
    if total > 80:
        return "ดีมาก very nice"
    elif 50 < total <= 80:
        return "ผ่าน pass"
    else:
        return "ไม่ผ่าน not pass"

def get_valid_score(prompt, max_score):
    while True:
        score = int(input(prompt))
        if score <= max_score:
            return score
        else:
            print(f"จำนวนคะแนนไม่เกิน {max_score}")

homework = get_valid_score("จำนวนคะแนนเก็บ : ", 20)
mid = get_valid_score("จำนวนคะแนนสอบกลางภาค : ", 40)
final = get_valid_score("จำนวนคะแนนสอบปลายภาค : ", 40)

total_score = sumcal(homework, mid, final)
result = sort(total_score)

print(f"จำนวนคะแนนรวม: {total_score}")
print(f"ผลการประเมิน: {result}")