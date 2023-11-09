#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * get_dnodeint_at_index - Funtion returns the nth node of the list.
 * @head: pointer
 * @index: index tryying to find
 *
 * Return: NULL if index does not exist or address on sucess.
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *tmpcount = head;
	unsigned int count = 0;

	if (!head)
		return (NULL);

	while (tmpcount)
		tmpcount = tmpcount->next, count++;

	if (index > (count - 1))
		return (NULL);

	for (count = 0; count < index; count++)
		head = head->next;

	return (head);
}
