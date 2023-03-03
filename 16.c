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
	sq queue;
	Init(&queue, 100000000);
	while (1){
		char query[6];
		scanf("%s", query);
		if (strcmp(query, "push") == 0){
			int x;
			scanf("%d", &x);
			push(&queue, x);
			printf("ok\n");
		}
		else if (strcmp(query, "pop") == 0) {
			if (!isEmpty(&queue)){
				printf("%d\n", pop(&queue));
			}
			else {
				printf("error\n");
			}
		}
		else if (strcmp(query, "front") == 0) {
			if (!isEmpty(&queue)){
				printf("%d\n", front(&queue));
			}
			else {
				printf("error\n");
			}
		}
		else if (strcmp(query, "size") == 0) {
			printf("%d\n", size(&queue));
		}
		else if (strcmp(query, "clear") == 0) {
			clear(&queue);
			printf("ok\n");
		}
		else if (strcmp(query, "exit") == 0) {
			freedata(&queue);
			printf("bye\n");
			break;
		}
	}
}