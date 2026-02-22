/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 16:52:43 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/02 20:32:21 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	len_int(long n)
{
	int	i;

	i = 0;
	while (n / 10 != 0)
	{
		n = n / 10;
		i++;
	}
	return (i);
}

static void	convert(char *str, long n)
{
	if (n / 10 != 0)
		convert(str - 1, n / 10);
	*str = n % 10 + '0';
}

char	*ft_itoa(int n)
{
	char	*str;
	int		len;
	long	nbr;
	int		sign;

	nbr = (long)n;
	sign = 0;
	if (n < 0)
	{
		sign = 1;
		nbr = -nbr;
	}
	len = len_int(nbr) + 1;
	str = malloc(sizeof(char) * (len + sign + 1));
	if (!str)
		return (NULL);
	if (sign == 1)
		str[0] = '-';
	str[len + sign] = '\0';
	convert(str + len - 1 + sign, nbr);
	return (str);
}
