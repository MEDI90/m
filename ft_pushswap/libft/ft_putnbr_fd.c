/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mboubaza <mboubaza@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 19:47:10 by mboubaza          #+#    #+#             */
/*   Updated: 2025/11/04 00:13:48 by mboubaza         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	char	c;
	long	nbr;

	nbr = (long)n;
	if (n < 0)
	{
		write(fd, "-", 1);
		nbr = -nbr;
	}
	if (nbr / 10 != 0)
		ft_putnbr_fd(nbr / 10, fd);
	c = nbr % 10 + '0';
	write(fd, &c, 1);
}
