#include "lists.h"
/**
 * sum_dlistint - Function that adds all the data (n) of a list.
 * @head: pointer to dlistint_t head
 * Return: sum
 */
int sum_dlistint(dlistint_t *head)
{
	int sum = 0;

	while (head)
	{
		sum += head->n;
		head = head->next;
	}
	return (sum);
}
