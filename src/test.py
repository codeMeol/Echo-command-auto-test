import pandas as pd
import subprocess

# 엑셀 파일 읽기
excel_file = 'path/to/your/excel_file.xlsx'
df = pd.read_excel(excel_file)

# 각 행에 대해 커맨드 실행
for index, row in df.iterrows():
    # 예시로 첫 번째 열의 데이터를 커맨드로 사용
    command = f'echo {row[0]}'
    print(f'Running command: {command}')
    
    # 커맨드 실행
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # 결과 출력
    print(result.stdout)

# 주의: 실제 환경에서는 커맨드 실행 결과를 잘 처리해야 하며,
# 보안상 shell=True를 사용하는 것을 지양할 수도 있습니다.
