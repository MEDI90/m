/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 16:16:00 by mboubaza          #+#    #+#             */
/*   Updated: 2026/02/13 18:02:17 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft/libft.h"

long				ft_atol(const char *nptr, int *error);

typedef struct node
{
	int				nbr;
	int				index;
	int				push_c;
	int				ab_med;
	int				push;
	struct node		*target_n;
	struct node		*next_n;
	struct node		*prev_n;
}	t_stack_node;

/* --------------------------- List Utils --------------------------------- */
t_stack_node		*find_last(t_stack_node *stack);
t_stack_node		*new_n(int nbr);
int					stack_len(t_stack_node **head);
void				stack_add_back(t_stack_node **stack, int nbr);
void				free_stack(t_stack_node **stack);
void				turk(t_stack_node **stack_a, t_stack_node **stack_b);
t_stack_node		*max_node(t_stack_node **stack);
t_stack_node		*min_node(t_stack_node **stack);

/* ----------------------------- Init ------------------------------------ */
void				init_stack(t_stack_node **a, char **av);
void				init_nodes(t_stack_node **a, t_stack_node **b);
void				init_i(t_stack_node **stack);
void				init_abmed(t_stack_node **head);
void				init_target(t_stack_node **a, t_stack_node **b);
void				init_target_b(t_stack_node **a, t_stack_node **b);
void				init_cost(t_stack_node **a, t_stack_node **b);
t_stack_node		*lowest_c(t_stack_node **a);
int					word_counter(char *str, char c);

/* ----------------------------- Moves ------------------------------------ */
void				sa(t_stack_node **a);
void				sb(t_stack_node **b);
void				ss(t_stack_node **a, t_stack_node **b);
void				pa(t_stack_node **a, t_stack_node **b);
void				pb(t_stack_node **b, t_stack_node **a);
void				ra(t_stack_node **a);
void				rb(t_stack_node **b);
void				rr(t_stack_node **a, t_stack_node **b);
void				rra(t_stack_node **a);
void				rrb(t_stack_node **b);
void				rrr(t_stack_node **a, t_stack_node **b);

#endif
