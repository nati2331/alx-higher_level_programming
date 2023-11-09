#include "lists.h"
/**
 * free_dlistint - Funtion frees all the elements.
 * @head: pointer
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current;

	current = head;
	while (head)
	{
		current = head;
		head = head->next;
		if (current)
			free(current);
	}
}
