#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - it is a function that checks if the linked list contains a cycle.
 * @list: Ait is the linked list.
 *
 * Return: o if it does not have a cycle and 1 if it does.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
