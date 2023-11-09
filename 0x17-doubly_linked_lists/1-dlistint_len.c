#include <stdio.h>
#include "lists.h"

/**
 * dlistint_len - Function that counts the length of the list.
 * @h - head of doubly linked list
 *
 * Return - Yeilds the total number of nodes.
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}
	return (count);
}
