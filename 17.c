#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct Queue{
	int *data;
	int cap, head, tail, count;
} sq;


void Init(sq *q, int n){
	q->cap = n;
	q->count = 0;
	q->head = 0;
	q->tail = 0;
	q->data = (int*)calloc(n+1, sizeof(int));
}


int isEmpty(sq* q){
	return q->count == 0;
}


void push(sq *q, int x){
	q->count++;
	q->data[q->tail++] = x;
	if (q->tail == q->cap){
		q->tail = 0;
	}
}


int pop(sq *q){
	q->count--;
	if (q->head == q->cap - 1){
		q->head = 0;
		return q->data[q->cap - 1];
	}
	return q->data[q->head++];
}


int front(sq* q){
	return q->data[q->head];
}


int size(sq* q){
	return q->count;
}


void clear(sq* q){
	q->count = 0;
	q->head = 0;
	q->tail = 0;
}


void freedata(sq* q){
	free(q->data);
}


int main(){
	sq first, second;
	Init(&first, 20);
	Init(&second, 20);
	char *str1 = (char*)calloc(20, sizeof(char));
	char *str2 = (char*)calloc(20, sizeof(char));
	fgets(str1, 20, stdin);
	fgets(str2, 20, stdin);
	for (int i = 0; i < 9; i+=2){
		push(&first, (int)str1[i] - (int)'0');
		push(&second, (int)str2[i] - (int)'0');
	}
	free(str1);
	free(str2);
	int moves = 0;
	while (moves <= 1000000 && !isEmpty(&first) && !isEmpty(&second)){
		int a = pop(&first);
		int b = pop(&second);
		if (a > b){
			if (a == 9 && b == 0){
				push(&second, a);
				push(&second, b);
			}
			else{
				push(&first, a);
				push(&first, b);
			}
		}
		else {
			if (a == 0 && b == 9){
				push(&first, a);
				push(&first, b);
			}
			else{
				push(&second, a);
				push(&second, b);
			}
		}
		moves++;
	}
	
	if (moves > 1000000){
		printf("botva\n");
	}
	else if (!isEmpty(&first)){
		printf("first %d\n", moves);
	}
	else{
		printf("second %d\n", moves);
	}
	
	freedata(&first);
	freedata(&second);
}