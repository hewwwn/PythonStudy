grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

num_sum = 0
total = 0

for i in range(20):
    a = list(map(str, input().strip().split()))
    sum = float(a[1])
    if a[2] == "P":
        continue
    else:
        idx = grade_list.index(a[2])
        score = score_list[idx]
        total += (sum*score)
        num_sum += sum
        
f_score = float(total / num_sum)
print(f_score)