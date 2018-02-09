# Allyajyo
Allyajyo, the tool for fast-solving CTF problems</br>
빠른 CTF 문제풀이 및 파일 분석을 위한 프로그램 "알랴죠(Allyajyo)"</br></br>
This file is README.md on project Allyajyo</br>
본 파일은 알랴죠(Allyajyo) 프로젝트의 깃허브 저장소 루트 위치에 있는 README.md입니다.</br></br>
해당 프로젝트는 <strong>MIT License</strong>를 따릅니다.</br><a href="https://github.com/JunhoYeo/Allyajyo/blob/master/LICENSE">LICENSE</a> 파일을 참고해 주십시오.

## Github repository
https://github.com/JunhoYeo/Allyajyo

## Naming  
```
뭐든지 다 알려주니까 알랴죠일 뿐, 더 이상의 의미는 없다...
```

## What is CTF?
CTF는 Capture The Flag의 약자로 주어지는 파일, 프로그램, 웹페이지 등을 분석하여 Flag라는 정답 문자열(String)을 찾아 인증하여 점수를 얻는 정보보안 해킹방어대회입니다.

## What is Allyajyo?

- 단순한 인코딩의 Crypto나 간단한 Stego 문제  

- 웹페이지 어딘가에 있는 Flag를 찾아내는 보물찾기  

- 덤프나 로그 파일에서 Flag를 찾아내는 형식의 포렌식 문제

위와 같은 문제에 시간이 많이 소요되는 경우가 많은데, 알랴죠를 이용하면 빠르게 풀 수 있습니다.</br>
웹페이지를 자동으로 크롤링하여 정보를 가져오고 필요한 파일들을 미리 다운로드하고 문제 데이터를 정리하는 기능 역시 개발 중에 있습니다.</br>
알랴죠를 사용하면 CTF 문제풀이에 걸리는 시간을 효과적으로 단축할 수 있을 것이고, 대회 종료 후 WriteUp(문제풀이 보고서) 역시 쉽게 작성이 가능할 것입니다.

## Allyajyo Features
이전 버전의 알랴죠의 경우 구현이 완벽하지 않은 경우가 있으므로 최신 버전의 얄랴죠 기준으로 기술합니다.</br>

- 파일의 Hex data에서 Flag로 의심되는 문자열을 출력(flag keyword database로 keyword 저장, 사용자가 관리 가능)

- SECCON 2017 'JPEG file' 문제풀이에 사용된 방법과 같이 JPEG 파일 에러를 찾고 자동으로 수정하는 기능(Python으로 포팅하면서 error 발생하여 디버깅 중)

- VBA 코드가 패스워드로 잠금되어 있는 PPSM 파일의 경우 자동 언락 해제(보류됨)

- 포너블 문제풀이에 활용이 가능한 shellcode database 추가 예정(개발 중)

- CTF webpage 크롤링(개발예정)

## Development
사용 언어(Used Programming Language):

- ~version 4 : C/C++ (Compiler: TDM-GCC 4.9.2 / IDE: Dev-C++)

- ~version 5 : Python 2.7 (Text Editor: Atom)

- after version 6 : Python 3.6.4 (Text Editor: Atom) ~~갓아톰~~

### Why use Python?
객체지향 언어(효율성, 코드 가독성) + 다양한 라이브러리 지원</br>
문법이 간단하여 C/C++ 보다 효율적인 프로그래밍이 가능

### For now...
점점 언어 특징을 잘 활용하고 기능 역시 추가할 예정입니다.</br>
+인터페이스 역시 사용자 친화적으로 개발 중</br>
(GUI 시스템의 경우 PyQT 고려중)

## Contributors
얄랴죠 프로젝트에 기여해 주셔서 감사합니다.</br>

- <strong>@HyungJu(HyungJu)</strong> : <a href="https://github.com/JunhoYeo/Allyajyo/issues/1">First Issue</a> (mistyped message)

- <strong>@Devonnuri(뎁온누리)</strong> : 알랴죠에서 파생된 프로젝트 <a href="https://github.com/Devonnuri">Allyajyo-GUI</a> 개발
