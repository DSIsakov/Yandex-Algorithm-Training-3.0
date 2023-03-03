#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct Deque{
	int *data;
	int cap, head, tail, count;
} sd;


void Init(sd *d, int n){
	d->cap = n;
	d->count = 0;
	d->head = 0;
	d->tail = 0;
	d->data = (int*)calloc(n+1, sizeof(int));
}


int isEmpty(sd* d){
	return d->count == 0;
}


void push_back(sd *d, int x){
	d->count++;
	d->data[d->tail++] = x;
	if (d->tail == d->cap){
		d->tail = 0;
	}
}


void push_front(sd *d, int x){
	d->count++;
	if (d->head == 0){
		d->head = d->cap;
	}
	d->data[--d->head] = x;
}


int pop_front(sd *d){
	d->count--;
	if (d->head == d->cap - 1){
		d->head = 0;
		return d->data[d->cap - 1];
	}
	return d->data[d->head++];
}


int pop_back(sd *d){
	d->count--;
	if (d->tail == 0){
		d->tail = d->cap;
	}
	return d->data[--d->tail];
}


int front(sd* d){
	return d->data[d->head];
}


int back(sd *d){
	if (d->tail == 0){
		return d->data[d->cap - 1];
	}
	return d->data[d->tail-1];
}


int size(sd* d){
	return d->count;
}


void clear(sd* d){
	d->count = 0;
	d->head = 0;
	d->tail = 0;
}


void freedata(sd* d){
	free(d->data);
}


int main(){
	sd deque;
	Init(&deque, 100);
	while (1){
		char query[12];
		scanf("%s", query);
		if (strcmp(query, "push_front") == 0){
			int x;
			scanf("%d", &x);
			push_front(&deque, x);
			printf("ok\n");
		}
		else if (strcmp(query, "push_back") == 0){
			int x;
			scanf("%d", &x);
			push_back(&deque, x);
			printf("ok\n");
		}
		else if (strcmp(query, "pop_front") == 0) {
			if (!isEmpty(&deque)){
				printf("%d\n", pop_front(&deque));
			}
			else {
				printf("error\n");
			}
		}
		else if (strcmp(query, "pop_back") == 0) {
			if (!isEmpty(&deque)){
				printf("%d\n", pop_back(&deque));
			}
			else {
				printf("error\n");
			}
		}
		else if (strcmp(query, "front") == 0) {
			if (!isEmpty(&deque)){
				printf("%d\n", front(&deque));
			}
			else {
				printf("error\n");
			}
		}
		else if (strcmp(query, "back") == 0) {
			if (!isEmpty(&deque)){
				printf("%d\n", back(&deque));
			}
			else {
				printf("error\n");
			}
		}
		else if (strcmp(query, "size") == 0) {
			printf("%d\n", size(&deque));
		}
		else if (strcmp(query, "clear") == 0) {
			clear(&deque);
			printf("ok\n");
		}
		else if (strcmp(query, "exit") == 0) {
			freedata(&deque);
			printf("bye\n");
			break;
		}
	}
}