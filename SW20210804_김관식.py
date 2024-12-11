import random
import string

def generate_students(n=30):
    """ 무작위 학생 정보 생성 """
    students = []
    for _ in range(n):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬 구현
def selection_sort(data, key, reverse=False):
    n = len(data)
    for i in range(n):
        min_max_idx = i
        for j in range(i + 1, n):
            if (data[j][key] < data[min_max_idx][key]) ^ reverse:
                min_max_idx = j
        data[i], data[min_max_idx] = data[min_max_idx], data[i]

# 삽입 정렬 구현
def insertion_sort(data, key, reverse=False):
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and ((data[j][key] > current[key]) ^ reverse):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current

# 퀵 정렬 구현
def quick_sort(data, key, reverse=False):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = [x for x in data[1:] if (x[key] < pivot[key]) ^ reverse]
    greater = [x for x in data[1:] if (x[key] >= pivot[key]) ^ reverse]
    return quick_sort(less, key, reverse) + [pivot] + quick_sort(greater, key, reverse)

# 기수 정렬 (성적 기준)
def radix_sort(data, key):
    max_score = 100  # 점수 범위: 0~100
    exp = 1
    while max_score // exp > 0:
        buckets = [[] for _ in range(10)]
        for student in data:
            index = (student[key] // exp) % 10
            buckets[index].append(student)
        data.clear()
        for bucket in buckets:
            data.extend(bucket)
        exp *= 10

# 학생 정보 출력 함수
def display_students(students):
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

# 입력값 검증 함수
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        print("잘못된 입력입니다. 다시 시도해주세요.")

# 메인 함수
def main():
    students = generate_students()
    print("\n생성된 학생 정보:")
    display_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        choice = get_valid_input("정렬 기준을 선택하세요 (1, 2, 3, 4): ", ["1", "2", "3", "4"])

        if choice == '4':
            print("프로그램을 종료합니다.")
            break

        print("\n정렬 알고리즘을 선택하세요:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 전용)")
        algo_choice = get_valid_input("알고리즘 선택 (1, 2, 3, 4): ", ["1", "2", "3", "4"])

        reverse = get_valid_input("정렬 방식을 선택하세요 (오름차순: 0, 내림차순: 1): ", ["0", "1"]) == '1'

        if choice == '1':
            key = '이름'
        elif choice == '2':
            key = '나이'
        elif choice == '3':
            key = '성적'
        else:
            print("잘못된 입력입니다.")
            continue

        # 정렬 알고리즘 실행
        if algo_choice == '1':
            selection_sort(students, key, reverse)
        elif algo_choice == '2':
            insertion_sort(students, key, reverse)
        elif algo_choice == '3':
            students = quick_sort(students, key, reverse)
        elif algo_choice == '4' and key == '성적':
            radix_sort(students, key)
            if reverse:
                students.reverse()
        else:
            print("잘못된 알고리즘 선택이거나 성적 외의 필드에서 기수 정렬은 사용할 수 없습니다.")
            continue

        print("\n정렬된 결과:")
        display_students(students)

if __name__ == "__main__":
    main()
