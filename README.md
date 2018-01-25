# Allyajyo
개발중인 해킹툴 "알랴죠(Allyajyo)" CTF 문제 풀이를 쉽고 빠르게!

## Naming  
```
뭐든지 다 알려주니까 알랴죠일 뿐, 더 이상의 의미는 없다...
```

## What is CTF?
CTF는 Capture The Flag의 약자로 주어지는 파일, 프로그램, 웹페이지 등을 분석하여 Flag라는 정답 문자열(String)을 찾아 인증하여 점수를 얻는 정보보안 해킹방어대회입니다.

## What is Allyajyo?
<ul>
  
- 단순한 인코딩의 Crypto나 간단한 Stego 문제  
  
- 웹페이지 어딘가에 있는 Flag를 찾아내는 보물찾기  

- 덤프나 로그 파일에서 Flag를 찾아내는 형식의 포렌식 문제
</ul>
위와 같은 문제에 시간이 많이 소요되는 경우가 많은데, 알랴죠를 이용하면 빠르게 풀 수 있습니다.</br>
웹페이지를 자동으로 크롤링하여 정보를 가져오고 필요한 파일들을 미리 다운로드하고 문제 데이터를 정리하는 기능 역시 개발 중에 있습니다.</br>
알랴죠를 사용하면 CTF 문제풀이에 걸리는 시간을 효과적으로 단축할 수 있을 것이고, 대회 종료 후 WriteUp(문제풀이 보고서) 역시 쉽게 작성이 가능할 것입니다.

## Allyajyo Features
1) 파일의 내용 및 헥스코드를 분석하여 Flag로 의심되는 문자열(Flag-like strings)들을 찾습니다.
- version 5에서 Flag-like string 출력 안되는 문제 디버깅중

2) SECCON 2017 문제(jpeg 파일 데이터 복구)  
- version 5에서의 정상동작여부 테스트 안됨

3) ~~decode Caesar Cipher~~ 디버깅중  
C언어로는 구현에 성공하였으나 Python으로 제작성하는 과정에서 오류가 발생

4) ~~decode base16/base32/base64~~ 개발중

## Development
사용 언어(Used Programming Language):
<ul>
  
- until version 4 : C/C++ (Compiler: TDM-GCC 4.9.2 / IDE: Dev-C++)
  
- after version 5 : Python 2.7 (Text Editor: Atom)
</ul>

### Why use Python?
객체지향 언어(효율성, 코드 가독성) + 다양한 라이브러리 지원</br>
문법이 간단하여 C/C++ 보다 효율적인 프로그래밍이 가능

### For now...
일단은 이전 버젼 C/C++ 코드를 Python으로 구현하고 있는 단계</br>
점점 언어 특징을 잘 활용하고 기능 역시 추가할 예정</br>
+인터페이스 역시 사용자 친화적으로 개발 중</br>
Website crawling feature in development
