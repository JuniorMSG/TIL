# Model Context Protocol (MCP) 개요

Model Context Protocol(MCP)은 AI 모델과 외부 데이터 소스 및 도구 간의 원활한 통합을 가능하게 하는 오픈 프로토콜입니다. 2024년 11월 Anthropic에서 처음 소개된 이 프로토콜은 AI 애플리케이션이 외부 시스템과 표준화된 방식으로 통신할 수 있게 해줍니다. [3]

## MCP의 주요 특징

MCP는 다음과 같은 핵심 기능을 제공합니다:

1. **표준화된 통신** - AI 모델이 다양한 도구와 상호 작용할 수 있는 구조화된 방법을 제공합니다. [6]
2. **클라이언트-서버 아키텍처** - AI 모델이 외부 도구와 효율적으로 상호 작용할 수 있게 합니다. [6]
3. **리소스, 프롬프트, 도구** - 서버는 클라이언트에게 컨텍스트 데이터, 템플릿화된 메시지, 그리고 AI 모델이 실행할 수 있는 함수를 제공합니다. [2]

## MCP 아키텍처 구성 요소

MCP는 다음과 같은 주요 구성 요소로 이루어져 있습니다:

- **호스트(Host)**: 연결을 시작하는 LLM 애플리케이션
- **클라이언트(Client)**: 호스트 애플리케이션 내의 커넥터
- **서버(Server)**: 컨텍스트와 기능을 제공하는 서비스 [2]

## MCP의 작동 방식

MCP는 다음과 같은 흐름으로 작동합니다:

1. AI 모델(호스트)이 요청을 보냅니다(예: "사용자 프로필 데이터 가져오기").
2. MCP 클라이언트가 요청을 적절한 MCP 서버로 전달합니다.
3. MCP 서버가 데이터베이스나 API에서 필요한 데이터를 검색합니다.
4. 응답이 MCP 클라이언트를 통해 AI 모델로 다시 전송됩니다. [6]

## 샘플 코드

다음은 MCP를 사용하는 기본적인 예제 코드입니다:

```typescript
// MCP 클라이언트 설정
import { McpClient } from '@anthropic/mcp-client';

// 클라이언트 초기화
const client = new McpClient({
  baseUrl: 'https://api.example.com/mcp',
  headers: {
    'Authorization': `Bearer ${API_KEY}`
  }
});

// 서버에 연결
async function connectToServer() {
  try {
    // 서버에 연결 요청
    const connection = await client.connect({
      serverUri: 'mcp://example-server',
      capabilities: {
        resources: true,
        tools: true
      }
    });
    
    return connection;
  } catch (error) {
    console.error('MCP 서버 연결 실패:', error);
    throw error;
  }
}

// 리소스 요청 예제
async function fetchUserData(connection, userId) {
  try {
    const response = await connection.getResource({
      resourceId: `user/${userId}`,
      parameters: {
        includeProfile: true,
        includePreferences: true
      }
    });
    
    return response.data;
  } catch (error) {
    console.error('사용자 데이터 가져오기 실패:', error);
    throw error;
  }
}

// 도구 실행 예제
async function executeSearchTool(connection, query) {
  try {
    const result = await connection.executeTool({
      toolId: 'search',
      parameters: {
        query: query,
        maxResults: 5
      }
    });
    
    return result.data;
  } catch (error) {
    console.error('검색 도구 실행 실패:', error);
    throw error;
  }
}
```

## 실행 결과 예시

다음은 위 코드를 실행했을 때의 예상 결과입니다:

```javascript
// 서버 연결 결과
{
  "status": "connected",
  "serverInfo": {
    "name": "Example MCP Server",
    "version": "1.0.0",
    "capabilities": {
      "resources": ["user", "document", "settings"],
      "tools": ["search", "translate", "summarize"]
    }
  }
}

// 사용자 데이터 가져오기 결과
{
  "resourceType": "user",
  "id": "user123",
  "profile": {
    "name": "John Doe",
    "email": "john@example.com",
    "role": "admin"
  },
  "preferences": {
    "theme": "dark",
    "language": "ko",
    "notifications": true
  }
}

// 검색 도구 실행 결과
{
  "toolId": "search",
  "results": [
    {
      "title": "MCP 시작하기",
      "url": "https://docs.example.com/mcp/getting-started",
      "snippet": "Model Context Protocol을 사용하여 AI 애플리케이션 구축하기..."
    },
    {
      "title": "MCP 통합 가이드",
      "url": "https://docs.example.com/mcp/integration",
      "snippet": "외부 시스템과 MCP 연결하기..."
    }
    // 추가 결과...
  ],
  "metadata": {
    "totalResults": 42,
    "executionTime": "120ms"
  }
}
```

