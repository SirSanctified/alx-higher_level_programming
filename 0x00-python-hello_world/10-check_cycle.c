#include "lists.h"

/**
 * check_cycle - check if the list contains a cycle
 * @list: the head ponter of the linked list
 *
 * Description: detect a cycle
 * Return: 0 if no cycle is detected else 1
 */

 int check_cycle(listint_t *list)
 {
		 listint_t *fast = list;
		 listint_t *slow = list;

		while (fast != NULL && fast->next != NULL && slow != NULL)
		{
				fast = fast->next->next;
				slow = slow->next;

				if (fast == slow)
						return (1);
		}
		return (0);
 }


