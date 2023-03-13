#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: the first node of the list
 *
 * Return:  0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *curr, *nxt, *p2, *p1, *temp;
	int flag = 0;

	if (head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
/*Find the middle of the list using the "slow and fast" pointer technique*/
	slow = fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		temp = slow;
		slow = slow->next, fast = fast->next->next;
	}

/*Reverse the second half of the list*/
	prev = NULL, curr = slow, nxt = NULL;
	while (curr != NULL)
	{
		nxt  = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}

/*check if the two halves of the list match*/
	p1 = *head, p2 = prev;
	while (p2 && p1)
	{
		if (p1->n == p2->n)
			p1 = p1->next,	p2 = p2->next;

		else
		{
			flag = 1;
			break;
		}
	}
	temp->next = prev;
	return (flag == 0 ? 1 : 0);
}
