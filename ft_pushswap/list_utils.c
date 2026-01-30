/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 16:16:00 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/30 16:16:00 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	free_stack(t_stack_node **stack)
{
	t_stack_node	*curr;
	t_stack_node	*next;

	if (!stack || !*stack)
		return ;
	curr = *stack;
	while (curr)
	{
		next = curr->next_n;
		free(curr);
		curr = next;
	}
	*stack = NULL;
}

t_stack_node	*find_last(t_stack_node *stack)
{
	if (!stack)
		return (NULL);
	while (stack->next_n)
		stack = stack->next_n;
	return (stack);
}

int	stack_len(t_stack_node **head)
{
	t_stack_node	*current;
	int				i;

	if (!head || !*head)
		return (0);
	i = 0;
	current = *head;
	while (current)
	{
		i++;
		current = current->next_n;
	}
	return (i);
}

t_stack_node	*new_n(int nbr)
{
	t_stack_node	*new_node;

	new_node = malloc(sizeof(t_stack_node));
	if (!new_node)
		return (NULL);
	new_node->nbr = nbr;
	new_node->next_n = NULL;
	new_node->prev_n = NULL;
	new_node->index = 0;
	new_node->push_c = 0;
	new_node->ab_med = 0;
	new_node->target_n = NULL;
	return (new_node);
}

void	stack_add_back(t_stack_node **stack, int nbr)
{
	t_stack_node	*new_node;
	t_stack_node	*last_node;

	if (!stack)
		return ;
	new_node = new_n(nbr);
	if (!new_node)
		return ;
	if (!*stack)
	{
		*stack = new_node;
	}
	else
	{
		last_node = find_last(*stack);
		last_node->next_n = new_node;
		new_node->prev_n = last_node;
	}
}
