/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 21:21:24 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/26 06:01:22 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	rev_rotate(t_stack_node **head)
{
	t_stack_node	*last;

	if (!head || !*head || !(*head)->next_n)
		return ;
	last = *head;
	while (last->next_n)
		last = last->next_n;
	last->prev_n->next_n = NULL;
	last->next_n = *head;
	last->next_n->prev_n = last;
	last->prev_n = NULL;
	*head = last;
}

void	rra(t_stack_node **a)
{
	rev_rotate(a);
	write(1, "rra\n", 4);
}

void	rrb(t_stack_node **b)
{
	rev_rotate(b);
	write(1, "rrb\n", 4);
}

void	rrr(t_stack_node **a, t_stack_node **b)
{
	rev_rotate(a);
	rev_rotate(b);
	write(1, "rrr\n", 4);
}
