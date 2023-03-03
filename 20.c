#include <stdio.h>
#include <stdlib.h>


void heapify(int i, int n, int *data){
	while (1){
		int l = 2 * i + 1, r = 2 * i + 2, j = i;
		if (l < n && data[i] < data[l]){
			i = l;
		}
		if (r < n && data[i] < data[r]){
			i = r;
		}
		if (i == j){
			break;
		}
		int temp = data[i];
		data[i] = data[j];
		data[j] = temp;
	}
}


void build(int n, int *data){
	for (int i = (n-1) / 2; i >= 0; i--){
		heapify(i, n, data);
	}
}


void hsort(int n, int *data){
	build(n, data);
	for (int i = n-1; i > 0; i--){
		int temp = data[0];
		data[0] = data[i];
		data[i] = temp;
		heapify(0, i, data);
	}
}


int main(){
	int n;
	scanf("%d", &n);
	int *arr = (int*)calloc(n+1, sizeof(int));
	for (int i = 0; i < n; i++){
		scanf("%d", &arr[i]);
	}
	
	hsort(n, arr);
	
	printf("%d", arr[0]);
	for (int i = 1; i < n; i++){
		printf(" %d", arr[i]);
	}
	printf("\n");
	
	free(arr);
}