# Allyajyo
![allyajyo introdution image, "Allyajyo, for faster & better CTF quals" in Google Roboto](/images/allyajyo_intro.png)
><strong>Allyajyo, for faster & better CTF quals</br>
더 나은 CTF 문제풀이를 위한 프로그램, "알랴죠(Allyajyo)"</strong>

This file is the README on project Allyajyo</br>
본 파일은 <strong>알랴죠(Allyajyo)</strong> 프로젝트의 깃허브 저장소 루트 위치에 있는 <strong>README.md</strong>입니다.</br></br>
해당 프로젝트는 <strong>MIT License</strong>를 따릅니다.</br><a href="https://github.com/JunhoYeo/Allyajyo/blob/master/LICENSE">LICENSE</a> 파일을 참고해 주십시오.</br>
위 이미지에는 <a href="https://github.com/JunhoYeo/Allyajyo/blob/master/Allyajyo_Logo.png">알랴죠 로고</a> 및 <a href="https://fonts.google.com/specimen/Roboto">Google Roboto</a>가 사용되었습니다.

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

#### Hex viewer
hex viewer 기능으로 파일의 hex data를 쉽게 확인할 수 있습니다.
```
USER@Allyajyo : analyze
file name to analyze : flag.txt
[Offset]      [Hex]                                               [Strings]
0000000000 |  54 68 69 73  20 66 69 6C  65 20 69 73  20 75 73 65  |This file is use
0000000010 |  64 20 69 6E  20 61 6C 6C  79 61 6A 79  6F 20 74 65  |d in allyajyo te
0000000020 |  73 74 69 6E  67 20 3A 29  0D 0A 68 61  5F 68 61 21  |sting :)..ha_ha!
0000000030 |  66 69 6E 64  20 53 6F 6D  33 74 68 69  6E 39 20 69  |find Som3thin9 i
0000000040 |  6E 20 48 33  72 33 21 21  0D 0A 23 40  24 24 2A 26  |n H3r3!!..#@$$*&
```
위 예시처럼 `analyze` 또는 `anal` 명령어를 사용하여 hex viewer를 실행시킬 수 있습니다.</br>
offset과 hex data, 그리고 hex data에 해당되는 string 정보를 한 화면에서 볼 수 있습니다.</br>
hex viewer를 실행해야 Flag-like strings 검색이나 파일 에러 탐색이 가능하여 비효율적이라고 생각할 수 있는데, 이 역시 곧 수정될 예정입니다.

#### Hex data에서 Flag-like strings 검색 (feat. flagDB)
Flag로 의심되는 문자열(Flag-like strings)을 Flag keyword database(FlagDB)에 있는 키워드 항목을 이용하여 검색하고 출력합니다.</br>
사용자는 얄랴죠를 통해 쉽게 새로운 키워드를 추가하고, 제거할 수 있습니다.
```
USER@Allyajyo : add keyword
keyword to add in database : flag
item successfully added to database

USER@Allyajyo : addkey
keyword to add in database : FLAG
item successfully added to database
```
위 예시처럼 `add keyword` 또는 `addkey` 명령어를 사용하여 새로운 키워드를 데이터베이스에 추가할 수 있습니다.</br>
<strong>같은 키워드가 중복 등록될 수 있다는 버그</strong>가 발견되었습니다.</br>
사용에 큰 지장은 없을 것으로 생각되나, 빠른 시일 내 처리가 가능하도록 하겠습니다.

```
USER@Allyajyo : delate keyword
keyword to delate in database : flag
item successfully delated from database

USER@Allyajyo : delkey
keyword to delate in database : FLAG
item successfully delated from database
```
위 예시처럼 `delate keyword` 또는 `delkey` 명령어를 사용하여 이미 데이터베이스에 존재하는 키워드를 삭제할 수 있습니다.</br>
같은 키워드가 중복 등록되었을 경우 중복 등록된 모든 키워드가 삭제됩니다.</br>
해당 버그는 신속히 수정하도로 하겠습니다.

```
<!--detecting for 'flag' flag-like strings-->
        ***!!FLAG-LIKE STRING DISCOVERED!!***
        flag{A1Ly4Jy0_f0R_f4sTer_&_b3tTer_CTF_qu4l5}
<!--detecting for 'FLAG' flag-like strings-->
        ***!!FLAG-LIKE STRING DISCOVERED!!***
        FLAG{W0w~_th1s_1s_Th3_Re4l_Fl49!!}
```
키워드를 등록한 이후 hexviewer를 `analyze` 또는 `anal` 명령으로 실행하면 hex data가 출력된 이후 검색결과가 출력됩니다.

