/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_addr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 00:14:43 by mboubaza          #+#    #+#             */
/*   Updated: 2025/12/14 15:02:08 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	hex_len(unsigned long nbr)
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

static void	pr_hex(unsigned long nbr)
{
	if (nbr / 16 != 0)
		pr_hex(nbr / 16);
	write(1, &"0123456789abcdef"[nbr % 16], 1);
}

int	print_addr(void *addr)
{
	unsigned long	ptr;

	if (!addr)
	{
		write(1, "(nil)", 5);
		return (5);
	}
	ptr = (unsigned long)addr;
	write(1, "0x", 2);
	pr_hex(ptr);
	return (hex_len(ptr) + 2);
}
