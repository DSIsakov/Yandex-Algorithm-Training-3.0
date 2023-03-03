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
	printf("ok\n");
}


void Pop(ss *s){
	if (isEmpty(s)){
		printf("error\n");
	}
	else{
		printf("%d\n", s->data[--s->index]);
	}
}


void Back(ss *s){
	if (isEmpty(s)){
		printf("error\n");
	}
	else{
		printf("%d\n", s->data[s->index - 1]);
	}
}


void Size(ss* s){
	printf("%d\n", s->index);
}


void Clear(ss *s){
	s->index = 0;
	printf("ok\n");
}


void Exit(ss* s){
	free(s->data);
	printf("bye\n");
}


int main(){
	ss s;
	Init(&s, 10000000);
	while (1) {
		char q[6] = "";
		scanf("%s", q);
		if (strcmp(q, "push") == 0){
			int x;
			scanf("%d", &x);
			Push(&s, x);
		}
		else if (strcmp(q, "pop") == 0) {
			Pop(&s);
		}
		else if (strcmp(q, "back") == 0) {
			Back(&s);
		}
		else if (strcmp(q, "size") == 0) {
			Size(&s);
		}
		else if (strcmp(q, "clear") == 0) {
			Clear(&s);
		}
		else if (strcmp(q, "exit") == 0){
			Exit(&s);
			break;
		}
	}
}