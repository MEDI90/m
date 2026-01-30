/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_target.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 16:16:00 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/30 16:16:00 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	get_best_match(t_stack_node *a, t_stack_node **b)
{
	t_stack_node	*current_b;
	t_stack_node	*target;
	long			best_match_val;

	current_b = *b;
	best_match_val = -2147483649;
	target = max_node(b);
	while (current_b)
	{
		if (current_b->nbr < a->nbr && current_b->nbr > best_match_val)
		{
			best_match_val = current_b->nbr;
			target = current_b;
		}
		current_b = current_b->next_n;
	}
	a->target_n = target;
}

void	init_target_b(t_stack_node **a, t_stack_node **b)
{
	t_stack_node	*current_a;
	t_stack_node	*current_b;
	t_stack_node	*target;
	long			best_match_val;

	current_b = *b;
	while (current_b)
	{
		best_match_val = 2147483648;
		target = min_node(a);
		current_a = *a;
		while (current_a)
		{
			if (current_a->nbr > current_b->nbr
				&& current_a->nbr < best_match_val)
			{
				best_match_val = current_a->nbr;
				target = current_a;
			}
			current_a = current_a->next_n;
		}
		current_b->target_n = target;
		current_b = current_b->next_n;
	}
}

void	init_target(t_stack_node **a, t_stack_node **b)
{
	t_stack_node	*current_a;

	current_a = *a;
	while (current_a)
	{
		get_best_match(current_a, b);
		current_a = current_a->next_n;
	}
}

void	init_nodes(t_stack_node **a, t_stack_node **b)
{
	init_i(a);
	init_i(b);
	init_abmed(a);
	init_abmed(b);
	init_target(a, b);
	init_cost(a, b);
}
