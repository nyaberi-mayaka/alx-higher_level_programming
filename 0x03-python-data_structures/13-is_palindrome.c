#include "lists.h"

void push(list_t **, listint_t *);
int pop(list_t **);
void frees(list_t *head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: the first node of the list
 *
 * Return:  0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	list_t *front = NULL;
	listint_t *slow, *fast, *curr, *p1;
	int flag = 0;

	if (head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
/*Find the middle of the list using the "slow and fast" pointer technique*/
	slow = fast = *head;
	while (fast != NULL && fast->next != NULL)
		slow = slow->next, fast = fast->next->next;

/*create a stack*/
	curr = slow;
	while (curr != NULL)
	{
		push(&front, curr);
		curr = curr->next;
	}
/*check if the first half of the list match and the stack match*/
	p1 = *head;
	while (front)
	{
		if (p1->n == pop(&front))
			p1 = p1->next;

		else
		{
			flag = 1;
			frees(front);
			break;
		}
	}
	return (flag == 0 ? 1 : 0);
}


/**
 * push - adds a new element to the top of stack
 * @temp: the data to store on top of the stack
 * @head: the address of the top most element of the stack
 */

void push(list_t **head, listint_t *temp)
{
	list_t *newnode = malloc(sizeof(list_t));

	if (newnode == NULL)
	{
		printf("Unable to allocate memory\n");
		return;
	}

	newnode->data = temp;
	newnode->next = *head;
	*head = newnode;
}

/**
 * pop - removes the top most element of the stack
 * @head: location of the top most element of the stack
 * Return: the value of the intger stored by the linked list node of
 * the top most element of the stack
 */

int pop(list_t **head)
{
	int x;
	list_t *temp;

	temp = *head;
	*head = temp->next;
	x = temp->data->n;
	free(temp);

	return (x);
}

/**
 * frees - frees a stack data structure
 * @head: pointer to the first node of the structure
 */

void frees(list_t *head)
{
	list_t *temp = head;

	while (temp)
	{
		temp = temp->next;

		/*free(head->data);*/
		free(head);
		head = temp;
	}
}
