from collections import Counter

# Survey results (แต่ละ List แทนตัวเลือกของผู้ร่วมสำรวจแต่ละคน)
survey_results = [
    ["Python", "JavaScript", "C++"],  # Participant 1
    ["Python", "JavaScript", "C#"],  # Participant 2
    ["Python", "Java"],  # Participant 3
    ["Python", "C++", "JavaScript"],  # Participant 4
    ["Python", "JavaScript", "C++", "Java"],  # Participant 5
]

# แปลงทุก List ให้เป็น Set เพื่อใช้สำหรับการคำนวณเซต
sets_list = [set(participant) for participant in survey_results]
all_choices = [lang for participant in survey_results for lang in participant]
counts = Counter(all_choices)

print("--- ผลลัพธ์การวิเคราะห์แบบสำรวจ ---")

# 1. ภาษาที่ถูกเลือกโดยผู้เข้าร่วมทุกคน (Intersection)
languages_all = set.intersection(*sets_list)
print("1. ภาษาที่เลือกโดยทุกคน:", languages_all)  # Output: {'Python'}

# 2. ภาษาที่ถูกเลือกโดยผู้เข้าร่วมเพียงคนเดียวเท่านั้น
single_choice = {lang for lang, count in counts.items() if count == 1}
print("2. ภาษาที่เลือกโดยคนเดียว:", single_choice)  # Output: {'C#'}

# 3. จำนวนภาษาที่ไม่ซ้ำกันทั้งหมดในแบบสำรวจ
unique_languages = set(all_choices)
print("3. จำนวนภาษาที่ไม่ซ้ำกัน:", len(unique_languages))  # Output: 5

# 4. ภาษาที่ถูกเลือกโดยผู้เข้าร่วม exactement 2 คน
two_choices = {lang for lang, count in counts.items() if count == 2}
print("4. ภาษาที่เลือกโดย 2 คน:", two_choices)  # Output: {'Java'}

# 5. หาผู้เข้าร่วมที่มีชุดภาษาโปรดเหมือนกันทุกประการ
print("5. ผู้เข้าร่วมที่มีชุดภาษาโปรดเหมือนกัน:")
for i in range(len(sets_list)):
  for j in range(i + 1, len(sets_list)):
    if sets_list[i] == sets_list[j]:
      print(f"   - Participant {i+1} และ Participant {j+1}")
      # Output: Participant 1 และ Participant 4