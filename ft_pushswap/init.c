/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 22:41:09 by mboubaza          #+#    #+#             */
/*   Updated: 2026/02/13 18:50:04 by mboubaza         ###   ########.fr       */
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

static void	handle_error(t_stack_node **a, char **arr)
{
	free_stack(a);
	free_split(arr);
	write(2, "Error\n", 6);
	exit(1);
}

void	init_stack(t_stack_node **a, char **av)
{
	char	**stack_arr;
	int		i;
	int		j;
	int		error;
	long	n;

	i = 1;
	while (av[i ++])
	{
		error = 0;
		// if ((word_counter(av[i - 1], ' ') == 0) || (*av[i - 1] == 0))
		// 	handle_error(a, NULL);
		stack_arr = ft_split(av[i - 1], ' ');
		if (!stack_arr || !stack_arr[0])
			handle_error(a, NULL);
		j = 0;
		while (stack_arr[j ++])
		{
			n = ft_atol(stack_arr[j - 1], &error);
			if (error)
				handle_error(a, stack_arr);
			stack_add_back(a, (int)n);
		}
		free_split(stack_arr);
	}
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
