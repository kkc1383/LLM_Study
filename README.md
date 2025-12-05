# LLM Study

OpenAI GPT API를 활용한 LLM 예제 프로젝트입니다.

## 시스템 요구사항

⚠️ **중요**: 이 프로젝트는 `deepspeed`, `bitsandbytes` 등 Linux 전용 패키지를 사용합니다.

### Windows 사용자
- **WSL (Windows Subsystem for Linux)** 필수
- Python 3.10 또는 3.11 권장 (Python 3.13은 일부 패키지와 호환 문제 있음)

### Mac/Linux 사용자
- Python 3.10 또는 3.11 권장

## WSL 설치 (Windows 사용자)

### 1. WSL 설치

PowerShell을 관리자 권한으로 실행 후:

```powershell
wsl --install
```

설치 완료 후 재부팅합니다.

### 2. Ubuntu 실행 및 사용자 설정

시작 메뉴에서 "Ubuntu"를 실행하고 사용자명과 비밀번호를 설정합니다.

### 3. Python 3.10 설치 (WSL 내부)

```bash
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3-pip build-essential
```

### 4. 프로젝트 디렉토리 접근

Windows 파일 시스템은 `/mnt/c/` 경로로 접근 가능합니다:

```bash
cd /mnt/c/Users/kangk/OneDrive/Desktop/Krafton_jungle/LLM_Study
```

## 설치 및 설정

### 1. 가상환경 생성 및 활성화

#### WSL/Linux/Mac 환경 (권장):

```bash
# 프로젝트 디렉토리로 이동
cd /mnt/c/Users/kangk/OneDrive/Desktop/Krafton_jungle/LLM_Study

# Python 3.10으로 가상환경 생성
python3.10 -m venv my_venv_name

# 가상환경 활성화
source my_venv_name/bin/activate
```

#### Windows (순수 Windows 환경 - 일부 패키지 제외됨):

```bash
# 가상환경 활성화만
my_venv_name\Scripts\activate
```

### 2. pip 및 기본 패키지 업그레이드

```bash
pip install --upgrade pip setuptools wheel
```

### 3. 의존성 설치

가상환경이 활성화된 상태에서 requirements.txt의 패키지들을 설치합니다:

```bash
pip install -r requirements.txt
```

**참고**: WSL 환경에서는 모든 패키지가 설치됩니다. 순수 Windows 환경에서는 `deepspeed`, `bitsandbytes`가 설치되지 않을 수 있습니다.

### 4. 환경 변수 설정

프로젝트를 처음 설정할 때 다음 단계를 따르세요:

1. `.env.example` 파일을 복사하여 `.env` 파일을 생성합니다:
   ```bash
   # WSL/Linux/Mac
   cp .env.example .env

   # Windows (순수 Windows 환경)
   copy .env.example .env
   ```

2. `.env` 파일을 열고 실제 API 키를 입력합니다:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

### 5. OpenAI API 키 발급

1. [OpenAI Platform](https://platform.openai.com/)에 접속
2. 계정 로그인 후 API Keys 섹션으로 이동
3. "Create new secret key" 버튼 클릭
4. 생성된 키를 복사하여 `.env` 파일에 저장

## 보안 주의사항

⚠️ **중요**: `.env` 파일과 가상환경은 절대 Git에 커밋하지 마세요!

- `.env` 파일은 `.gitignore`에 포함되어 있습니다
- `my_venv_name/` 가상환경 디렉토리도 `.gitignore`에 포함되어 있습니다
- 실제 API 키는 `.env` 파일에만 저장하세요
- `.env.example`은 템플릿으로 Git에 포함됩니다 (실제 키 없음)
- API 키가 노출되었다면 즉시 OpenAI 대시보드에서 키를 재발급하세요

## 사용 예제

### Python
```python
import os
from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# API 사용 예제
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### Node.js
```javascript
import 'dotenv/config';
import OpenAI from 'openai';

// OpenAI 클라이언트 초기화
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// API 사용 예제
const response = await openai.chat.completions.create({
  model: "gpt-3.5-turbo",
  messages: [{ role: "user", content: "Hello!" }]
});
console.log(response.choices[0].message.content);
```

## 문제 해결

### Python 버전 호환성 문제
- Python 3.13에서는 일부 패키지가 설치되지 않을 수 있습니다
- **해결책**: Python 3.10 또는 3.11을 사용하세요
- WSL에서 Python 3.10 설치:
  ```bash
  sudo apt install python3.10 python3.10-venv
  ```

### deepspeed, bitsandbytes 설치 실패 (Windows)
- 이 패키지들은 Linux 전용입니다
- **해결책**: WSL을 사용하세요

### numpy, setuptools 관련 에러
- 가상환경의 기본 패키지를 먼저 업그레이드하세요:
  ```bash
  pip install --upgrade pip setuptools wheel
  ```

### API 키 오류
- `.env` 파일이 프로젝트 루트 디렉토리에 있는지 확인
- API 키가 올바르게 입력되었는지 확인
- 키 앞뒤에 공백이나 따옴표가 없는지 확인

### 환경 변수 로드 안됨
- `dotenv` 패키지가 설치되어 있는지 확인
- `load_dotenv()` (Python) 또는 `import 'dotenv/config'` (Node.js)가 코드 최상단에 있는지 확인
