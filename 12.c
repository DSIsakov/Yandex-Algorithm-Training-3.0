#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Stack{
	char *data;
	int cap, index;
} ss;


void Init(ss *s, int n){
	s->cap = n;
	s->index = 0;
	s->data = (char*)calloc(n+1, sizeof(char));
}


int isEmpty(ss* s){
	return s->index == 0;
}


void Push(ss *s, char x){
	s->data[s->index++] = x;
}


char Pop(ss *s){
	return s->data[--s->index];
}


void Exit(ss* s){
	free(s->data);
}


int main(){
	char *str = (char*)calloc(100001, sizeof(char));
	scanf("%s", str);
	ss s;
	Init(&s, 100001);
	for (int i = 0; i < strlen(str); i++){
		if (str[i] == '{' || str[i] == '[' || str[i] == '('){
			Push(&s, str[i]);
		}
		else if (str[i] == '}') {
			char c = Pop(&s);
			if (c != '{'){
				printf("no\n");
				free(s.data);
				free(str);
				return 0;
			}
		}
		else if (str[i] == ']') {
			char c = Pop(&s);
			if (c != '['){
				printf("no\n");
				free(s.data);
				free(str);
				return 0;
			}
		}
		else if (str[i] == ')') {
			char c = Pop(&s);
			if (c != '('){
				printf("no\n");
				free(s.data);
				free(str);
				return 0;
			}
		}
	}
	if (s.index == 0) {
		printf("yes\n");
	}
	else {
		printf("no\n");
	}
	free(s.data);
	free(str);
}