/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   turk.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 01:47:42 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/26 06:46:36 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	executioner(t_stack_node **a, t_stack_node **b)
{
	t_stack_node	*ready_n;

	ready_n = lowest_c(a);
	if (ready_n->ab_med == 1 && ready_n->target_n->ab_med == 1)
		while (*a != ready_n && *b != ready_n->target_n)
			rr(a, b);
	else if (ready_n->ab_med == 0 && ready_n->target_n->ab_med == 0)
		while (*a != ready_n && *b != ready_n->target_n)
			rrr(a, b);
	if (ready_n->ab_med == 0)
		while (*a != ready_n)
			rra(a);
	else if (ready_n->ab_med == 1)
		while (*a != ready_n)
			ra(a);
	if (ready_n->target_n->ab_med == 0)
		while (*b != ready_n->target_n)
			rrb(b);
	else if (ready_n->target_n->ab_med == 1)
		while (*b != ready_n->target_n)
			rb(b);
	pb(a, b);
}

void	executioner_b(t_stack_node **a, t_stack_node **b)
{
	t_stack_node	*ready_n;

	ready_n = *b;
	if (ready_n->target_n->ab_med == 1)
		while (*a != ready_n->target_n)
			ra(a);
	else if (ready_n->target_n->ab_med == 0)
		while (*a != ready_n->target_n)
			rra(a);
	pa(a, b);
}

void	sort_tree(t_stack_node **stack)
{
	t_stack_node	*biggest;

	biggest = max_node(stack);
	if (stack_len(stack) > 2)
	{
		if (*stack == biggest)
			ra(stack);
		else if ((*stack)->next_n == biggest)
			rra(stack);
	}
	if ((*stack)->nbr > (*stack)->next_n->nbr)
		sa(stack);
}

static void	final_rotate(t_stack_node **stack)
{
	t_stack_node	*min;

	init_i(stack);
	init_abmed(stack);
	min = min_node(stack);
	if (min->ab_med == 1)
		while (*stack != min)
			ra(stack);
	else
		while (*stack != min)
			rra(stack);
}

void	turk(t_stack_node **stack_a, t_stack_node **stack_b)
{
	if (!stack_a || !*stack_a)
		return ;
	if (stack_len(stack_a) > 3 && !*stack_b)
		pb(stack_a, stack_b);
	if (stack_len(stack_a) > 3 && !*stack_b)
		pb(stack_a, stack_b);

	while (stack_len(stack_a) > 3)
	{
		init_nodes(stack_a, stack_b);
		executioner(stack_a, stack_b);
	}
	sort_tree(stack_a);
	while (*stack_b)
	{
		init_i(stack_a);
		init_i(stack_b);
		init_abmed(stack_a);
		init_abmed(stack_b);
		init_target_b(stack_a, stack_b);
		executioner_b(stack_a, stack_b);
	}
	final_rotate(stack_a);
}
