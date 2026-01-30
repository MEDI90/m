/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 16:16:00 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/30 16:16:00 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack_node	*min_node(t_stack_node **stack)
{
	t_stack_node	*min_n;
	t_stack_node	*current;

	min_n = *stack;
	current = *stack;
	while (current)
	{
		if (current->nbr < min_n->nbr)
			min_n = current;
		current = current->next_n;
	}
	return (min_n);
}

t_stack_node	*max_node(t_stack_node **stack)
{
	t_stack_node	*max_n;
	t_stack_node	*current;

	max_n = *stack;
	current = *stack;
	while (current)
	{
		if (current->nbr > max_n->nbr)
			max_n = current;
		current = current->next_n;
	}
	return (max_n);
}

t_stack_node	*lowest_c(t_stack_node **a)
{
	t_stack_node	*current;
	t_stack_node	*push;

	current = *a;
	push = *a;
	while (current)
	{
		if (current->push_c < push->push_c)
			push = current;
		current = current->next_n;
	}
	return (push);
}

static int	cost_calc(t_stack_node *node, int len)
{
	if (node->ab_med == 1)
		return (node->index);
	else
		return (len - node->index);
	return (0);
}

void	init_cost(t_stack_node **a, t_stack_node **b)
{
	t_stack_node	*current;
	int				len_a;
	int				len_b;

	len_a = stack_len(a);
	len_b = stack_len(b);
	current = *a;
	while (current)
	{
		if (current->ab_med == current->target_n->ab_med)
		{
			if (cost_calc(current, len_a) > cost_calc(current->target_n, len_b))
				current->push_c = cost_calc(current, len_a) + 1;
			else
				current->push_c = cost_calc(current->target_n, len_b) + 1;
		}
		else
			current->push_c = cost_calc(current->target_n, len_b)
				+ cost_calc(current, len_a) + 1;
		current = current->next_n;
	}
}
