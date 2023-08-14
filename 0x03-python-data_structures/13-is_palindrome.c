#include "lists.h"

/**
 * reverse_listint - reverses the linked list
 * @head: pointer to the start of the node.
 * Return: pointer to reverse node
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *nxt, *prv = NULL;

	while (node)
	{
		nxt = node->next;
		node->next = prv;
		prv = node;
		node = nxt;
	}
	*head = prv;
	return (*head);
}

/**
 * is_palindrome - Checks for a palindrome
 * @head: pointer to the linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid_p;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid_p = rev;
	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid_p);
	return (1);
}
