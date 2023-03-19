# CP1_DS AIB 16기

## 과적 및 정상차량 감지
- 과적 차량과 정상 차량을 구분할 수 있는 모델입니다

## How to download?
![image](https://user-images.githubusercontent.com/114691059/226193218-fcce3c4f-e36c-4699-96cf-748bf8e2e59d.png)
- 해당 이미지 초록색박스안 <> CODE를 누르면 해당 이미지와 같은 화면이 나옵니다.
- Download ZIP 혹은 https://로 시작하는 주소를 복사하여 로컬 컴퓨터로 가져옵니다.
- 이후 아래의 Step을 따라 실행해주시기 바랍니다.

## Info
각 폴더에 관한 설명입니다.
- data : 비디오 파일을 넣는곳입니다. 테스트용 sample.mp4라는 영상이 있으며 사용자가 테스트할 데이터를 이곳에 넣습니다.
- test : 직접 테스트할 test.ipynb가 있는 폴더입니다. 이것을 실행시켜 테스트를 진행합니다.
- utils : detect.py가 있는 폴더입니다. test.ipynb의 모듈로 사용됩니다.
- weights : 미리 학습된 모델이 저장되어있는 폴더입니다.
- result : 테스트한 결과가 저장되는 폴더이며, 미리 생성돼있지 않고 테스트가 끝나면 생기고 이곳에 저장됩니다.


## Step 1
- 가상환경을 설정합니다 본 파일은 python 버전 3.8로 제작되었습니다.
- requirements.txt 내 패키지들을 인스톨합니다.

## Step 2
- test폴더 내 test.ipynb를 실행합니다.
- 4개의 셀을 순서대로 실행합니다.
- 사용자가 수정해야할 부분은 아래 이미지의 sample.mp4와 output_sample.mp4입니다.
![image](https://user-images.githubusercontent.com/114691059/226195541-a3037211-ee99-4bb5-a3c5-07cfcccc148b.png)
- sample.mp4를 테스트할 비디오의 파일명으로 수정합니다.
- output_sample.mp4를 원하는 파일명으로 수정합니다.
- 이후 detect.main()셀을 실행합니다

## Step 3
- 모든 과정이 끝나면 탐지가 완료되었습니다 라는 문구가 출력됩니다.
- 결과는 result폴더에 저장되며 재생하여 확인합니다.
