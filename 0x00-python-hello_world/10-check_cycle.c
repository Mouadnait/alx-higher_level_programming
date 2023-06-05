#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *single_hop, *triple_hop;

	if (list == NULL || list->next == NULL)
		return (0);

	single_hop = list->next;
	triple_hop = list->next->next;

	while (single_hop && triple_hop && triple_hop->next)
	{
		if (single_hop == triple_hop)
			return (1);

		single_hop = single_hop->next;
		triple_hop = triple_hop->next->next;
	}

	return (0);
}
