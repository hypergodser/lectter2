def generate_primes(limit):
    primes = []
    
    # วนลูปตรวจสอบจำนวนตั้งแต่ 2 จนถึง limit - 1
    for num in range(2, limit):
        is_prime = True
        # ตรวจสอบว่ามีเลขใดหารลงตัวหรือไม่
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
            
    # นำรายการจำนวนเฉพาะมาเชื่อมกันด้วย ", " ตามรูปแบบ Output
    return ", ".join(primes)

# --- Example usage ---
print(generate_primes(10))  # Output: "2, 3, 5, 7"
print(generate_primes(20))  # Output: "2, 3, 5, 7, 11, 13, 17, 19"
print(generate_primes(1))   # Output: ""
print(generate_primes(2))   # Output: "2"