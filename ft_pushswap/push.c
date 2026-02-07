/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 02:11:08 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/20 11:58:31 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	push(t_stack_node **src, t_stack_node **dest)
{
	t_stack_node	*tmp;

	if (!src || !*src)
		return ;
	tmp = *src;
	*src = (*src)->next_n;
	if (*src)
		(*src)->prev_n = NULL;
	tmp->prev_n = NULL;
	if (!*dest)
	{
		*dest = tmp;
		tmp->next_n = NULL;
	}
	else
	{
		tmp->next_n = *dest;
		tmp->next_n->prev_n = tmp;
		*dest = tmp;
	}
}

void	pb(t_stack_node **stack_a, t_stack_node **stack_b)
{
	push(stack_a, stack_b);
	write(1, "pb\n", 3);
}

void	pa(t_stack_node **stack_a, t_stack_node **stack_b)
{
	push(stack_b, stack_a);
	write(1, "pa\n", 3);
}