## MCP의 이점

MCP는 다음과 같은 주요 이점을 제공합니다:

1. **실시간 데이터 가져오기** - AI 어시스턴트가 API, 데이터베이스 및 내부 시스템에서 최신 정보를 검색할 수 있습니다. [6]
2. **컨텍스트 기반 AI 응답** - 정확하고 최신 정보를 제공하여 AI 응답을 향상시킵니다. [6]
3. **표준화된 통합** - 다양한 데이터 소스와 도구에 대한 커스텀 통합을 구축할 필요성을 줄입니다. [7]
4. **보안 및 확장성** - 기업 애플리케이션에 적합한 안전하고 확장 가능한 통합을 제공합니다. [6]






## 주요 보안 취약점

### 1. 임의 데이터 액세스 및 코드 실행 경로

MCP는 임의 데이터 액세스와 코드 실행 경로를 통해 강력한 기능을 제공합니다. 이러한 강력한 기능은 중요한 보안 및 신뢰 고려사항을 수반하며, 모든 구현자가 신중하게 대응해야 합니다. [2]

### 2. 사용자 동의 및 데이터 프라이버시 문제

MCP 구현 시 다음과 같은 주요 원칙을 고려해야 합니다:
- 사용자는 모든 데이터 액세스 및 작업에 명시적으로 동의하고 이해해야 함
- 사용자는 어떤 데이터가 공유되고 어떤 작업이 수행되는지에 대한 통제권을 유지해야 함
- 구현자는 활동을 검토하고 승인하기 위한 명확한 UI를 제공해야 함 [2]

### 3. 외부 시스템 연결로 인한 보안 위험

MCP는 AI 모델이 외부 시스템과 통신할 수 있게 해주는데, 이는 다음과 같은 보안 위험을 초래할 수 있습니다:
- 인증 정보 노출 위험
- 권한 관리 문제
- 데이터 유출 가능성
- 악의적인 서버와의 연결 위험 [6]

### 4. 권한 관리 및 접근 제어 문제

MCP 구현 시 다음과 같은 접근 제어 문제가 발생할 수 있습니다:
- 과도한 권한 부여
- 세분화된 접근 제어의 부재
- 권한 검증 메커니즘 부족
- 사용자별 권한 구분의 어려움 [7]

## 보안 강화를 위한 권장 사항

MCP 구현 시 보안을 강화하기 위한 몇 가지 권장 사항은 다음과 같습니다:

1. **엄격한 인증 및 권한 부여**: 모든 MCP 연결에 강력한 인증 메커니즘을 구현하고, 최소 권한 원칙을 적용합니다.

2. **데이터 암호화**: 전송 중인 데이터와 저장된 데이터 모두에 대해 강력한 암호화를 적용합니다.

3. **감사 및 로깅**: 모든 MCP 작업에 대한 포괄적인 로깅 및 감사 메커니즘을 구현합니다.

4. **사용자 동의 UI**: 사용자가 데이터 액세스 및 작업을 명확하게 이해하고 승인할 수 있는 인터페이스를 제공합니다.

5. **서버 검증**: MCP 서버의 신뢰성을 검증하는 메커니즘을 구현합니다. [2] [6]

## 보안 구현 코드 예시

다음은 MCP 구현 시 보안을 강화하기 위한 코드 예시입니다:

