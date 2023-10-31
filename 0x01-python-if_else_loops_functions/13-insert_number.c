#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -it is a function that insters the linked list.
 * @head: it is a poniter to the head.
 * @number: It is the number to insert.
 *
 * Return: To a new node upon sucess and null if it fail.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
