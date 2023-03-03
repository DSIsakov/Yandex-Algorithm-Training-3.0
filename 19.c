#include <stdio.h>
#include <stdlib.h>
#define parent (index-1) / 2
#define left index * 2 + 1
#define right index * 2 + 2


typedef struct Heap {
	int* data;
	int cap, count;
} sh;


void Init(sh* h, int n){
	h->cap = n;
	h->count = 0;
	h->data = (int*)calloc(n+1, sizeof(int));
}


void insert(sh* h, int x){
	int index = h->count++;
	h->data[index] = x;
	while (index > 0 && h->data[index] > h->data[parent]){
		int temp = h->data[index];
		h->data[index] = h->data[parent];
		h->data[parent] = temp;
		index = (index - 1) / 2;
	}
}


int extract(sh* h){
	int ans = h->data[0], temp, index = 0;
	h->data[0] = h->data[--h->count];
	while (left < h->count){
		if (right < h->count){
			if (h->data[index] > h->data[left] && h->data[index] > h->data[right]){
				break;
			}
			if (h->data[left] > h->data[right]){
				temp = h->data[left];
				h->data[left] = h->data[index];
				h->data[index] = temp;
				index = left;
			}
			else{
				temp = h->data[right];
				h->data[right] = h->data[index];
				h->data[index] = temp;
				index = right;
			}
		}
		else{
			if (h->data[index] > h->data[left]){
				break;
			}
			temp = h->data[left];
			h->data[left] = h->data[index];
			h->data[index] = temp;
			index = left;
		}
	}
	
	return ans;
}


int main(){
	int n;
	sh heap;
	scanf("%d", &n);
	Init(&heap, n);
	for (int i = 0; i < n; i++){
		int cmd;
		scanf("%d", &cmd);
		if (cmd == 0){
			int x;
			scanf("%d", &x);
			insert(&heap, x);
		}
		else {
			printf("%d\n", extract(&heap));
		}
	}
	
	free(heap.data);
}