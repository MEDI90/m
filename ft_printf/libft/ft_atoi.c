/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 12:25:52 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/04 15:01:37 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	sign_check(int nb)
{
	if (nb > 0)
		return (0);
	else
		return (-1);
}

int	ft_atoi(const char *nptr)
{
	int		i;
	int		sign;
	long	nbr;
	long	pv;

	i = 0;
	nbr = 0;
	sign = 1;
	while (nptr[i] == ' ' || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	if (nptr[i] == '+' || nptr[i] == '-')
	{
		if (nptr[i] == '-')
			sign = -1;
		i++;
	}
	while (nptr[i] >= '0' && nptr[i] <= '9')
	{
		pv = nbr;
		nbr = nbr * 10 + (nptr[i] - '0');
		if (nbr / 10 != pv)
			return (sign_check((int)nbr));
		i++;
	}
	return (nbr * sign);
}
