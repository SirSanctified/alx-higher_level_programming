#include "lists.h"
#include<stdlib.h>

/**
 * insert_node - insert a node into a sorted list
 * @head: pointer to head pointer of the list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pred;
	listint_t *curr = *head;
	listint_t *node;

	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
	}
	else if (node->n < curr->n)
	{
		node->next = curr;
		*head = node;
	}
	else
	{
		while (curr->n <= node->n && curr->next != NULL)
		{
			pred = curr;
			curr = curr->next;
		}
		if (curr->next != NULL)
		{
			node->next = curr;
			pred->next = node;
		}
		else
		{
			if (curr->n < node->n)
			{
				curr->next = node;
			}
			else
			{
				pred->next = node;
				node->next = curr;
			}
		}
	}
	return (node);
}