```typescript
// 보안이 강화된 MCP 클라이언트 설정
import { McpClient } from '@anthropic/mcp-client';
import { createHmac } from 'crypto';

// 안전한 인증 처리
function generateSecureToken(apiKey, timestamp) {
  const hmac = createHmac('sha256', SECRET_KEY);
  hmac.update(`${apiKey}:${timestamp}`);
  return hmac.digest('hex');
}

// 보안이 강화된 클라이언트 초기화
const client = new McpClient({
  baseUrl: 'https://api.example.com/mcp',
  headers: {
    'Authorization': `Bearer ${API_KEY}`,
    'X-Request-Timestamp': Date.now().toString(),
    'X-Auth-Token': generateSecureToken(API_KEY, Date.now().toString())
  },
  // TLS 설정 강화
  tls: {
    minVersion: 'TLSv1.2',
    ciphers: 'HIGH:!aNULL:!MD5:!RC4'
  }
});

// 사용자 동의 확인 함수
async function verifyUserConsent(action, resourceId) {
  // 사용자에게 동의 요청 UI 표시
  const userConsent = await showConsentDialog({
    action: action,
    resource: resourceId,
    permissions: ['read', 'write'],
    purpose: 'AI 모델이 귀하의 데이터에 접근하여 질문에 답변하기 위함입니다.'
  });
  
  if (!userConsent.granted) {
    throw new Error('사용자가 동의를 거부했습니다.');
  }
  
  // 동의 로그 기록
  await logConsentRecord({
    userId: currentUser.id,
    action: action,
    resource: resourceId,
    timestamp: new Date(),
    consentId: userConsent.id
  });
  
  return userConsent;
}

// 안전한 서버 연결
async function connectToServerSecurely() {
  try {
    // 서버 인증서 검증
    await validateServerCertificate('mcp://example-server');
    
    // 서버에 연결 요청 (권한 제한)
    const connection = await client.connect({
      serverUri: 'mcp://example-server',
      capabilities: {
        resources: true,
        tools: {
          // 특정 도구만 허용
          allowlist: ['search', 'summarize'],
          // 위험한 도구 명시적 차단
          blocklist: ['executeCode', 'modifySystem', 'sendEmail']
        }
      },
      // 타임아웃 설정
      timeout: 5000
    });
    
    // 연결 감사 로그
    await logConnection({
      serverUri: 'mcp://example-server',
      timestamp: new Date(),
      clientId: client.id
    });
    
    return connection;
  } catch (error) {
    console.error('MCP 서버 연결 실패:', error);
    throw error;
  }
}

// 안전한 리소스 요청
async function fetchUserDataSecurely(connection, userId) {
  // 사용자 동의 확인
  await verifyUserConsent('read', `user/${userId}`);
  
  try {
    // 요청 범위 제한
    const response = await connection.getResource({
      resourceId: `user/${userId}`,
      parameters: {
        includeProfile: true,
        // 민감한 정보 제외
        includeSensitiveData: false,
        // 특정 필드만 요청
        fields: ['name', 'email', 'preferences']
      }
    });
    
    // 응답 검증
    validateResourceResponse(response);
    
    // 액세스 로깅
    await logResourceAccess({
      resourceId: `user/${userId}`,
      timestamp: new Date(),
      action: 'read'
    });
    
    return response.data;
  } catch (error) {
    console.error('사용자 데이터 가져오기 실패:', error);
    throw error;
  }
}
```




## 기억해두면 좋은 영어 표현

- "Standardized communication protocol" - 표준화된 통신 프로토콜
- "Client-server architecture" - 클라이언트-서버 아키텍처
- "Seamless integration between AI models and external tools" - AI 모델과 외부 도구 간의 원활한 통합
- "Real-time data fetching" - 실시간 데이터 가져오기

- "Arbitrary data access and code execution paths" - 임의 데이터 액세스 및 코드 실행 경로
- "User consent and control" - 사용자 동의 및 통제
- "Principle of least privilege" - 최소 권한 원칙
- "Data privacy considerations" - 데이터 프라이버시 고려사항
- "Security vulnerability mitigation" - 보안 취약점 완화
## 영어로 질문하기

한글: "Model Context Protocol을 사용하여 외부 데이터베이스와 AI 모델을 연결하는 방법이 궁금합니다."
영어: "I'm curious about how to connect an external database with an AI model using the Model Context Protocol."

한글: "MCP의 보안 기능과 사용자 데이터 보호 방법에 대해 알고 싶습니다."
영어: "I'd like to know about MCP's security features and how it protects user data."

한글: "MCP 구현 시 어떤 보안 모범 사례를 따라야 하나요?"
영어: "What security best practices should I follow when implementing MCP?"

한글: "MCP에서 사용자 데이터 접근 권한을 어떻게 제한할 수 있나요?"
영어: "How can I restrict access permissions to user data in MCP?"


