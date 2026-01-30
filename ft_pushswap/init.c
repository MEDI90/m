/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 22:41:09 by mboubaza          #+#    #+#             */
/*   Updated: 2026/01/30 15:41:38 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	free_split(char **str)
{
	int	i;

	i = 0;
	if (!str)
		return ;
	while (str[i])
	{
		free(str[i]);
		i++;
	}
	free(str);
}

static void	handle_error(t_stack_node **a, char **arr, int ac)
{
	free_stack(a);
	if (ac == 2)
		free_split(arr);
	write(2, "Error\n", 6);
	exit(1);
}

void	init_stack(t_stack_node **a, int ac, char **av)
{
	char	**stack_arr;
	int		i;
	int		error;
	long	n;

	error = 0;
	i = 0;
	if (ac == 2)
		stack_arr = ft_split(av[1], ' ');
	else
		stack_arr = av + 1;
	while (stack_arr[i])
	{
		n = ft_atol(stack_arr[i], &error);
		if (error)
			handle_error(a, stack_arr, ac);
		stack_add_back(a, (int)n);
		i++;
	}
	if (ac == 2)
		free_split(stack_arr);
}

void	init_i(t_stack_node **stack)
{
	int				i;
	t_stack_node	*current;

	if (!stack || !*stack)
		return ;
	current = *stack;
	i = 0;
	while (current)
	{
		current->index = i;
		current = current->next_n;
		i++;
	}
}

void	init_abmed(t_stack_node **head)
{
	int				len;
	t_stack_node	*node;

	len = stack_len(head);
	node = *head;
	while (node)
	{
		if (len / 2 >= node->index)
			node->ab_med = 1;
		else
			node->ab_med = 0;
		node = node->next_n;
	}
}
