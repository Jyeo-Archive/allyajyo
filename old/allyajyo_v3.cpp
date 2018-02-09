//allyajyo_v3.cpp

#include <stdio.h> //stdio.h ��������
#include <stdlib.h> //stdlib.h ��������
#include <stdbool.h> //stdbool.h ��������
#include <windows.h> //windows.h ��������
#define BUFFER_SIZE 16
int *file_data;
int file_data_index=0; //index of file_data ����, �ʱ�ȭ
void setcolor(int text_color, int background_color){ //���󺯰�
    text_color &= 0xf; //text ��
    background_color &= 0xf; //background ��
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), (background_color<<4) | text_color);
}
void viewHexCode(){
	setcolor(14, 5);
    printf("[Offset]");
	for(int i=0; i<13-8+1; i++) printf(" ");
	setcolor(10, 5);
	printf("[Hex]");
	for(int i=0; i<(BUFFER_SIZE-1)*3+2; i++) printf(" ");
	setcolor(15, 5);
	printf("[Strings]\n");
	setcolor(10, 5);
	int file_data_length;
	if(file_data_index%BUFFER_SIZE==0) file_data_length=file_data_index/BUFFER_SIZE;
	else file_data_length=(file_data_index/BUFFER_SIZE)+1;
	int offset=0, read=0;
	for(int i=0; i<file_data_length; i++){ //file_data_length�� �����ؾ� �� line�� ��
	    //������ ����**************************************************
	    setcolor(14, 5);
        printf("%.10X | ", offset); //BUFFER_SIZE�� hex�� ���Ͽ��� �о� 1�ٿ� ������. offset=������
        setcolor(10, 5);
		//�� ����ŭ �ݺ��Ѵ�
		int n=0; //�ش� �ٿ��� �� ��° hex���ΰ� is n
	    int counter=0; //����
		for(int j=read; j<read+BUFFER_SIZE; j++){ //BUFFER_SIZE���� �о���
		    if(j==file_data_index) break; //������ ���� �ٴٸ��� break;
			if(n%4==0 || n==0){
        		printf(" ");
        		counter++;
			}
			printf("%.2X ", file_data[j]);
			if(n==BUFFER_SIZE-1){
            	printf(" ");
            	counter++;
			}
			n++;
		}
		offset+=n;
		//����ó��**************************************************
        if((BUFFER_SIZE*3+1*5)-(n*3+counter*1)>0){
        	for(int j=0; j<(BUFFER_SIZE*3+1*5)-(n*3+counter*1)-1; j++) printf(" ");
		    //"| " ���ڿ��� 2����Ʈ, �ϳ��� ���� �����Ϳ� ������ 3����Ʈ ����
            printf(" ");
		}
        //string ����**************************************************
		setcolor(15, 5);
        printf("| ");
        for (int j=read; j<read+(int)BUFFER_SIZE; j++) { //text strings ����
            if(file_data[j]>=0x20 && file_data[j]<=0x7E) printf("%c", file_data[j]);
            else printf(".");
        }
        setcolor(10, 5);
        read+=n;
		printf("\n");
	}
}
int main(){
	setcolor(10, 5); //���������濡 �ʷϱ۾�
	system("cls"); //ȭ���ʱ�ȭ
    FILE *file=NULL; //���������� ����
    char file_name[100]; //���� �̸�/���� <=��������ó�� ������
    printf("file name to analyze : ");
    scanf("%s", &file_name); //�м��� ���� �̸�/���� �Է¹���
    file=fopen(file_name,"rb"); //���� ����
    if(file==NULL) return -1; //���� ó��
    fseek(file, 0, SEEK_END);
    int file_size = ftell(file); //filesize�� ����
	rewind(file); //���������� rewind
	file_data=(int*)malloc(sizeof(int)*file_size); //file_data �迭�� ����, filesize ũ�⸸ŭ �����Ҵ�
    for(int i=0; i<file_size; i++) file_data[i]=0; //�迭 �ʱ�ȭ
    char buffer[BUFFER_SIZE]={0};
    //�� ���ھ� int������ �������κ��� �Է¹޾� file_data�� ����
    for(int read=0; (read=fread(&buffer, sizeof(char), BUFFER_SIZE, file))!=0;){ //���� �̺κ� �޸��� �� �� ���Ը԰� �����Ұ�
    	for(int i=0; i<read; i++){
            file_data[file_data_index]=buffer[i]&0xFF;
            file_data_index++;
        }
	}
	viewHexCode();
    fclose(file); //close file
	char keyword[15]="flag";
	for(int i=0; i<file_data_index; i++){
		int flag=0, weight=0, startpoint;
		for(int j=0; j<strlen(keyword); j++){
			if(j==0) startpoint=i;
			if(file_data[i+weight]!=keyword[j]) break;
			weight++;
			if(j==strlen(keyword)-1) flag=1;
		}
		if(flag!=0){
			setcolor(12, 0);
	    	printf("***!!FLAG-LIKE STRING DISCOVERED!!***");
	    	setcolor(10, 5);
	    	printf(" \n");
	    	setcolor(0, 7);
		    for(int j=startpoint; true; j++){
		    	if(!(file_data[j]>=0x20 && file_data[j]<=0x7E)) break; //'.'�� ���� ������ ���� ����
		    	else if(file_data[j]=='{' || file_data[j]=='}' || file_data[j]=='_'){ //�߰�ȣ�� ������ ������ �÷���
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
	for(int i=32; i<file_data_index; i++){
		if(file_data[i]==0x00 && file_data[i+1]==0xFF && file_data[i+2]!=0x00){
			setcolor(12, 0);
		    printf("found JPEG structure error! 0x%.2X is not 0x00 after 0x00 0xFF", file_data[i+2]);
		    setcolor(10, 5);
		    printf("\n");
		    file=fopen(file_name,"wb"); //���� ����
            if(file==NULL) return -1; //���� ó��
            file_data[i+2]=0x00;
            for(int j=0; j<file_data_index; j++){
            	//printf("offset: %.10X / file_data: %.2X\n", offset, file_data[j]);
            	fprintf(file, "%c", file_data[j]);
			}
			fclose(file);
			setcolor(0, 14);
		    printf("data corrected!", file_data[i+2]);
		    setcolor(10, 5);
		    printf("\n");
		}
	}
	//printf("file_data_index is %.10X\n", file_data_index);
	free(file_data);
	system("pause");
	return 0;
    //flag{W3_4R3_TH3_D3vC0_C0d3r5}
}
