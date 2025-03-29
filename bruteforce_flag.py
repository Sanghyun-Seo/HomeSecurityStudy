
import subprocess
import string
import itertools

# 입력 문자 조합 (대문자 + 숫자)
charset = string.ascii_uppercase + string.digits

# 조합 길이 (예시: 8자리, 필요 시 늘릴 수 있음)
length = 8

print(f"[*] Trying all {length}-length combinations from charset ({len(charset)} chars)...")

for candidate in itertools.product(charset, repeat=length):
    test_input = ''.join(candidate)
    try:
        result = subprocess.run(
            ['./prob'],
            input=test_input + '\n',
            capture_output=True,
            text=True,
            timeout=1
        )
        output = result.stdout + result.stderr
        if "FLAG" in output or "codegate" in output:
            print("🎉 Found input:", test_input)
            print("=== Program Output ===")
            print(output)
            break
    except subprocess.TimeoutExpired:
        continue
