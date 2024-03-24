# LeetCode GraphQL API

## questionTitle

### Query
```
questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    isPaidOnly
    difficulty
    likes
    dislikes
    categoryTitle
  }
}
```
### Variables
```
{
  "titleSlug": "divide-two-integers"
}
```
### Response
```
{
  "data": {
    "question": {
      "questionId": "29",
      "questionFrontendId": "29",
      "title": "Divide Two Integers",
      "titleSlug": "divide-two-integers",
      "isPaidOnly": false,
      "difficulty": "Medium",
      "likes": 4965,
      "dislikes": 14691,
      "categoryTitle": "Algorithms"
    }
  }
}
```

## questionContent

### Query
```
query questionContent($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    content
    mysqlSchemas
    dataSchemas
  }
} 
```
### Variables
```
{
  "titleSlug": "divide-two-integers"
}
```
### Response
```
{
  "data": {
    "question": {
      "content": "<p>Given two integers <code>dividend</code> and <code>divisor</code>, divide two integers <strong>without</strong> using multiplication, division, and mod operator.</p>\n\n<p>The integer division should truncate toward zero, which means losing its fractional part. For example, <code>8.345</code> would be truncated to <code>8</code>, and <code>-2.7335</code> would be truncated to <code>-2</code>.</p>\n\n<p>Return <em>the <strong>quotient</strong> after dividing </em><code>dividend</code><em> by </em><code>divisor</code>.</p>\n\n<p><strong>Note: </strong>Assume we are dealing with an environment that could only store integers within the <strong>32-bit</strong> signed integer range: <code>[&minus;2<sup>31</sup>, 2<sup>31</sup> &minus; 1]</code>. For this problem, if the quotient is <strong>strictly greater than</strong> <code>2<sup>31</sup> - 1</code>, then return <code>2<sup>31</sup> - 1</code>, and if the quotient is <strong>strictly less than</strong> <code>-2<sup>31</sup></code>, then return <code>-2<sup>31</sup></code>.</p>\n\n<p>&nbsp;</p>\n<p><strong class=\"example\">Example 1:</strong></p>\n\n<pre>\n<strong>Input:</strong> dividend = 10, divisor = 3\n<strong>Output:</strong> 3\n<strong>Explanation:</strong> 10/3 = 3.33333.. which is truncated to 3.\n</pre>\n\n<p><strong class=\"example\">Example 2:</strong></p>\n\n<pre>\n<strong>Input:</strong> dividend = 7, divisor = -3\n<strong>Output:</strong> -2\n<strong>Explanation:</strong> 7/-3 = -2.33333.. which is truncated to -2.\n</pre>\n\n<p>&nbsp;</p>\n<p><strong>Constraints:</strong></p>\n\n<ul>\n\t<li><code>-2<sup>31</sup> &lt;= dividend, divisor &lt;= 2<sup>31</sup> - 1</code></li>\n\t<li><code>divisor != 0</code></li>\n</ul>\n",
      "mysqlSchemas": [],
      "dataSchemas": []
    }
  }
}
```

## languageList

### Query
```
query languageList {
  languageList {
    id
    name
  }
}

```
### Variables
```
{}
```
### Response
```
{
  "languageList": [
    {
      "id": 0,
      "name": "cpp"
    },
    {
      "id": 1,
      "name": "java"
    },
    {
      "id": 2,
      "name": "python"
    },
    {
      "id": 11,
      "name": "python3"
    },
    {
      "id": 3,
      "name": "mysql"
    },
    {
      "id": 14,
      "name": "mssql"
    },
    {
      "id": 15,
      "name": "oraclesql"
    },
    {
      "id": 4,
      "name": "c"
    },
    {
      "id": 5,
      "name": "csharp"
    },
    {
      "id": 6,
      "name": "javascript"
    },
    {
      "id": 20,
      "name": "typescript"
    },
    {
      "id": 8,
      "name": "bash"
    },
    {
      "id": 19,
      "name": "php"
    },
    {
      "id": 9,
      "name": "swift"
    },
    {
      "id": 13,
      "name": "kotlin"
    },
    {
      "id": 24,
      "name": "dart"
    },
    {
      "id": 10,
      "name": "golang"
    },
    {
      "id": 7,
      "name": "ruby"
    },
    {
      "id": 12,
      "name": "scala"
    },
    {
      "id": 16,
      "name": "html"
    },
    {
      "id": 17,
      "name": "pythonml"
    },
    {
      "id": 18,
      "name": "rust"
    },
    {
      "id": 21,
      "name": "racket"
    },
    {
      "id": 22,
      "name": "erlang"
    },
    {
      "id": 23,
      "name": "elixir"
    },
    {
      "id": 25,
      "name": "pythondata"
    },
    {
      "id": 26,
      "name": "react"
    },
    {
      "id": 27,
      "name": "vanillajs"
    },
    {
      "id": 28,
      "name": "postgresql"
    }
  ]
}
```

## syncedCode

### Query
```
query syncedCode($questionId: Int!, $lang: Int!) {
  syncedCode(questionId: $questionId, lang: $lang) {
    timestamp
    code
  }
}
```
### Variables
```
{
  "lang": 11,
  "questionId": 29
}
```
### Response
```
{
  "syncedCode": {
    "timestamp": 1682099748,
    "code": "class Solution:\n    def divide(self, dividend: int, divisor: int) -> int:\n\n            "
  }
}
```

## consolePanelConfig

### Query
```
query consolePanelConfig($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    questionTitle
    enableDebugger
    enableRunCode
    enableSubmit
    enableTestMode
    exampleTestcaseList
    metaData
  }
}
```
### Variables
```
{
  "titleSlug": "divide-two-integers"
}
```
### Response
```
{
  "question": {
    "questionId": "29",
    "questionFrontendId": "29",
    "questionTitle": "Divide Two Integers",
    "enableDebugger": true,
    "enableRunCode": true,
    "enableSubmit": true,
    "enableTestMode": false,
    "exampleTestcaseList": [
      "10\n3",
      "7\n-3"
    ],
    "metaData": "{\r\n  \"name\": \"divide\",\r\n  \"params\": [\r\n    {\r\n      \"name\": \"dividend\",\r\n      \"type\": \"integer\"\r\n    },\r\n    {\r\n      \"name\": \"divisor\",\r\n      \"type\": \"integer\"\r\n    }\r\n  ],\r\n  \"return\": {\r\n    \"type\": \"integer\"\r\n  }\r\n}"
  }
}
```
