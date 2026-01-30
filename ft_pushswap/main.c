/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 15:06:46 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/30 16:03:26 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	check_dup(t_stack_node *a)
{
	t_stack_node	*tmp;

	while (a)
	{
		tmp = a->next_n;
		while (tmp)
		{
			if (a->nbr == tmp->nbr)
				return (1);
			tmp = tmp->next_n;
		}
		a = a->next_n;
	}
	return (0);
}

static int	stack_sorted(t_stack_node *stack)
{
	if (!stack)
		return (1);
	while (stack->next_n)
	{
		if (stack->nbr > stack->next_n->nbr)
			return (0);
		stack = stack->next_n;
	}
	return (1);
}

int	main(int ac, char **av)
{
	t_stack_node	*stack_b;
	t_stack_node	*stack_a;

	stack_a = NULL;
	stack_b = NULL;
	if (ac == 1 || (ac == 2 && !av[1][0]))
		return (1);
	init_stack(&stack_a, ac, av);
	if (check_dup(stack_a))
	{
		free_stack(&stack_a);
		write(2, "Error\n", 6);
		return (1);
	}
	if (!stack_sorted(stack_a))
	{
		if (stack_len(&stack_a) == 2)
			sa(&stack_a);
		else
			turk(&stack_a, &stack_b);
	}
	free_stack(&stack_a);
	return (0);
}
