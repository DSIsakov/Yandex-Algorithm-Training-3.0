#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct Elem{
	int num, cost;
} se;


typedef struct Stack{
	se *data;
	int cap, index;
} ss;


void InitElem(se *e, int n, int c){
	e->cost = c;
	e->num = n;
}


void InitStack(ss *s, int n){
	s->cap = n;
	s->index = 0;
	s->data = (se*)calloc(n+1, sizeof(se));
}


int isEmpty(ss* s){
	return s->index == 0;
}


void Push(ss *s, se e){
	s->data[s->index++] = e;
}


se Pop(ss *s){
	return s->data[--s->index];
}


se Back(ss *s){
	return s->data[s->index - 1];
}


void Exit(ss* s){
	free(s->data);
}


int main(){
	ss s;
	int n;
	scanf("%d", &n);
	InitStack(&s, n);
	int *ans = (int*)calloc(n, sizeof(int));
	for (int i = 0; i < n; i++){
		int cost;
		scanf("%d", &cost);
		se cur;
		InitElem(&cur, i, cost);
		while (!isEmpty(&s) && cost < Back(&s).cost){
			se prev = Pop(&s);
			ans[prev.num] = i;
		}
		Push(&s, cur);
	}
	
	while (!isEmpty(&s)){
		se elem = Pop(&s);
		ans[elem.num] = -1;
	}
	printf("%d", ans[0]);
	for (int i = 1; i < n; i++){
		printf(" %d", ans[i]);
	}
	printf("\n");
	
	Exit(&s);
	free(ans);
}