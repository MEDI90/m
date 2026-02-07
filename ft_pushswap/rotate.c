/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 17:44:33 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/20 18:15:49 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	rotate(t_stack_node **head)
{
	t_stack_node	*first;
	t_stack_node	*last;

	if (!head || !*head || !(*head)->next_n)
		return ;
	first = *head;
	last = *head;
	while (last->next_n)
		last = last->next_n;
	last->next_n = first;
	*head = first->next_n;
	(*head)->prev_n = NULL;
	first->prev_n = last;
	first->next_n = NULL;
}

void	ra(t_stack_node **a)
{
	rotate(a);
	write(1, "ra\n", 3);
}

void	rb(t_stack_node **b)
{
	rotate(b);
	write(1, "rb\n", 3);
}

void	rr(t_stack_node **a, t_stack_node **b)
{
	rotate(a);
	rotate(b);
	write(1, "rr\n", 3);
}
