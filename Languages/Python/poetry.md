Python의 **Poetry**는 Python 프로젝트의 **패키지 관리**와 **의존성 관리**를 위한 도구입니다. 기존의 `pip` 및 `virtualenv`와 같은 도구를 대체하거나 보완하는 역할을 합니다. Poetry는 Python 프로젝트를 더 쉽게 설정하고 관리할 수 있도록 설계되었으며, 특히 의존성 충돌 문제를 해결하거나, 환경을 재현 가능하게 만드는 데 도움을 줍니다.

### 주요 특징
1. **의존성 관리**:
    - Poetry는 프로젝트에서 필요한 패키지(의존성)를 선언하고 설치할 수 있습니다.
    - `pyproject.toml` 파일을 사용하여 의존성을 명시합니다.
    - 의존성 충돌을 방지하고, 잠금 파일(`poetry.lock`)을 생성하여 환경을 재현 가능하게 만듭니다.

2. **가상 환경 관리**:
    - Poetry는 프로젝트별로 가상 환경을 자동으로 생성하고 관리합니다.
    - 별도로 `virtualenv`를 설정할 필요가 없습니다.

3. **패키지 배포**:
    - Poetry는 프로젝트를 Python 패키지로 쉽게 빌드하고 배포할 수 있는 기능을 제공합니다.
    - PyPI(Python Package Index)에 배포하는 과정을 단순화합니다.

4. **사용자 친화적인 CLI**:
    - Poetry는 직관적이고 간단한 명령어를 제공합니다.
    - 예: 패키지 추가, 업데이트, 제거, 의존성 검사 등이 간단합니다.

---

### Poetry 설치
Poetry는 Python 패키지가 아니라 독립 실행형 도구로 설치됩니다. 설치 방법은 다음과 같습니다:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

설치가 완료되면, Poetry 명령어를 사용할 수 있습니다.

---

### 주요 명령어
1. **프로젝트 생성**:
   ```bash
   poetry new my_project
   ```
    - 새로운 Python 프로젝트 디렉토리를 생성합니다.

2. **의존성 추가**:
   ```bash
   poetry add requests
   ```
    - `requests` 패키지를 프로젝트에 추가합니다.

3. **개발 의존성 추가**:
   ```bash
   poetry add --dev pytest
   ```
    - 개발 환경에서만 필요한 의존성을 추가합니다.

4. **의존성 설치**:
   ```bash
   poetry install
   ```
    - `pyproject.toml` 및 `poetry.lock` 파일에 명시된 모든 의존성을 설치합니다.

5. **가상 환경 실행**:
   ```bash
   poetry shell
   ```
    - Poetry가 생성한 가상 환경으로 진입합니다.

6. **패키지 배포**:
   ```bash
   poetry publish
   ```
    - PyPI에 패키지를 배포합니다.

---

### pyproject.toml
Poetry는 의존성을 관리하기 위해 `pyproject.toml` 파일을 사용합니다. 이 파일은 프로젝트의 메타데이터(이름, 버전, 설명 등)와 의존성을 정의합니다.

예시:
```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "A sample project"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.26.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.5"
```

---

### Poetry의 장점
1. **일관된 환경**:
    - 잠금 파일을 통해 모든 개발자가 동일한 환경에서 작업할 수 있습니다.
2. **편리한 의존성 관리**:
    - 의존성 추가, 제거, 업데이트가 간단합니다.
3. **가상 환경 통합**:
    - 별도의 도구 없이 가상 환경을 자동으로 관리합니다.
4. **배포 간소화**:
    - PyPI 배포가 쉬워집니다.

---

### 기억해두면 좋은 영어 표현
- **Dependency management**: 의존성 관리
- **Virtual environment**: 가상 환경
- **Reproducible environment**: 재현 가능한 환경
- **Package distribution**: 패키지 배포

---

### 질문을 영어로 표현하면?
"Python 포에트리란 뭐야?"는 영어로 이렇게 표현할 수 있습니다:
- "What is Python Poetry?"
- "Can you explain what Poetry is in Python?"