#### JPEG file 에러 자동 수정 (00 FF 00)
SECCON 2017의 'JPEG file' 문제풀이에 사용된 방법과 같이 JPEG 파일 에러를 찾고 자동으로 수정하는 기능을 만들었습니다.</br>
File data 부분에서 00 FF 바이트 이후 반드시 00이 리턴되어야 하는데 그러지 못해 발생하는 파일 에러입니다.</br>
C/C++를 사용해서는 정상적으로 구현이 되었지만 Python 포팅 이후 디버깅에 어려움을 많이 겪었습니다. 지금 해결되었으니 한번 확인해 봅시다!
```
found JPEG structure error! FC is not 0x00 after 0x00 0xFF
data corrected!
```
SECCON CTF 2017의 'JPEG file' 문제 바이너리를 대상으로 `analyze` 또는 `anal` 명령어를 실행하자 위와 같은 메세지가 hex viewer 실행 이후에 나타납니다.</br></br>
![result of allyajyo used in SECCON CTF 2017 ](/images/allyajyo_seccon2017.png)</br></br>
위 그림과 같이 Flag가 보이는 원래 이미지 파일로 정상적으로 복구된 모습을 확인할 수 있었습니다.

#### Binary visualizer
VELES(CodiSec)라는 바이너리 분석 툴에서 영감을 얻은 기능입니다.</br>
쉽게 파일을 분석하기 위해서 바이너리 파일을 그림 파일로 시각화하는 기능을 추가되었습니다.
```
USER@Allyajyo : visualize
file name to visualize : README.md
image successfully visualized and saved as 'visualized_README_md.png'

USER@Allyajyo : visual
file name to visualize : README.md
image successfully visualized and saved as 'visualized_README_md.png'
```
위처럼 `visualize` 또는 `visual` 명령어로 visualizer를 실행할 수 있습니다.</br></br>
![result of visualizing README.md file](/images/visualized_README_md.png)</br></br>
실행 결과는 위와 같습니다.</br>
자세한 설명은 http://nogadaworks.tistory.com/93?category=800460 를 참고해 주시면 될 것 같습니다.

## 개발 예정 및 계획
아직은 개발되지 않았지만, 개발 중이거나 개발할 예정인 알랴죠 기능들입니다.

#### PE viewer
PE viewer 기능을 빠른 시일 내 개발하여 추가하려고 합니다.</br>
Python pefile module을 사용하려고 하고, 물론 해당 module을 설치하지 않은 사람들을 위해서 예외 처리 역시 할 것입니다.

#### Shellcode DB
포너블 등 CTF 문제풀이에 유용하게 사용될 것으로 추정되는 기능으로, 쉘코드를 직접 등록하고 삭제 및 view가 가능하도록 구현할 예정입니다.</br>
태그를 통해 자신의 문제풀이에 필요한 쉘코드를 빠르게 검색할 수 있어서 문제풀이뿐만이 아니라 정보보안 분야의 학습에도 도움이 될 것이라고 생각합니다.

#### Crypto 쉽게 풀기
카이사르 암호나 base64/base32/base16 인코딩 등을 복호화하는 기능을 추가할 생각입니다.</br>
문제에서 가끔 나오는 암호화 역시 쉽게 접근할 수 있도록 md5나 base64/base32/base16 등을 지원할 생각입니다.</br>
esolang(난해한 프로그래밍 언어) 문제가 가끔씩 나오기도 하는데 코드를 입력하면 어떤 esolang인지 알려줘 정보보안 공부를 갓 시작한~~필자 같은~~ 뉴비들도 쉽게 분석이 가능하도록 할 수 있는 기능 역시 만들고 싶습니다.

#### Stego 쉽게 풀기
Stego(스테가노그래피) 문제들 중에는 비교적 간단한 방법으로, 배경색과 구분이 안 되는 색들을 전부 한 색으로 전환하면 Flag가 나오거나, 간단한 효과 몇 개를 적용하면 Flag가 나오는 등의 문제가 가끔 있습니다. 이러한 문제를

#### VBA code password unlock
파워포인트 등 Microsoft office 프로그램들을 사용할 때 advanced한 기능을 위해서 VBA 코드를 사용할 때가 많습니다.</br>
보안을 위해 패스워드를 설정했다가 까먹는~~ㅋㅋㅋㅋㅋ~~ 일이 많은데, 구글링을 통해 언락이 간단하다는 것을 알게 되었고 이를 지원하도록 개발할 생각이 있습니다.

#### CTF webpage 크롤링
CTF가 시작되는 시간에 웹페이지를 크롤링하면서 문제풀이에 필요한 파일과 문제들을 미리 다운로드받고, 마이크테스트 등의 간단한 문제들은 인증까지 해 줄 수 있는 모습을 상상하면서 기획했습니다.

#### GUI Development
PyQT나 Tkinter 등으로 GUI 역시 개발할 계획입니다.</br>
아래 Contributors에서도 확인이 가능하지만, <a href="https://github.com/Devonnuri"><strong>@Devonnuri(뎁온누리)</strong></a> 님께서 개발하신 <a href="https://github.com/Devonnuri/Allyajyo-GUI"><strong>Allyajyo-GUI</strong></a> 프로젝트 이미 존재합니다.

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

- <a href="https://github.com/HyungJu"><strong>@HyungJu(HyungJu)</strong></a> : <a href="https://github.com/JunhoYeo/Allyajyo/issues/1">First Issue</a> (mistyped message)

- <a href="https://github.com/Devonnuri"><strong>@Devonnuri(뎁온누리)</strong></a> : 알랴죠에서 파생된 프로젝트 <a href="https://github.com/Devonnuri/Allyajyo-GUI">Allyajyo-GUI</a> 개발
