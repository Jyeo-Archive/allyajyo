#include <stdio.h> //stdio.h 헤더파일  
#include <stdlib.h> //stdlib.h 헤더파일  
#include <stdbool.h> //stdbool.h 헤더파일  
#include <windows.h> //windows.h 헤더파일   
#define BUFFER_SIZE 16 //Hex viewer에서 한 줄에 출력할 Hex code의 수  
void setcolor(int text_color, int background_color){ //색상변경 
	text_color &= 0xf; //text 색 
	background_color &= 0xf; //background 색  
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), (background_color<<4) | text_color);
}
char* GetFileExtenstion(char *file_name){ //파일 확장자를 구하는 함수  
	int file_name_length=strlen(file_name);
    file_name+=file_name_length;
    char *file_extenstion;
    for(int i=0; i<file_name_length; i++){
        if(*file_name=='.'){
            file_extenstion=file_name+1;
            break;
        }
        file_name--;
    }
    return file_extenstion;
}

class hexViewer{ //Hex viewer 클래스 (저는 분명히 혼종이라고 했습니다) 
private:
	char *filename; //파일 이름/경로 
	int *file_data; //파일 데이터  
	int file_data_index; //index of file_data 선언, 초기화  
public:
	void openFile(char *_file_name);
	void viewCode();
	void findFlag();
	void correctJpegData(); //
	void freeMemory(); //메모리 해제 함수  
};
void hexViewer::openFile(char *_file_name){
	FILE *file=NULL; //파일포인터 선언  
	filename=_file_name;
	file=fopen(filename,"rb"); //파일 열기  
	if(file==NULL) exit(1); //에러 처리  
	fseek(file, 0, SEEK_END); 
	int file_size = ftell(file); //filesize를 구함 
	rewind(file); //파일포인터 rewind  
	file_data=(int*)malloc(sizeof(int)*file_size); //file_data 배열을 생성, filesize 크기만큼 동적할당
	file_data_index=0; 
	for(int i=0; i<file_size; i++) file_data[i]=0; //배열 초기화  
	char buffer[BUFFER_SIZE]={0};
	//한 문자씩 int형으로 파일으로부터 입력받아 file_data에 저장  
	for(int read=0; (read=fread(&buffer, sizeof(char), BUFFER_SIZE, file))!=0;){ //언제 이부분 메모리 좀 더 적게먹게 수정할것 
		for(int i=0; i<read; i++){
			file_data[file_data_index]=buffer[i]&0xFF;
			file_data_index++;
		}
	}
	fclose(file); //close file  
}
void hexViewer::viewCode(){ 
	setcolor(14, 5);
    printf("[Offset]");
	for(int i=0; i<6; i++) printf(" "); //적절한 공백 추가 
	setcolor(10, 5);
	printf("[Hex]");
	for(int i=0; i<(BUFFER_SIZE-1)*3+2; i++) printf(" "); //적절한 공백 추가 
	setcolor(15, 5); 
	printf("[Strings]\n"); //적절한 공백 추가 
	setcolor(10, 5);
	int file_data_length;
	if(file_data_index%BUFFER_SIZE==0) file_data_length=file_data_index/BUFFER_SIZE;
	else file_data_length=(file_data_index/BUFFER_SIZE)+1;
	int offset=0, read=0;
	for(int i=0; i<file_data_length; i++){ //file_data_length는 출력해야 할 line의 수  
	    //오프셋 출력**************************************************  
	    setcolor(14, 5); 
        printf("%.10X | ", offset); //BUFFER_SIZE개 hex씩 파일에서 읽어 1줄에 출력함. offset=오프셋 
        setcolor(10, 5);
		//줄 수만큼 반복한다  
		int n=0; //해당 줄에서 몇 번째 hex값인가 is n 
	    int counter=0; //공백 
		for(int j=read; j<read+BUFFER_SIZE; j++){ //BUFFER_SIZE개씩 읽어옴  
		    if(j==file_data_index) break; //파일의 끝에 다다르면 break; 
		    //Hex data 4개 출력할 때마다 한 칸씩 더 공백을 넣어줘서 이쁘게 해줌  
			if(n%4==0 || n==0){ 
        		printf(" ");
        		counter++;
			}  
			printf("%.2X ", file_data[j]); //2자리로 Hex data 출력  
			if(n==BUFFER_SIZE-1){
            	printf(" ");
            	counter++;
			}
			n++;
		} 
		offset+=n;
		//공백처리**************************************************  
        if((BUFFER_SIZE*3+5)-(n*3+counter)>0){
        	for(int j=0; j<(BUFFER_SIZE*3+5)-(n*3+counter)-1; j++) printf(" ");
		    //"| " 문자열은 2바이트, 하나의 헥스 데이터와 공백은 3바이트 차지 
            printf(" ");
		}
        //string 출력**************************************************  
		setcolor(15, 5);  
        printf("| ");
        for (int j=read; j<read+(int)BUFFER_SIZE; j++) { //text strings 출력 
            if(file_data[j]>=0x20 && file_data[j]<=0x7E) printf("%c", file_data[j]);
            else printf(".");
        }
        setcolor(10, 5);
        read+=n;
		printf("\n");
	}
}
void hexViewer::findFlag(){
	//키워드가 저장된 파일에서부터 입력받아 strstr() 등으로 검색하는 구조로 수정해야 하는데 
	//귀찮으니 그냥 그건 파이썬으로 구현해버리는걸루~  
	char keyword[15]="flag";
	for(int i=0; i<file_data_index; i++){
		int flag=0, weight=0, startpoint; 
		for(int j=0; j<strlen(keyword); j++){
			if(j==0) startpoint=i;
			if(file_data[i+weight]!=keyword[j]) break;
			weight++;
			if(j==strlen(keyword)-1) flag=1;
		}
		if(flag!=0){ //Flag-like string이 발견되면  
			setcolor(12, 0);
			printf("***!!FLAG-LIKE STRING DISCOVERED!!***"); //안내 메세지 출력  
			setcolor(10, 5);
			printf(" \n");
			setcolor(0, 7);
			for(int j=startpoint; true; j++){
				if(!(file_data[j]>=0x20 && file_data[j]<=0x7E)) break; //'.'이 나올 때까지 내용 출력  
				else if(file_data[j]=='{' || file_data[j]=='}' || file_data[j]=='_'){ //중괄호나 언더바 나오면 컬러링  
					setcolor(0, 14);
					printf("%c", file_data[j]);
					setcolor(0, 7);
				}
				else{
					printf("%c", file_data[j]);
				}
			} 
			setcolor(10, 5); 
			printf(" \n");
		}
	}
}
void hexViewer::correctJpegData(){
	for(int i=32; i<file_data_index; i++){
		if(file_data[i]==0x00 && file_data[i+1]==0xFF && file_data[i+2]!=0x00){
			setcolor(12, 0);
		    printf("found JPEG structure error! 0x%.2X is not 0x00 after 0x00 0xFF", file_data[i+2]);
		    setcolor(10, 5);
		    printf("\n");
		    FILE *file=NULL; //파일포인터 선언  
		    file=fopen(filename,"wb"); //파일 열기  
            if(file==NULL) exit(1); //에러 처리  
            file_data[i+2]=0x00;
            for(int j=0; j<file_data_index; j++){
            	fprintf(file, "%c", file_data[j]);
			}
			fclose(file);
			setcolor(0, 14);
		    printf("data corrected!", file_data[i+2]);
		    setcolor(10, 5);
		    printf("\n");
		}
	}
}
void hexViewer::freeMemory(){
	free(file_data); //동적할당한 file_data 메모리 해제  
}

int main(){ //main 함수  
	setcolor(10, 5); //보라색배경에 초록글씨  
	system("cls"); //화면 초기화  
	char file_name[100]; //파일 이름/경로 <=에러방지처리 수정좀  
	printf("file name to analyze : "); 
	scanf("%s", &file_name); //분석할 파일 이름/경로 입력받음  
	hexViewer hexviewer; //hexViewer 클래스 객제 hexviewer 생성  
	hexviewer.openFile(file_name); //file_name의 파일 열기  
	//hexviewer.viewCode(); //Hex data 출력  
	hexviewer.findFlag(); //파일의 바이너리에서 Flag 검색  
	if(strcmp(GetFileExtenstion(file_name), "jpeg")==0){ //파일 확장자가 jpeg인 경우 
		hexviewer.correctJpegData(); //jpeg 파일 에러가 있는지 확인하고 있으면 수정 후 저장 
	}
	hexviewer.freeMemory();
	system("pause"); 
	return 0; //프로그램 종료  
}
