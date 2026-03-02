/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_hex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 21:03:57 by mboubaza          #+#    #+#             */
/*   Updated: 2025/12/14 15:27:42 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	hex_len(unsigned int nbr)
{
	int	count;

	if (nbr == 0)
		return (1);
	count = 0;
	while (nbr != 0)
	{
		nbr = nbr / 16;
		count++;
	}
	return (count);
}

static void	pr_hex(unsigned int nbr, char *base)
{
	char	c;

	if (nbr / 16 != 0)
		pr_hex(nbr / 16, base);
	c = base[nbr % 16];
	write(1, &c, 1);
}

int	print_hex(unsigned int nbr, char c)
{
	if (c == 'X')
		pr_hex(nbr, "0123456789ABCDEF");
	else if (c == 'x')
		pr_hex(nbr, "0123456789abcdef");
	return (hex_len(nbr));
}
