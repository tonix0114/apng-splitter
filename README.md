# APNG (Animated Portable Network Graphics)

> "PNG를 확장한 이미지 파일 포맷으로 GIF와 같이 animation을 지원해준다. (24bit image , 8bit transparency)"

- APNG의 __첫번째 프레임__은 기존의 PNG Stream이기 때문에 PNG만 지원할 경우 첫번째 프레임만 보여주게 된다.

- 프레임의 속성값은 extra chunk에 저장되어 있다.

<br>

Signature + IHDR + IDAT(fdAT) + IEND 와 같은 구조로 만들어지며

fdAT를 IDAT로 변경하기 위해서 아래의 조건을 만족시켜야 한다.

1. length -= 4; __// fdAT가 100일 경우 IDAT로 변환할 때 96__

2. fdAT DATA offset += 4; __// 길이를 줄여준만큼 4바이트 뒤에 부터 데이터를 이어줌__

# 사용 방법

fdAT 청크를 찾는데 성공하면 __apng\_split\_{00-99}.png__와 같은 식으로 현재 디렉토리에 PNG 파일이 생성된다.

```
$ python ./apng-splitter.py {apng_file.png}

>> ./apng_split_1.png
   ./apng_split_2.png
        ...
```
