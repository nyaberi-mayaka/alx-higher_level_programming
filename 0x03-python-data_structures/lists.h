#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

typedef struct queue
{
	int data;
	struct queue *next, *prev;
} q_t;

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

void enqueue(q_t **, q_t **, int);
int dequeue_front(q_t **);
int dequeue_rear(q_t **);
void frees(q_t *);

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
