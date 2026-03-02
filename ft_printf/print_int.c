/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_int.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 17:57:18 by mboubaza          #+#    #+#             */
/*   Updated: 2025/12/14 15:02:16 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	ft_putnbr(long nbr, int count)
{
	char	c;

	if (nbr / 10 != 0)
		count += ft_putnbr(nbr / 10, count);
	c = nbr % 10 + '0';
	write(1, &c, 1);
	return (++count);
}

int	print_int(int nbr)
{
	long	nb;
	int		nig;

	nig = 0;
	nb = (long)nbr;
	if (nb < 0)
	{
		write(1, "-", 1);
		nb = -nb;
		nig = 1;
	}
	return (ft_putnbr(nb, 0) + nig);
}
