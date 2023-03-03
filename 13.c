#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct Stack{
	int *data;
	int cap, index;
} ss;


void Init(ss *s, int n){
	s->cap = n;
	s->index = 0;
	s->data = (int*)calloc(n+1, sizeof(int));
}


int isEmpty(ss* s){
	return s->index == 0;
}


void Push(ss *s, int x){
	s->data[s->index++] = x;
}


int Pop(ss *s){
	return s->data[--s->index];
}


void Exit(ss* s){
	free(s->data);
}


int main(){
	ss s;
	Init(&s, 10000001);
	char *str = (char*)calloc(10000001, sizeof(char));
	fgets(str, 100000001, stdin);
	for (int i = 0; i < strlen(str); i += 2){
		if (str[i] == '+'){
			int b = Pop(&s);
			int a = Pop(&s);
			Push(&s, a + b);
		}
		else if (str[i] == '-') {
			int b = Pop(&s);
			int a = Pop(&s);
			Push(&s, a - b);
		}
		else if (str[i] == '*') {
			int b = Pop(&s);
			int a = Pop(&s);
			Push(&s, a * b);
		}
		else {
			Push(&s, (int)str[i] - (int)'0');
		}
	}
	printf("%d\n", Pop(&s));
	
	Exit(&s);
}