/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_uint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 18:36:42 by mboubaza          #+#    #+#             */
/*   Updated: 2025/12/14 15:02:17 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	ft_putnbr(unsigned int nbr, int count)
{
	char	c;

	if (nbr / 10 != 0)
		count += ft_putnbr(nbr / 10, count);
	c = nbr % 10 + '0';
	write(1, &c, 1);
	return (++count);
}

int	print_uint(unsigned int nbr)
{
	return (ft_putnbr(nbr, 0));
}
