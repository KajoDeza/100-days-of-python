student_scores = [98, 86, 34, 65, 76, 24, 10, 89, 67, 100]

#total_exam_score = sum(student_scores)

#sum = 0
#for score in student_scores:
    #sum += score

#print(sum)

#print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score


print(max_score)