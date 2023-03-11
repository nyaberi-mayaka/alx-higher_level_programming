#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: the first node of the list
 *
 * Return:  0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{

	q_t *front = NULL;
	q_t *rear = NULL;
	int len = 0, i, free_check = 0;
	listint_t *temp = NULL;

	if (*head == NULL)
		return (1);

	temp = *head;
	while (temp->next != NULL)
	{
		enqueue(&front, &rear, temp->n);
		temp = temp->next, len++;
	}
	enqueue(&front, &rear, temp->n);

	for (i = 0; i <= len / 2; i++)
	{
		free_check++;

		if (dequeue_front(&front) != dequeue_rear(&rear))
		{
			if (front && rear)
				frees(front);
			return (0);
		}
		if (front == rear)
		{
			frees(front);
			break;
		}
	}
	if (front && rear)
		frees(front);

	return (1);
}



/**
* enqueue - stores a value into a queue
* @front: pointer to the front of the queue
* @rear: pointer to the rear of the queue
* @x: value to store
* Return: value stored in the rear most node
*/

void enqueue(q_t **front, q_t **rear, int x)
{
	q_t *newnode = malloc(sizeof(q_t));

	newnode->data = x;
	newnode->next = newnode->prev = NULL;

	if (*front == NULL && *rear == NULL)
		*front = *rear = newnode;
	else
	{
		(*rear)->next = newnode;
		newnode->prev = *rear;
		*rear = newnode;
	}
}
/**
* dequeue_rear - pops the rearmost value of a queue
* @rear: pointer to the rear of the queue
* Return: value stored in the rear most node
*/

int dequeue_rear(q_t **rear)
{
	q_t *temp = NULL;
	int ret;

	if (!*rear)
		exit(1);

	temp = *rear;

	ret = temp->data;

	if (temp->prev == NULL)
	{
		free(temp);
		*rear = NULL;
	}
	else
	{
		temp = temp->prev;
		free(*rear);
		*rear = temp;
		temp->next = NULL;
	}
	return (ret);
}
/**
* dequeue_front - pops the frontmost value of a queue
* @front: pointer to the front of the queue
* Return: value stored in the front most node
*/

int dequeue_front(q_t **front)
{
	q_t *temp = NULL;
	int ret;

	if (!*front)
		exit(1);

	temp = *front;

	ret = temp->data;

	if (temp->next == NULL)
	{
		free(temp);
		*front = NULL;
	}
	else
	{
		temp = temp->next;
		free(*front);
		*front = temp;
		temp->prev = NULL;
	}
	return (ret);
}

/**
 * frees - frees a non-empty queue
 * @front: pointer to the front of queue
 */
void frees(q_t *front)
{
	q_t *temp = front;

	while (front)
	{
		temp = temp->next;
		free(front);
		front = temp;
	}
}
