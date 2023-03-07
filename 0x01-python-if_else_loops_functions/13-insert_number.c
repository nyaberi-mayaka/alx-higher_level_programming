#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: address of first node of the list.
 * @number: the number to insert.
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL, *temp = NULL;

	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);
	newnode->n = number, newnode->next = NULL;

	if (!*head)
	{
		*head = newnode;
		return (newnode);
	}
	temp = *head;
	while (temp->next != NULL)
	{
		if (temp->next->n > number)
			break;
		temp = temp->next;
	}

	newnode->next = temp->next;
	temp->next = newnode;

	return (newnode);
}
