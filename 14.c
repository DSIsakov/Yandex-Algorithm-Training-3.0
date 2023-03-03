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


int Back(ss *s){
	return s->data[s->index - 1];
}


void Exit(ss* s){
	free(s->data);
}


int main(){
	int n, cur = 1;
	ss s;
	scanf("%d", &n);
	Init(&s, n);
	for (int i = 0; i < n; i++){
		int tr;
		scanf("%d", &tr);
		Push(&s, tr);
		while (!isEmpty(&s) && Back(&s) == cur){
			Pop(&s);
			cur++;
		}
	}
	if (isEmpty(&s)) {
		printf("YES\n");
	}
	else {
		printf("NO\n");
	}
	Exit(&s);
}